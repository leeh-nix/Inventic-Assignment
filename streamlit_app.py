import streamlit as st

from utils.gemini import initialize_gemini
from utils.utils import generate_response


# Show title and description.
st.title("💬 Inventic Assignment")
st.write(
    "This is a simple chatbot that uses Gemini's 'gemini-1.5-flash' model to generate summary."
)

# Use the user's given API or the owner's API
gemini_api_key = (
    st.text_input("Gemini API Key", type="password") or st.secrets["GEMINI_API_KEY"]
)
if not gemini_api_key:
    st.info("Please add your Gemini API key to continue.", icon="🗝️")
else:

    client = initialize_gemini(gemini_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        # Store and display the current prompt of user.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        res = generate_response(prompt)

        # Store and display the current prompt of the bot.
        with st.chat_message("assistant"):
            response = st.markdown(res)
        st.session_state.messages.append({"role": "assistant", "content": res})
