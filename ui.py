import torch
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AdvitChatBot-llama", layout="centered")

st.title("AdvitChatBot-llama")

@st.cache_resource
def load_model():
    model_id = "meta-llama/Llama-3.2-1B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    return pipe

pipe = load_model()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a professional chatbot who always responds in helpful and responsive manner!"
        }
    ]

# Display chat history (skip system message)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            outputs = pipe(
                st.session_state.messages,
                max_new_tokens=256,
            )

            reply = outputs[0]["generated_text"][-1]["content"]
            st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )