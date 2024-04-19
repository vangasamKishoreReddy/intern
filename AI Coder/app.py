import streamlit as st
import google.generativeai as gemini


st.title('Data Science Conversion Tutor - AI')

f = open(r"C:\Users\vkr20\Desktop\All Projects\Internship\Gen Ai\Keys\.Inten_ship_key3.txt")
api_key = f.read()

gemini.configure(api_key = api_key)
model = gemini.GenerativeModel(model_name = "gemini-1.5-pro-latest",
                               system_instruction = """You are AI Assistant to resolve data science
                               Queries of the user.""")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", 
         "content": "Hello, this is Gemini and how I can help you today?"}
    ]
    st.title("📢:blues[How can I assist you today?]")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input()

if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)