import streamlit as st
from dotenv import load_dotenv

load_dotenv()  ## Load all environment variables
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text 
and summarizing the entire video and providing the important summary in points 
within 250 words. Please provide the summary of the text given here: """

## Getting the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## Getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Page configuration
st.set_page_config(
    page_title="YouTube Transcript to Detailed Notes",
    page_icon="📹",
    layout="wide"
)

st.title("YouTube Video Transcript to Detailed Notes Converter 📹✨")
st.markdown(
    """
    **Welcome to the YouTube Transcript Summarizer!**  
    Paste your YouTube video URL below, and we’ll convert the video transcript into detailed, summarized notes in seconds!  
    🔹 **Easy to Use**  
    🔹 **Instant Results**  
    🔹 **AI-Powered Summarization**  
    """
)

# User Input for YouTube URL
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to get detailed notes
if st.button("Generate Detailed Notes 📝"):
    if youtube_link:
        try:
            transcript_text = extract_transcript_details(youtube_link)

            if transcript_text:
                summary = generate_gemini_content(transcript_text, prompt)
                st.markdown("## Detailed Notes:")
                st.write(summary)
            else:
                st.error("Sorry, we couldn't retrieve the transcript. Please check the video URL.")
        except Exception as e:
            st.error(f"Error occurred: {e}")
