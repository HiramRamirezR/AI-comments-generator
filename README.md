# Automatic Social Media Comment Generator

This project is a simple web application that uses a pre-trained language model to generate engaging comments for social media posts.

## Features

-   Generates automatic comments with "engagement" (open questions, support, humor, etc.).
-   Allows you to choose the tone of the comment (e.g., professional, casual, motivational).
-   Simple and intuitive interface built with Streamlit.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://huggingface.co/spaces/hiram-labs/autocomment-generator
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the Streamlit application:
    ```bash
    streamlit run src/main.py
    ```
2.  Enter the text of the social media post.
3.  Select the desired tone for the comment.
4.  Click the "Generate Comment" button.
5.  The generated comment will be displayed on the screen.

## Built With

-   [Streamlit](https://streamlit.io/)
-   [Hugging Face Transformers](https://huggingface.co/transformers/)
-   [PyTorch](https://pytorch.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
