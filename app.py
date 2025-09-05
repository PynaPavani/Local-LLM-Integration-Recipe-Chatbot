import streamlit as st
import requests

st.title("🍳 Recipe Chatbot")
st.write("Enter ingredients and get a recipe suggestion!")

ingredients = st.text_input("Ingredients(comma separated)")

if st.button("Get Recipe"):
    if ingredients:
        response = requests.post("http://127.0.0.1:8000/chat", json={"ingredients": ingredients})
        if response.status_code == 200:
            recipe = response.json()["recipe"]
            st.success(f"🍲 Recipe Suggestion: {recipe}")
        else:
            st.error("Error fetching recipe. Try again!")
    else:
        st.warning("Please enter some ingredients.")
