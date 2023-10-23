import os
import streamlit as st
from langchain.llms import OpenAI
from ApiKey import apikey

os.environ["OPENAI_API_KEY"]=apikey
st.title("🦜️🔗 Privacy Policy Flagger")
mainprompt=st.text_input("Paste the Text of the Privacy Policy Document here-")

if(mainprompt and apikey):
    llm1=OpenAI(temperature=0.2)
    llm2=OpenAI(temperature=0.2)

    try:
        prompt1="Summarize the text of a Privacy Policy within five to ten lines-"+mainprompt
        response1=llm1(prompt1)
        st.subheader("Summary-")
        st.write(response1)

        prompt2="Tell me all the lines that are normally not present in a Privacy Policy-"+mainprompt
        response2=llm2(prompt2)
        st.subheader("Abnormal Points-")
        st.write(response2)
    except Exception as e:
        st.write(f"An error occurred- {str(e)}")
else:
    st.write("Please enter the Privacy Policy text and ensure that the API key is provided")