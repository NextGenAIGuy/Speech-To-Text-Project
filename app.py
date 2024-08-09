import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from main import process_audio
from feedback_generation import ConversationReviewer

img_path = "OIP.jpg"

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return os.path.join("uploaded_files", uploaded_file.name)
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

def get_conversation(df):
    conversation = ""
    for index, row in df.iterrows():
        conversation += f"{row['speaker']}: {row['text']} "
    return conversation

st.title("Speech To Text Analysis")

# Display the image below the title
st.image(img_path, caption="Speech To Text Analysis", use_column_width=True)

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an option", ("Upload an audio file", "Use default audio"))

def display_data(df):
    # Display the dataframe with specified columns
    st.write("### Speech to Text Results with Speaker Identification")
    st.dataframe(df[['start', 'end', 'text', 'speaker']])

    # Check if sentiment_category column is present
    if 'sentiment_category' not in df.columns:
        st.error("Column 'sentiment_category' not found in the data.")
        return

    st.write("### Sentiment Category by Speaker")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x='speaker', hue='sentiment_category', ax=ax)
    st.pyplot(fig)

    # Analyze conversation
    conversation_reviewer = ConversationReviewer()
    conversation = get_conversation(df)
    review_output = conversation_reviewer.review_conversation(conversation)

    st.write("### Conversation Review")
    st.write(review_output)

if option == "Upload an audio file":
    uploaded_file = st.sidebar.file_uploader("Choose an audio file", type=["wav", "mp3"])
    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        if file_path:
            st.sidebar.success("File uploaded successfully!")
            df = process_audio(file_path)
            display_data(df)
elif option == "Use default audio":
    default_audio_path = "audio_file/combined_audio.wav"
    df = process_audio(default_audio_path)
    display_data(df)
