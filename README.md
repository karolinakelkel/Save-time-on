# Save-time-on

This project provides a web application to summarize YouTube videos into text using OpenAI's GPT models. The application downloads audio from YouTube videos, converts it to WAV format, and generates a text summary.

## Features

- Download audio from YouTube videos
- Convert audio to WAV format
- Generate text summary using OpenAI's GPT models

## Requirements

- Python 3.6 or higher
- `fastapi`
- `ffmpeg` (for audio conversion)
- `openai`
- `psycopg2-binary`
- `pydantic`
- `uvicorn`
- `yt-dlp`

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/karolinakelkel/Save-time-on.git
cd your-repo-name
```

### 2. Create and activate a virtual environment
#### On macOS and Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the required Python libraries
```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg

#### On macOS (using Homebrew)
```bash
brew install ffmpeg
```

#### On Windows
1. Download ffmpeg from the official website: [ffmpeg.org/download.html]()
2. Extract the downloaded archive to a convenient location, e.g., C:\ffmpeg.
3. Add the bin directory to your system's PATH:
	- Press Win+R, type sysdm.cpl, and press Enter.
	- Go to the "Advanced" tab and click "Environment Variables".
	- In the "System variables" section, find the Path variable and click "Edit".
	- Click "New" and add the path to the bin directory, e.g., C:\ffmpeg\bin.
	- Click "OK" to save the changes.

### 5. Set up OpenAI API Key

Sign up at OpenAI to get your API key. Then, set up the API key in your environment variables:

#### On macOS and Linux
Add the following line to your ~/.bash_profile or ~/.zshrc file:
```bash
export OPENAI_API_KEY='your-openai-api-key'
```
Reload the profile:
```bash
source ~/.bash_profile  # or source ~/.zshrc
```

#### On Windows
Add a new environment variable named OPENAI_API_KEY with your API key as the value.

## Usage

### Running the Web Application

To start the web application, run the following command:
```bash
uvicorn main:app --reload
```

### Accessing the Application
Open your web browser and go to http://127.0.0.1:8000 to access the application.

### API Endpoints
POST /summarize: Accepts a JSON payload with a YouTube video URL and returns a text summary of the video.

## Notes

Ensure ffmpeg is installed and accessible in your system's PATH.

## License

