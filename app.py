# Code Generator ---> 

# Prompt / Text 

import streamlit as st
import requests

key = st.secrets["OPENROUTER_API_KEY"]


st.title("Code Generator")

prompt = st.text_area("Enter Your Prompt")
language = st.selectbox("Select Language" , ["Python","Java","C","C++","JS"])

if st.button("Generate"):
    if prompt:
        with st.spinner("Generation Code....."):
                    url = 'https://openrouter.ai/api/v1/chat/completions'
                    headers = {
                        "Authorization":f"Bearer {key}",
                        "Content-Type":"application/json"
                    }
                    body={
                        "model": "openai/gpt-4o-mini",
                        "messages": [
                            {
                                "role": "user",
                                "content": f"Generate beginner-friendly Code Language:{language} , Requirement:{prompt} "
                            }
                        ]
                    }
        
                    try:
                        response = requests.post(url,headers=headers,json=body,timeout=60)
                        response.raise_for_status()

                        data = response.json()

                        generated_code = (
                        data["choices"][0]["message"]["content"]
                )

                        st.success("Code Generated Successfully!")

                        st.code(generated_code, language=language.lower())

                    except requests.exceptions.RequestException as e:
                        st.error(f"API Error: {e}")

                    except (KeyError, IndexError, ValueError):
                        st.error("Invalid response received from API.")
