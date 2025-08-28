# Automatic Social Media Comment Generator

This project uses a pre-trained language model to generate engaging comments for social media posts, served via a modern API.

## Architecture

This project follows a decoupled frontend-backend architecture:

-   **Backend API:** A robust backend built with **FastAPI** that exposes an endpoint for comment generation. It handles the interaction with the AI model.
-   **Frontend UI:** A simple and intuitive interface built with **Streamlit** that consumes the backend API to provide a user-friendly experience.

## Features

-   Generates multiple automatic comment options based on a post's text.
-   Allows the user to choose the desired tone (e.g., professional, casual, motivational).
-   Clear separation between the AI logic (API) and the user interface.

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

This application requires running two services in separate terminals.

1.  **Run the Backend API:**
    Open a terminal and run the Uvicorn server:
    ```bash
    uvicorn src.api:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

2.  **Run the Frontend Application:**
    Open a second terminal and run the Streamlit application:
    ```bash
    streamlit run src/main.py
    ```
    You can now open your browser and interact with the UI, which will communicate with your local API.

## Built With

-   [FastAPI](https://fastapi.tiangolo.com/)
-   [Streamlit](https://streamlit.io/)
-   [Hugging Face Transformers](https://huggingface.co/transformers/)
-   [PyTorch](https://pytorch.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
