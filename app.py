import streamlit as st
import os
import time
import base64
import urllib.parse
from io import BytesIO
import PyPDF2

# Set Page Config
st.set_page_config(page_title="Text-to-Speech", layout="wide")

# Custom CSS for Styling & Center Alignment
def set_background():
    background_image_url = "https://images.unsplash.com/photo-1510070009289-b5bc34383727"
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 30px;
            border-radius: 10px;
        }}
        .stButton>button {{
            background-color: #ff8c00 !important;
            color: white !important;
            border-radius: 10px !important;
            font-size: 18px !important;
            width: 100%;
        }}
        .wave-animation {{
            width: 150px;
            height: 20px;
            background: linear-gradient(90deg, #ff8c00, #ff5733);
            animation: wave 1s infinite alternate;
            margin: auto;
        }}
        @keyframes wave {{
            0% {{ transform: scaleX(1); }}
            100% {{ transform: scaleX(1.2); }}
        }}
        </style>
        <div class="container">
        """,
        unsafe_allow_html=True
    )

set_background()

st.markdown("<h1 style='text-align: center;'>🎤 Text-to-Speech Audio Generator 🎵</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Upload a text/PDF file or choose from pre-uploaded stories.</p>", unsafe_allow_html=True)

# ✅ Pre-uploaded stories
pre_uploaded_stories = {
    "The Lion and the Mouse": "stories/lion_mouse.txt",
    "The Tortoise and the Hare": "stories/tortoise_hare.txt",
    "The Boy Who Cried Wolf": "stories/boy_wolf.txt"
}

# ✅ User options: Upload file OR select a pre-uploaded story
option = st.radio("📌 Choose Input Method", ["📂 Upload a Text/PDF File", "📖 Select a Pre-Uploaded Story"], index=0, horizontal=True)

# Global text variable
text = None

if option == "📂 Upload a Text/PDF File":
    uploaded_file = st.file_uploader("📤 Upload a Text or PDF File", type=["txt", "pdf"])
    
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension == "txt":
            text = uploaded_file.read().decode("utf-8")
        
        elif file_extension == "pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

elif option == "📖 Select a Pre-Uploaded Story":
    selected_story = st.selectbox("📚 Choose a Story", list(pre_uploaded_stories.keys()))
    story_path = pre_uploaded_stories[selected_story]
    with open(story_path, "r", encoding="utf-8") as f:
        text = f.read()

# Show preview only if text is available
if text:
    st.markdown("<h3 style='text-align: center;'>📄 Story Preview</h3>", unsafe_allow_html=True)
    st.text_area("Text Content", text, height=200)

    # ✅ Select Voice Gender
    voice = st.selectbox("🎤 Choose Voice Gender", ["Male", "Female"])

    # ✅ Button to trigger processing
    if st.button("🚀 Process Text & Generate Audio"):
        with st.spinner("🔄 Processing your file... Please wait."):
            time.sleep(2)  # Simulating delay
        
        # ✅ Simulated Audio Output (Replace this with real TTS)
        audio_content = b"FAKE_MP3_DATA"  # Replace with actual audio bytes
        audio_io = BytesIO(audio_content)

        # ✅ Show waveform animation
        st.markdown("<h3 style='text-align: center;'>🎵 Waveform Visualization</h3>", unsafe_allow_html=True)
        st.markdown('<div class="wave-animation"></div>', unsafe_allow_html=True)

        # ✅ Show audio player
        st.success("✅ Audio Processing Complete!")
        st.markdown("<h3 style='text-align: center;'>🎧 Generated Audio</h3>", unsafe_allow_html=True)
        st.audio(audio_io, format="audio/mp3")

        # ✅ Download button
        st.download_button(label="⬇️ Download Audio", data=audio_io, file_name="generated_audio.mp3", mime="audio/mp3")

        # ✅ Generate shareable link (Simulated)
        encoded_audio = base64.b64encode(audio_content).decode()
        share_link = f"data:audio/mp3;base64,{encoded_audio}"

        st.markdown("<h3 style='text-align: center;'>📢 Share Audio</h3>", unsafe_allow_html=True)
        
        # WhatsApp Share Button
        whatsapp_link = f"https://api.whatsapp.com/send?text={urllib.parse.quote('Check out this audio! ' + share_link)}"
        st.markdown(f"<p style='text-align: center;'><a href='{whatsapp_link}' target='_blank'>📲 Share on WhatsApp</a></p>", unsafe_allow_html=True)

        # Telegram Share Button
        telegram_link = f"https://t.me/share/url?url={urllib.parse.quote(share_link)}&text={urllib.parse.quote('Check out this audio!')}"
        st.markdown(f"<p style='text-align: center;'><a href='{telegram_link}' target='_blank'>📩 Share on Telegram</a></p>", unsafe_allow_html=True)

        # Email Share Button
        email_link = f"mailto:?subject=Check out this Audio&body={urllib.parse.quote('Listen to this audio: ' + share_link)}"
        st.markdown(f"<p style='text-align: center;'><a href='{email_link}' target='_blank'>📧 Share via Email</a></p>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:14px;'>Developed with ❤️ using Streamlit</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
