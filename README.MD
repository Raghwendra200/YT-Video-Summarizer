
# YouTube Video Transcript to Detailed Notes Converter 📹✨

Welcome to the **YouTube Video Transcript to Detailed Notes Converter**, a simple yet powerful tool that helps you convert YouTube video transcripts into summarized notes in seconds using **AI-powered technology**.

## Key Features
- **AI-Powered Summarization:** Leverage Google Gemini's generative model to summarize video transcripts.
- **Instant Results:** Get detailed notes quickly and easily, saving you time on summarizing lengthy YouTube videos.
- **Easy to Use:** Paste the YouTube URL, click a button, and receive summarized notes without any hassle.
- **YouTube Video Thumbnail:** The app displays the YouTube thumbnail of the entered video link for better visual context.

## How It Works
1. **Enter a YouTube Video URL**  
   Paste any YouTube video URL into the provided text box.
   
2. **Click "Generate Detailed Notes 📝"**  
   After pasting the link, click the button to generate the summary.

3. **Get AI-Powered Summarized Notes**  
   The app extracts the transcript of the video and generates a summarized version of the content using Google's **Gemini Pro** model.

## Installation

To run this app locally, follow the steps below.

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/YouTube-Transcript-Summarizer.git
cd YouTube-Transcript-Summarizer
```

### 2. Create a virtual environment:
For **Windows**:
```bash
python -m venv venv
```
For **Mac/Linux**:
```bash
python3 -m venv venv
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up API key:
- Sign up for **Google Gemini API** and get your **API Key**.
- Create a `.env` file in the root directory and add the following line:
  ```bash
  GOOGLE_API_KEY=your_api_key
  ```

### 5. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage
1. **Enter a YouTube video URL** in the input box.
2. **Click on the "Generate Detailed Notes 📝"** button to process the video.
3. The AI will extract the transcript and provide a summary of the video in **bullet points**.

## Technologies Used
- **Streamlit:** For building the web interface.
- **Google Gemini:** For AI-based text summarization.
- **YouTube Transcript API:** To extract transcripts from YouTube videos.
- **dotenv:** For managing environment variables.