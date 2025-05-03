# Save-time-on

**Save-time-on** is a command-line tool for summarising YouTube videos using OpenAI's GPT models.  
It was created as a personal productivity project — designed for people who, like me, struggle to stay focused during long videos.

## Features

- Downloads audio from a YouTube video
- Transcribes speech to text using OpenAI Whisper
- Summarises the content using GPT-4
- Outputs the final summary in the terminal


## Tech Stack

- Python 3.12
- OpenAI Whisper (speech-to-text)
- OpenAI GPT-4 (summarisation)
- yt-dlp (audio extraction)
- Logging (custom logger)
- dotenv for environment config

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/karolinakelkel/Save-time-on.git
cd Save-time-on
```

### 2. Create and activate a virtual environment

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg

**macOS (Homebrew):**

```bash
brew install ffmpeg
```

**Windows:**

- Download from: https://ffmpeg.org/download.html
- Unzip and add the `bin/` folder to your system’s `PATH` variable

### 5. Set environment variables

Create a `.env` file in the root of the project with the following:

```env
OPENAI_API_KEY=your_openai_key_here
FFMPEG_PATH=/path/to/ffmpeg  # optional if ffmpeg is in your system PATH
```

## Usage

```bash
python main.py
```

Then paste a valid YouTube video link when prompted.

## Example Output

```
Enter YouTube video URL: https://www.youtube.com/watch?v=xyz...

Summary:
The speaker describes how he accidentally joined a pyramid scheme, learned emotional resilience, and invented a new method for boiling eggs — all in under ten minutes...
```

## Notes

- Only public videos are supported. Private/unlisted videos won’t work unless you pass cookies to `yt-dlp`.
- Extremely long videos may take significantly longer to process due to audio transcription time. Additionally, OpenAI models have token limits, which may result in truncated input or incomplete summaries for lengthy transcripts.
- Temporary `.wav` files are cleaned up automatically after transcription.

## License

MIT License

---

Created with focus and care by [Karolina Kelkel](https://github.com/karolinakelkel)
