# app.py

import streamlit as st
import time
from utils.text_formatter import format_lyrics
from backend_inference import generate_music

# Page Config
st.set_page_config(page_title="AI Quote-to-Song", page_icon="🎵", layout="centered")

st.title("🎵 Quote-to-Song Generator")
st.write("Turn your favorite quote or short poem into a high-quality track in under a minute.")

# User Inputs
user_text = st.text_area("Enter your quote or poem:", height=150, placeholder="The night is darkest just before the dawn...")

genre_options = [
    "Lo-Fi Hip Hop", 
    "80s Synthwave", 
    "Acoustic Indie Folk", 
    "Epic Cinematic", 
    "Upbeat Pop"
]
selected_genre = st.selectbox("Choose a background music style:", genre_options)

# Generate Button
if st.button("Generate Song 🎧"):
    if not user_text.strip():
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Warming up the AI and generating your song... (this may take a minute)"):
            
            # Step 1: Format the text
            formatted_lyrics = format_lyrics(user_text)
            
            # Step 2: Generate the music
            # In a production app, you might add a unique timestamp to the filename 
            # so multiple users don't overwrite the same file.
            output_file = generate_music(formatted_lyrics, selected_genre)
            
            # Step 3: Display the result
            if output_file:
                st.success("Your song is ready!")
                
                # Show the formatted lyrics to the user
                with st.expander("See how the AI read your lyrics"):
                    st.text(formatted_lyrics)
                
                # Play the audio
                st.audio(output_file, format="audio/wav")
            else:
                st.error("Something went wrong during generation. Check the server logs.")
