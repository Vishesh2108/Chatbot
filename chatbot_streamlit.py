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
st.set_page_config(page_title="Ai – Your Daily AI Assistant")
st.title("🤖 Meet Ai – Your Daily Life AI Assistant")

# Initialize the model
model = ChatOpenAI(  
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    model="meta-llama/llama-3.3-70b-instruct",
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
if prompt := st.chat_input("What can i help you with today?"):
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Ai is thinking..."):
            messages = [SystemMessage(content=prompt_template.template), HumanMessage(content=prompt)]
            response = model.invoke(messages)
            st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))
