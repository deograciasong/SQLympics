// Handles SQL box query button
document.addEventListener("DOMContentLoaded", function () {
    const runBtn = document.getElementById("run-query");
    const sqlInput = document.getElementById("sql-input");
    const resultDiv = document.getElementById("query-result");

    if (runBtn && sqlInput && resultDiv) {
        runBtn.addEventListener("click", () => {
            const query = sqlInput.value.trim();
            if (!query) {
                resultDiv.innerHTML = "⚠️ Please enter a SQL query.";
                return;
            }

            fetch(`/chatbot/?prompt=${encodeURIComponent(query)}`)
                .then((res) => res.json())
                .then((data) => {
                    if (data.error) {
                        resultDiv.innerHTML = `<span style="color: red;"><strong>Error:</strong> ${data.error}</span>`;
                    } else {
                        resultDiv.innerHTML = `
                            <strong>SQL:</strong> ${data.sql}<br/>
                            <strong>Result:</strong> <pre>${JSON.stringify(data.result, null, 2)}</pre>
                        `;
                    }
                })
                .catch((err) => {
                    resultDiv.innerHTML = `<strong>Error:</strong> ${err}`;
                });
        });
    }

    // Optional: chatbot integration if also using chatbot popup in dashboard
    const chatbotIcon = document.getElementById('chatbot-icon');
    const chatbotPopup = document.getElementById('chatbot-popup');
    const closeChatbot = document.getElementById('close-chatbot');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const chatbotBody = document.getElementById('chatbot-body');

    if (chatbotIcon && chatbotPopup && closeChatbot && sendBtn && chatInput && chatbotBody) {
        chatbotIcon.addEventListener('click', () => {
            chatbotPopup.style.display = 'flex';
        });

        closeChatbot.addEventListener('click', () => {
            chatbotPopup.style.display = 'none';
        });

        sendBtn.addEventListener('click', () => {
            const userMessage = chatInput.value.trim();
            if (!userMessage) return;

            chatbotBody.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
            chatInput.value = '';

            fetch(`/chatbot/?prompt=${encodeURIComponent(userMessage)}`)
                .then(res => res.json())
                .then(data => {
                    const response = data.error
                        ? `<p><strong>Bot:</strong> Error: ${data.error}</p>`
                        : `<p><strong>Bot:</strong> SQL: ${data.sql}<br/>Result: ${JSON.stringify(data.result)}</p>`;
                    chatbotBody.innerHTML += response;
                    chatbotBody.scrollTop = chatbotBody.scrollHeight;
                });
        });
    }
});
