import streamlit as st
from generator import generate_comment
from utils import get_available_tones

# Set the page title
st.title("Automatic Social Media Comment Generator")

# Get the available tones
tones = get_available_tones()

# Create the UI elements
post_text = st.text_area("Enter the social media post text:")
tone = st.selectbox("Select the desired tone:", tones)
generate_button = st.button("Generate Comment")

# Handle the button click
if generate_button:
    # Make sure the user has entered some text
    if not post_text:
        st.warning("Please enter a post text to generate comments.")
    else:
        # Show a spinner while generating the comments
        with st.spinner("Generating comments..."):
            # Generate the comments
            comments = generate_comment(post_text, tone)

            # Display the comments
            st.success("Here are some comment options:")
            for i, comment in enumerate(comments):
                st.write(f"{i+1}. {comment}")
