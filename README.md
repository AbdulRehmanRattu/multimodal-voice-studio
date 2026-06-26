# Multimodal Voice Studio

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Gemini API](https://img.shields.io/badge/Gemini_2.5-Native_Audio-orange.svg)](https://ai.google.dev/)
[![OpenAI API](https://img.shields.io/badge/OpenAI_TTS-HD_Voices-green.svg)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

**Multimodal Voice Studio** is a professional Python-based audio generation suite designed to automate high-fidelity, expressive narration for short-form content like Instagram Reels, TikToks, and YouTube Shorts. 

By combining the power of **Google Gemini 2.5's native audio modality** and **OpenAI's high-definition TTS engine**, this tool allows you to convert plain text scripts into dynamic voiceovers guided by custom emotional acting instructions (e.g., *"Deep movie trailer voice"* or *"Energetic tech news anchor"*).

---

## Key Features

*   **Gemini 2.5 Native Multimodal Audio:** Utilizes Gemini's direct audio generation capabilities (`response_modalities=["AUDIO"]`) rather than standard text-to-speech, enabling nuanced tone, pauses, and expression.
*   **OpenAI TTS-HD Studio:** Full parameterized control over all 11 premium OpenAI voices (Nova, Shimmer, Coral, Ballad, Alloy, etc.) with configurable speeds (0.25x to 4.0x) and output formats.
*   **Custom Audio Engineering Pipeline:** Features a built-in PCM audio wrapping layer that structures raw 24kHz Mono 16-bit PCM output from Gemini into a valid WAV format and exports it to MP3 using `pydub`.
*   **Production-Ready Credential Safety:** Out-of-the-box support for `python-dotenv` to ensure your API keys are loaded securely from environment variables and never committed to code.

---

## Technical Highlights

### Solving the Raw PCM Wrapping Hurdle
Standard text-to-speech APIs output audio in standard compressed containers like MP3. However, Gemini 2.5's native multimodal audio endpoint returns a raw, headerless 24kHz Mono 16-bit PCM byte stream. 

This project solves this by programmatically building a WAV header structure before exporting the audio:

```python
wav_io = io.BytesIO()
with wave.open(wav_io, "wb") as wav_file:
    wav_file.setnchannels(1)       # Mono channel
    wav_file.setsampwidth(2)       # 16-bit sample width
    wav_file.setframerate(24000)   # 24kHz Sample Rate
    wav_file.writeframes(raw_audio_bytes)
```

---

## Directory Structure

```text
├── .env.example                # Template for your local environment configuration
├── .gitignore                  # Prevents committing API keys and generated media
├── requirements.txt            # Project python dependencies
├── gemini_voice_generator.py   # Voiceover generator powered by Gemini 2.5
└── openai_voice_generator.py   # Pitch and voiceover studio powered by OpenAI TTS-HD
```

---

## Getting Started

### 1. Prerequisites
Make sure you have Python 3.9 or higher installed. You will also need `ffmpeg` installed on your system to process MP3 conversions via `pydub`.

*   **macOS (via Homebrew):**
    ```bash
    brew install ffmpeg
    ```
*   **Windows (via Choco):**
    ```cmd
    choco install ffmpeg
    ```

### 2. Installation
Clone the repository and install the dependencies in a virtual environment:

```bash
# Clone the repository
git clone https://github.com/AbdulRehmanRattu/multimodal-voice-studio.git
cd multimodal-voice-studio

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory by copying the example template:

```bash
cp .env.example .env
```

Open the `.env` file and insert your API keys:
```env
GEMINI_API_KEY=your_actual_gemini_api_key
OPENAI_API_KEY=your_actual_openai_api_key
```

---

## Usage

### Generating Audio with Gemini 2.5
Run the script to generate content marketing voiceovers using custom voices and acting directions:
```bash
python gemini_voice_generator.py
```
This script will produce 4 distinct audio reels matching the scripts and tones specified inside the program.

### Generating Audio with OpenAI TTS
Run the OpenAI voice controller to generate highly realistic voice pitches:
```bash
python openai_voice_generator.py
```
Modify the configuration variables at the bottom of `openai_voice_generator.py` to change the voice, model quality, playback speed, or audio output format.

---

## Author & Contact

**Abdul Rehman Rattu**  
*Founder & AI Developer*  

If you are looking to build predictive AI models, business workflows, or custom generative pipelines, feel free to reach out.

*   **Email:** [rattu786.ar@gmail.com](mailto:rattu786.ar@gmail.com)
*   **LinkedIn:** [linkedin.com/in/abdul-rehman-rattu-395bba237](https://www.linkedin.com/in/abdul-rehman-rattu-395bba237)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
