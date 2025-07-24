#!/usr/bin/env python
# coding: utf-8

# In[5]:


import google.generativeai as genai
import gradio as gr

genai.configure(api_key="Your gemini api key")

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def get_health_recommendation(age, gender, symptoms):
    prompt = f"Patient age: {age}, gender: {gender}, symptoms: {symptoms}. Suggest likely disease, medicines, and doctor type."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=get_health_recommendation,
    inputs=[
        gr.Number(label="Age"),
        gr.Radio(["Male", "Female", "Other"], label="Gender"),
        gr.Textbox(label="Symptoms")
    ],
    outputs="text",
    title="Healthcare Recommender",
    description="Enter your details to get health advice."
)

iface.launch(share=True)


# In[ ]:




