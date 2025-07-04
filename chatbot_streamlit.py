import streamlit as st
import json
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate

# Load prompt template
with open("v_prompt_template.json", "r") as f:
    data = json.load(f)

prompt_template = PromptTemplate.from_template(data["template"])

# Set Streamlit page title
st.set_page_config(page_title="Aura – Your Smart Daily Companion")
st.title("✨ Meet Aura – Your Friendly Everyday AI Assistant")

# Initialize the model
model = ChatOpenAI(  
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    model="mistralai/mistral-small-3.2-24b-instruct",
)

# Set up session history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
if prompt := st.chat_input("Ask me anything or tell me what you need help with 😊"):
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Ai is thinking..."):
            messages = [SystemMessage(content=prompt_template.template), HumanMessage(content=prompt)]
            response = model.invoke(messages)
            st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))
