# 🤖 Ai – Your Daily Life AI Assistant

This is a Streamlit-based chatbot application powered by **Meta-Llama 3 70B** via OpenRouter. It provides users with a clean and interactive interface to chat with an AI assistant for daily help, productivity, and general inquiries.

---

## 🚀 Features

- Built with **Streamlit** for a simple and modern chat interface
- Uses **Meta-Llama 3 (70B Instruct)** via **OpenRouter API**
- Persistent chat history using Streamlit session state
- Customizable system prompt via external template (`v_prompt_template.json`)
- Responsive AI replies with typing indicator spinner

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **OpenRouter API**
- **Meta Llama 3 Model**

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-assistant-chatbot.git
   cd ai-assistant-chatbot
pip install -r requirements.txt

OPENROUTER_API_KEY=your-api-key-here

streamlit run chatbot_streamlit.py

{
  "template": "You are Ai, a helpful assistant that provides clear and thoughtful responses."
}


