"""
Multimodal Voice Studio - OpenAI Voice Generator
Provides full control over OpenAI's Text-to-Speech API with support for all 11 voices.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch OpenAI API Key
API_KEY = os.getenv("OPENAI_API_KEY")

def openai_text_to_speech(
    text, 
    output_filename="output.mp3", 
    voice="nova", 
    model="tts-1-hd",
    speed=1.0,
    response_format="mp3"
):
    """
    Convert text to speech using OpenAI's TTS API with full control
    
    Args:
        text (str): The text to convert to speech
        output_filename (str): Output filename (e.g., "output.mp3")
        voice (str): Voice name
        model (str): 'tts-1' (faster) or 'tts-1-hd' (higher quality)
        speed (float): Playback speed (0.25 to 4.0)
        response_format (str): Output format - 'mp3', 'opus', 'aac', 'flac', 'wav', 'pcm'
    """
    
    if not API_KEY:
        raise ValueError(
            "OPENAI_API_KEY not set. Please set the OPENAI_API_KEY environment variable "
            "or specify it in a .env file."
        )
        
    # Initialize OpenAI client
    client = OpenAI(api_key=API_KEY)
    
    print(f"🎙️ Generating speech with OpenAI TTS...")
    print(f"   👤 Voice: {voice}")
    print(f"   ⚙️ Model: {model}")
    print(f"   ⚡ Speed: {speed}x")
    print(f"   📁 Format: {response_format}")
    
    # Generate speech
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,
        speed=speed,
        response_format=response_format
    )
    
    # Ensure filename has correct extension
    if not output_filename.endswith(f'.{response_format}'):
        output_filename = output_filename.rsplit('.', 1)[0] + f'.{response_format}'
    
    # Save to file
    response.stream_to_file(output_filename)
    
    print(f"✅ Audio saved: {output_filename}")
    
    # Auto-play on Mac
    print(f"🔊 Playing audio...")
    os.system(f"afplay {output_filename}")
    
    return output_filename


# Example/Business script
business_text = (
    "Before AI: Your team spends hours on data entry. "
    "Customers wait days for responses. Decisions are based on gut feelings and outdated "
    "reports. Problems are discovered after they've already cost you money. "
    "After AI: Data processes itself. Customer questions get answered instantly with personalized "
    "solutions. Decisions are made with real-time intelligence and predictive insights. "
    "Problems are prevented before they happen. This isn't just automation - this is "
    "transformation. Your employees focus on strategy, not repetitive tasks. Your customers "
    "get experiences that exceed their expectations. Your business operates with the "
    "intelligence of the future, today. The transformation isn't gradual. It's not incremental. "
    "It's revolutionary. And it starts with a simple decision: Will you transform your business, "
    "or will you let your business be transformed by those who did?"
)


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🎯 OPENAI TTS VOICE ENGINE - 11 ACTIVE VOICES")
    print("=" * 70)
    print("\n🔴 FEMALE VOICES:")
    print("  nova    - Bright, energetic, professional ⭐ RECOMMENDED")
    print("  shimmer - Soft, gentle, warm")
    print("  coral   - Expressive female")
    print("  ballad  - Storytelling female")
    print()
    print("🟡 NEUTRAL/VERSATILE VOICES:")
    print("  alloy   - Balanced (can sound male/female)")
    print("  sage    - Neutral voice")
    print("  verse   - Versatile voice")
    print()
    print("🔵 MALE VOICES:")
    print("  echo    - Articulate, precise")
    print("  fable   - Warm, engaging, storytelling")
    print("  onyx    - Deep, authoritative")
    print("  ash     - Confident male")
    print()
    print("=" * 70)
    print()
    
    # Configure generation
    selected_voice = "nova"
    selected_model = "tts-1-hd"
    playback_speed = 0.9
    audio_format = "mp3"
    output_file = "ai_agents_pitch4.mp3"
    
    print("\n📝 CURRENT SETTINGS:")
    print(f"   Voice: {selected_voice}")
    print(f"   Model: {selected_model}")
    print(f"   Speed: {playback_speed}x")
    print(f"   Format: {audio_format}")
    print(f"   Output: {output_file}")
    print()
    
    # Generate the speech
    openai_text_to_speech(
        text=business_text,
        output_filename=output_file,
        voice=selected_voice,
        model=selected_model,
        speed=playback_speed,
        response_format=audio_format
    )
    
    print("\n✨ Done!")
