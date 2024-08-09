# 🎙️ Speech-to-Text with Speaker Diarization and Sentiment Analysis 🎙️

 This project showcases a powerful Speech-to-Text system with advanced features like Speaker Diarization, Sentiment Analysis, and integration with Large Language Models (LLMs). We use **WhisperX** for precise transcription and speaker identification, **Vader** for sentiment analysis, and **Groq** for efficient LLM operations.

 ## 🛠️ Installation and Setup

 ### Step 1: Clone the Repository

 Clone this repository to your local machine:

 ```bash
 git clone [https://github.com/your-username/speech-to-text-project.git](https://github.com/NextGenAIGuy/Speech-To-Text-Project.git)
 cd Speech-To-Text-Project
 ```

 ### Step 2: Create a Conda Environment

 Create a new Conda environment with Python 3.10:

 ```bash
 conda create --name speech-to-text-env python=3.10
 conda activate speech-to-text-env
 ```

 ### Step 3: Install Dependencies

 Install the required Python packages using `pip`:

 ```bash
 pip install -r requirements.txt
 ```

 If you encounter any issues with the installation, you can install WhisperX directly:

 ```bash
 pip install whisperx
 ```

 ## 🚀 Usage

 With the environment set up and dependencies installed, you can run the project to transcribe audio, identify speakers, and perform sentiment analysis.

 ### Example Command

 ```bash
 python app.py
 ```

 This command will:
 - Transcribe the audio file using **WhisperX**.
 - Identify and diarize different speakers in the audio.
 - Perform sentiment analysis on the transcribed text using **Vader**.
 - Utilize **Groq** for handling large language models, if applicable.

 ## 🧩 Key Components

 - **WhisperX**: For Speech-to-Text and Speaker Diarization.
 - **Vader**: For Sentiment Analysis.
 - **Groq**: For efficient Large Language Model integration.
