import os #To set OPENAI API Key for our Environment
import streamlit as st #Application Framework to build web apps
from langchain.llms import OpenAI #Importing OpenAI Service
from ApiKey import apikey 

#Making the OpenAI Key Available
os.environ["OPENAI_API_KEY"]=apikey

#App framework
st.title("🦜️🔗 Privacy Policy Flagger")
mainprompt=st.text_input("Paste the Text of the Privacy Policy Document here-")# mainprompt is provided with a string to store

#Using our LLMs
#Creating llm Object
llm1=OpenAI(temperature=0.2)#temperature value decides how creative our Model will be
#Large values means more creative
# temperature-Number or null Optional Defaults to 1
# https://platform.openai.com/docs/api-reference/chat/create?lang=python
# What sampling temperature to use,between 0 and 2. 
# Higher values like 0.8 will make the output more random,while lower values like 
# 0.2 will make it more focused and deterministic

#Creating New Instance of our OpenAI service
llm2=OpenAI(temperature=0.2)

#Using Prompt to trigger our LLM-Showing Text on screen if there is a prompt
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
#We are actually tackling a specific topic,so It is not a User Directed Application
#But we can use Prompts and LangChain Modules to make our code User directed
