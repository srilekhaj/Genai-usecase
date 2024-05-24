import streamlit as st
from routingprompt import navigator
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from  routingprompt import llm
from Speech.speech import SpeechToText
from logger import Logger

@st.cache_resource
def initialize():
    pass
 
st.session_state.chat=initialize()
 
st.title("Customer Support Chatbot 🤖🏦")
 
if "messages" not in st.session_state:
    # Welcome Message
    welcome_message = """**<h3>Welcome to our payment and banking support chat!**</h3>\n\nHow can we assist you?\n\nWe're delighted to help with any inquiries about your financial transactions.\nWhether it's making payments, checking balances, or resolving banking issues, 
    our team is here for you.\n\nJust type your query in the chatbox, and we'll swiftly provide the support you need.\nFor security purposes, please refrain from sharing sensitive information such as account numbers or passwords during this chat.\n\nLet's get started! 🚀    """

    st.session_state.messages = [{"role": "assistant", "content": welcome_message}]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"],unsafe_allow_html=True)

# Main Page
if "prompt" not in st.session_state:
    st.session_state["prompt"] = ""
if "logger" not in st.session_state:
    st.session_state["logger"] = None
if "stt" not in st.session_state:
    st.session_state["stt"] = None

col1, col2,_,col3 = st.columns(4)
with col2:
    if st.button("Speak Prompt"):
        st.session_state.api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss"
        st.session_state.stt = SpeechToText()
        prompt = st.session_state.stt.listen_and_convert()
        print(prompt)
        print(st.session_state['prompt'])# = prompt

if prompt := st.chat_input("Enter Question"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    prompt ="Hi I am Alice Smith. " + prompt
    greet_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful personal banking assistant named Intelli. Your boss is Alice Smith. Assume you have access to a banking database.
                If the user requests for information of other customers, return a 0.
                If the user asks anything outside the banking domain, return a 0.
                Return 1 when the users asks valid questions related to his personal banking needs.
                Return 1 when user asks general wealth management related questions, banking faq and credit card related questions.


                The output should be ONLY one of 0 or 1...

                """
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    chain = greet_prompt | llm
    res = chain.invoke(
        {
            "messages":[
                HumanMessage(
                    content=prompt
                )
            ]
        }
    )

    response = "Sorry I am unable to assist with your query at the moment"
    if res.content =='1':
        response = navigator(prompt) # Backend

    
    with st.chat_message("assistant"):
        st.markdown(response,unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})
