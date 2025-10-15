# Voice Assistant

This is a Python-based voice assistant that can perform a variety of tasks based on voice commands.

## Features

*   **Plays Music:** Plays songs on YouTube.
*   **Tells Time and Date:** Provides the current time and date.
*   **Wikipedia Summaries:** Fetches and reads summaries from Wikipedia.
*   **Tells Jokes:** Tells jokes from a collection of programmer jokes.
*   **News Headlines:** Reads the latest news headlines.
*   **Weather Forecasts:** Provides weather information for a specified city.
*   **Sends Emails:** Sends emails to a pre-defined recipient.
*   **Opens Applications:** Opens applications on your computer.
*   **Answers Questions:** Answers general knowledge questions using a large language model.

## Technologies Used

*   **Python:** The core programming language.
*   **SpeechRecognition:** For recognizing voice commands.
*   **pyttsx3:** For text-to-speech conversion.
*   **pywhatkit:** For playing songs on YouTube.
*   **wikipedia:** For fetching information from Wikipedia.
*   **pyjokes:** For telling jokes.
*   **requests:** For making HTTP requests to news and weather APIs.
*   **google-generativeai:** For answering general knowledge questions.
*   **python-dotenv:** For managing environment variables.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Evans2028/Voice-Assistant.git
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**
    Create a `.env` file in the root of the project and add the following environment variables:

    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    NEWS_API_KEY="YOUR_NEWS_API_KEY"
    WEATHER_API_KEY="YOUR_WEATHER_API_KEY"
    SENDER_EMAIL="YOUR_EMAIL@gmail.com"
    EMAIL_PASSWORD="YOUR_EMAIL_PASSWORD"
    RECIPIENT_EMAIL="RECIPIENT_EMAIL@example.com"
    ```

## How to Run

To run the voice assistant, simply run the `main.py` file:

```bash
python main.py
```
