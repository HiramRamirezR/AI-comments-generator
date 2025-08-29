import requests
import streamlit as st
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
            # Set the URL for the local API
            api_url = "http://127.0.0.1:8000/generate-comment"

            # Data to send to the API
            payload = {
                "text": post_text,
                "tone": tone
            }

            try:
                # Send a POST request to the API
                response = requests.post(api_url, json=payload)

                # If the API answer with a 200 code
                if response.status_code == 200:
                    comment_data = response.json()
                    comments_list = comment_data.get("comments")

                    if comments_list:
                        generated_comment = comments_list[0]
                    else:
                        generated_comment = "No comments generated."


                    # Show result
                    st.success("Generated Comment:")
                    st.write(generated_comment)

                else:
                    # Shows an error in case of API failure
                    st.error(f"Error from API: {response.status_code} - {response.text}")

            except requests.exceptions.RequestException as e:
                # Shows an error if you cannot connect to the API
                st.error(f"Error connecting to the API: {e}")
