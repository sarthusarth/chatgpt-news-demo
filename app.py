import random
import streamlit as st
from datasets import load_dataset

st.title("Comparison between CNN and ChatGPT News Articles")

dataset = load_dataset('isarth/chatgpt-news-articles')

idx = random.randint(0,len(dataset['train']))
st.text(f'Article id: {dataset["train"][idx]["id"]}')
st.text_area('Highlights provide to ChatGPT',dataset['train'][idx]['highlights'],height=100)


col1, col2 = st.columns(2)
col1.text_area('CNN',dataset['train'][idx]['article'], height=600)
col2.text_area('ChatGPT',dataset['train'][idx]['chatgpt'], height=600)

if st.button('Show Another'):
	pass