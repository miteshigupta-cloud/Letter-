
import streamlit as st

st.set_page_config(page_title="💌 Cute Letter Generator", page_icon="💙")

st.title("💌 Cute Letter Generator")
st.write("Make a sweet personalized letter for someone special 💙")

name = st.text_input("Enter their name:")
reason = st.text_input("Why are you writing this letter (e.g., sorry, thank you, love)?")
things = st.text_input("Write one thing you really like about them:")

if st.button("Generate Letter 💌"):
    if name and reason and things:
        letter = f"""
        Dear {name},

        I just wanted to say {reason}.
        You mean so much to me, and one of the things I love about you is {things}.
        Thank you for being in my life 💙

        With love,  
        ~ Your Special Person 💌
        """
        st.success("Here's your cute letter 💙")
        st.text_area("💌 Your Letter", letter, height=200)

        st.download_button(
            label="📥 Download Letter as Text",
            data=letter,
            file_name="letter.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please fill all the fields before generating!")
