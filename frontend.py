
# 1.Setup UI with streamlit(model provider.model,system prompt,query)
import streamlit as st

st.set_page_config(page_title="LangGraph AI Agent UI",layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and interact with AI agnets")

system_prompt=st.text_area("Define your AI Agent: ",height=70,placeholder="Type your system prompt here")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.selectbox("Select Model Provider", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

#API_URL="http://localhost:8000/chat"

API_URL="https://agentic-chatbot-backend.onrender.com/chat"
if st.button("Ask Agent!"):
    if user_query.strip():
        #  2.Connect with backend via URL 
        import requests
        payload={
            "model_name":selected_model,
            "model_provider":provider,
            "system_prompt":system_prompt,
            "messages":[user_query],
            "allow_search":allow_web_search
        }

        response=requests.post(API_URL,json=payload)
        if response.status_code==200:
            response=response.json()
            if "error" in response:
                st.error(response["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"final respose-----{response}")
        else:
            st.error("Error: Unable to get a response from the server.")
        
#
