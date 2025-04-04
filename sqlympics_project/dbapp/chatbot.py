from openai import OpenAI
import mysql.connector
import re

# Load OpenAI API key from file
import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)


# ✅ SQLympics schema passed to GPT
schema_description = """
You are working with a MySQL database named SQLympics. Table and column names are case-sensitive.

Schema:
USER(user_id [PK], first_name, last_name, email, password, role)
STUDENT(user_id [FK to USER], initial_rank_id, total_score, current_rank_id)
INSTRUCTOR(user_id [FK to USER], department_id)
QUESTIONS(question_id [PK], title, difficulty, created_by)
TEST(test_id [PK], student_id [FK], score, taken_at)
TESTQUESTION(test_id [FK], question_id [FK], is_correct, time_taken)
CLASSROOM(classroom_id [PK], name, instructor_id [FK])
RANKS(rank_id [PK], title, min_score)
FEEDBACK(feedback_id [PK], student_id [FK], instructor_id [FK], content, sent_date)
MESSAGE(message_id [PK], sender_id [FK], receiver_id [FK], content, sent_date)

Always generate only valid MySQL queries. Do NOT return markdown (```sql), explanations, or comments. Only return the raw SQL query text.
"""

# 🧽 Extract only the valid SQL from GPT response
def extract_sql_from_response(response_text):
    # Try extracting from ```sql blocks
    match = re.search(r"```sql(.*?)```", response_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Else, start collecting from first SQL keyword
    sql_lines = []
    started = False
    for line in response_text.splitlines():
        if any(line.strip().lower().startswith(kw) for kw in ["select", "insert", "update", "delete", "with"]):
            started = True
        if started:
            sql_lines.append(line)
    return "\n".join(sql_lines).strip()

# 🔄 Convert natural language to SQL
def get_sql_query(prompt):
    print(f"💬 User Prompt: {prompt}")

    messages = [
        {"role": "system", "content": schema_description},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.3,
        max_tokens=150
    )

    raw = response.choices[0].message.content
    print(f"🧠 OpenAI Raw Response:\n{raw}")

    clean_sql = extract_sql_from_response(raw)
    print(f"✅ SQL to Execute:\n{clean_sql}")
    return clean_sql

# 🧾 Execute the SQL and return HTML-formatted result
def execute_sql(sql_query):
    try:
        conn = mysql.connector.connect(
            host="35.247.84.183",
            user="remote",
            password="password123!",
            database="SQLympics"
        )
        cursor = conn.cursor()
        cursor.execute(sql_query)

        if sql_query.strip().lower().startswith("select"):
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                return "No results found."

            # 🖼️ Format output as HTML table
            html = '<table border="1" style="border-collapse: collapse;">'
            html += '<tr>' + ''.join(f'<th>{col}</th>' for col in columns) + '</tr>'
            for row in rows:
                html += '<tr>' + ''.join(f'<td>{val}</td>' for val in row) + '</tr>'
            html += '</table>'
            return html

        else:
            conn.commit()
            return "Query executed successfully."

    except Exception as e:
        print(f"❌ SQL Execution Error: {e}")
        return f"Error: {e}"

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
