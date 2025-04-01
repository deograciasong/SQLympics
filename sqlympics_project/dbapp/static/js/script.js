const chatbotIcon = document.getElementById('chatbot-icon');
const chatbotPopup = document.getElementById('chatbot-popup');
const closeChatbot = document.getElementById('close-chatbot');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const chatbotBody = document.getElementById('chatbot-body');

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
