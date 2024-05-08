"""
Run: PYTHONPATH=. streamlit run src/app.py
"""
import logging

import streamlit as st
from streamlit.external.langchain import StreamlitCallbackHandler

from retriever import configure_retrieval_chain, MEMORY

logging.basicConfig(encoding="utf-8", level=logging.INFO)
LOGGER = logging.getLogger()

st.set_page_config(page_title="Golf Assistant", page_icon="⛳")
st.title("⛳ Golf Assistant")

if st.sidebar.button("Clear message history"):
    MEMORY.chat_memory.clear()

avatars = {"human": "user", "ai": "assistant"}

if len(MEMORY.chat_memory.messages) == 0:
    st.chat_message("assistant").markdown("Ask me anything about Golf!")

for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

CONV_CHAIN = configure_retrieval_chain()

assistant = st.chat_message("assistant")
if user_query := st.chat_input(placeholder="Hello!"):
    st.chat_message("user").write(user_query)
    container = st.empty()
    stream_handler = StreamlitCallbackHandler(container)
    with st.chat_message("assistant"):
        params = {"question": user_query,'chat_history':MEMORY.chat_memory.messages}
        response = CONV_CHAIN.run(params, callbacks=[stream_handler])
        # Display the response from the chatbot
        if response:
            container.markdown(response)
