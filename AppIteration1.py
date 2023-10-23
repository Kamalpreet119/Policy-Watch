import os 
import streamlit as st 
from langchain.llms import OpenAI 
from ApiKey import apikey 

os.environ["OPENAI_API_KEY"]=apikey
st.title("🦜️🔗 Privacy Policy Flagger")
mainprompt=st.text_input("Paste the Text of the Privacy Policy Document here-")

llm1=OpenAI(temperature=0.2)
llm2=OpenAI(temperature=0.2)

try:
    if(mainprompt):
        prompt1="Summarize the text of a Privacy Policy within five to ten lines-"+mainprompt
        response1=llm1(prompt1)
        st.subheader("Summary of the Privacy Policy of the Company-")
        st.write(response1)

        prompt2="Tell me all the lines that are normally not present in a Privacy Policy-"+mainprompt
        response2=llm2(prompt2)
        st.subheader("AbNormal Points in the Privacy Policy-")
        st.write(response2)
except:
    st.write("Current API Quota exceeded")