
import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

chat_completion_input = st.text_input("Enter your message:")
if st.button("Generate Chat Completion"):
    chat_completion = client.chat_completion(
        messages=[
            {
                "role": "user",
                "content": chat_completion_input,
            }
        ],
        max_tokens=100)
    st.write(chat_completion)







# hf_client = InferenceApi(repo_id="gpt-2", token=os.environ['HF_KEY']) 

# generated_text = client.text_generation(prompt="Write a code for snake game")
# print(generated_text)

# response = hf_client(text="The definition of machine learning inference is")

# print(response)

# 'model': "HuggingFaceH4/zephyr-7b-beta"