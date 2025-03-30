import streamlit as st  
import random  

# Data Lists  
genres = ["Fantasy", "Sci-Fi", "Mystery", "Horror", "Romance"]
themes = ["Betrayal", "Survival", "Discovery", "Redemption"]
characters = ["Detective", "Scientist", "Warrior", "Outcast"]

def generate_prompt(genre, theme, character):
    return f"In a {genre} world, a {character} must face {theme}."

# Streamlit UI  
st.title("Story Idea Generator")  
st.write("Select options below to generate a creative story prompt.")  

# User Input  
genre = st.selectbox("Choose a Genre", genres)  
theme = st.selectbox("Choose a Theme", themes)  
character = st.selectbox("Choose a Character", characters)  

if st.button("Generate Story Idea"):  
    st.write("**Your Story Prompt:**")  
    st.write(generate_prompt(genre, theme, character))
