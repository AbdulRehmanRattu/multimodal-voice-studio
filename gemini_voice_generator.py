"""
Multimodal Voice Studio - Gemini Native Audio Generator
Generates voiceovers using Gemini 2.5's native audio modality with custom PCM-to-MP3 processing.
"""

import io
import os
import wave
from google import genai
from google.genai import types
from pydub import AudioSegment
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

def generate_reel_audio(
    reel_number,
    filename,
    voice_name,
    text_script,
    acting_instruction
):
    """
    Generates a single Reel's audio with specific acting direction.
    """
    try:
        print(f"\n🎬 STARTING REEL {reel_number}: {filename}")
        print(f"   👤 Voice: {voice_name}")
        print(f"   🎭 Direction: {acting_instruction}")
        
        if not API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not set. Please set the GEMINI_API_KEY environment variable "
                "or specify it in a .env file."
            )
            
        client = genai.Client(api_key=API_KEY)
        
        # 1. Create the "Director Prompt"
        # We wrap the script in instructions so the AI knows HOW to act.
        full_prompt = (
            f"Generate audio for the following text. "
            f"Style instruction: {acting_instruction} "
            f"Do not read the style instruction out loud. "
            f"Text to read: \n\n{text_script}"
        )

        # 2. Configure Voice
        speech_config = types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=voice_name
                )
            )
        )

        # 3. Request Audio (Gemini 2.5 TTS Model)
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=speech_config
            )
        )

        # 4. Process Raw PCM Audio
        if response.candidates and response.candidates[0].content.parts:
            part = response.candidates[0].content.parts[0]
            
            if part.inline_data:
                raw_audio_bytes = part.inline_data.data
                
                # --- FIX: RAW PCM HEADER WRAP ---
                # Gemini 2.5 TTS output is 24kHz, Mono, 16-bit PCM
                wav_io = io.BytesIO()
                with wave.open(wav_io, "wb") as wav_file:
                    wav_file.setnchannels(1)       # Mono
                    wav_file.setsampwidth(2)       # 16-bit
                    wav_file.setframerate(24000)   # 24kHz Sample Rate
                    wav_file.writeframes(raw_audio_bytes)
                
                wav_io.seek(0) # Reset pointer

                # --- CONVERT TO MP3 ---
                audio_segment = AudioSegment.from_wav(wav_io)
                
                # Ensure .mp3 extension
                if not filename.endswith(".mp3"):
                    filename += ".mp3"
                    
                audio_segment.export(filename, format="mp3", bitrate="192k")
                
                print(f"✅ DONE! Saved: {filename}")
                return True
            else:
                print("❌ Error: API returned no audio data.")
        else:
            print("❌ Error: No candidates returned.")
            print(response)

    except Exception as e:
        print(f"❌ FATAL ERROR on Reel {reel_number}:\n{e}")
    
    return False


if __name__ == "__main__":
    print("="*60)
    print("🚀 MULTIMODAL VOICE STUDIO - GEMINI AUDIO PRODUCTION")
    print("="*60)

    # 🎬 REEL 1: The Physical AI Revolution
    reel1_script = (
        "Picture this: Your manufacturing line encounters an unexpected problem. "
        "A traditional robot stops and waits for reprogramming. Meanwhile, a Physical AI "
        "system understands the situation, adapts its approach, and continues operating seamlessly. "
        "Traditional robots follow scripts. Physical AI thinks, learns, and evolves. They don't just "
        "execute commands - they reason through physics. They don't just repeat motions - they master "
        "environments. NVIDIA CEO Jensen Huang called this 'the next big thing for AI' at CES 2025. "
        "The question isn't whether Physical AI will transform manufacturing. It's whether you'll "
        "be the one leading that transformation or watching from the factory floor."
    )
    
    generate_reel_audio(
        reel_number=1,
        filename="reel1_physical_ai.mp3",
        voice_name="Charon",
        acting_instruction="Deep, dramatic, and intense movie trailer voice. Slow down for emphasis on the big words. Pause slightly after saying 'Picture this'.",
        text_script=reel1_script
    )

    # 🎬 REEL 2: Governance & Compliance
    reel2_script = (
        "While competitors fear AI regulation, leaders see opportunity. With EU AI Act in effect "
        "and U.S. states enacting 100+ AI laws, governance isn't a barrier – it's your moat. 83% of "
        "organizations use AI daily, but only 7% have proper governance. This gap is your advantage. "
        "Governed AI systems operate faster because decisions are pre-approved. They scale easier "
        "because frameworks are established. They innovate confidently because risks are managed. "
        "While others pause for compliance reviews, you accelerate. While they retrofit governance, "
        "you design it in. While they worry about regulations, you exceed them. AI governance isn't "
        "about following rules – it's about writing them. The future belongs to businesses that don't "
        "just move fast, but move smart."
    )

    generate_reel_audio(
        reel_number=2,
        filename="reel2_governance.mp3",
        voice_name="Kore",
        acting_instruction="Confident, professional, and reassuring. Speak clearly and intelligently, like a high-end business consultant giving advice to a CEO. Emphasize the word 'advantage'.",
        text_script=reel2_script
    )

    # 🎬 REEL 3: Industry Disruption
    reel3_script = (
        "Healthcare AI now outperforms human diagnosis with 95% accuracy versus 65% human rate, "
        "saving over $1.2 million annually per facility. Manufacturing deploys Physical AI 40% faster "
        "using digital twin simulations, achieving 25% efficiency gains. Finance prevents fraud in "
        "microseconds while humans take hours, protecting millions daily. Retail powers 95% of "
        "customer interactions through AI agents, boosting satisfaction and sales simultaneously. "
        "Supply chains optimize themselves in real-time, eliminating bottlenecks across continents. "
        "This isn't incremental improvement – this is industry redefinition. Every sector, every "
        "workflow, every competitive advantage now runs on intelligence. The companies dominating "
        "2026 aren't just using industry-standard AI. They're creating industry-defining AI. "
        "The disruption is here. The question is: Are you the disruptor or the disrupted?"
    )

    generate_reel_audio(
        reel_number=3,
        filename="reel3_disruption.mp3",
        voice_name="Puck",
        acting_instruction="Fast-paced, energetic, and exciting. Speak like a tech news anchor breaking a massive story. Keep the momentum high. Ensure the numbers (95%, 40%) are punchy and clear.",
        text_script=reel3_script
    )

    # 🎬 REEL 4: Your AI Future (Confidence Transformation)
    reel4_script = (
        "Before AI Governance: Your team hesitates to deploy AI due to regulatory uncertainty. "
        "Innovation stalls while legal reviews every decision. Competitors move faster because they "
        "ignore compliance risks. Your AI potential remains locked behind procedural barriers. "
        "After AI Governance: Your team deploys AI confidently with pre-approved frameworks. "
        "Innovation accelerates within established boundaries. Competitors struggle with retrofit "
        "compliance while you're already scaling. Your AI advantage compounds daily through systematic "
        "intelligence deployment. This isn't just about risk management – it's about unlocking velocity. "
        "Your governance doesn't slow you down, it speeds you up. Your compliance doesn't constrain you, "
        "it enables you. Your frameworks don't limit innovation, they amplify it. The confidence "
        "transformation isn't gradual. It's not about checking compliance boxes. It's revolutionary certainty. "
        "And it starts with choosing governance as your competitive weapon."
    )

    generate_reel_audio(
        reel_number=4,
        filename="reel4_future.mp3",
        voice_name="Aoede",
        acting_instruction="Soft, elegant, and inspiring. Start gently and build up emotion and confidence towards the end. Make it sound like a hopeful vision of the future. Dramatic pause before 'It's revolutionary certainty'.",
        text_script=reel4_script
    )

    print("\n" + "="*60)
    print("✨ ALL PRODUCTION COMPLETE. FILES READY IN FOLDER.")
    print("="*60)
