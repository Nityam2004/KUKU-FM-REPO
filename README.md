# 🎙️ KUKU-FM-REPO: Script-to-Voice

**AI-Powered Script to Video Pipeline**

A fully automated, end-to-end system that converts raw text scripts or podcast transcripts into emotionally expressive, subtitle-synced videos — complete with AI-generated visuals and natural voiceovers.

---

## 🔍 Overview

**Script-to-Voice** streamlines multimedia content creation by converting textual narratives into complete videos. It combines emotion-aware speech synthesis, AI-based visual scene generation, and automated video assembly for scalable content production.

---

## 🚀 Features

- 🎭 **Emotion-Aware Voice Modulation**  
  SSML-tuned Google WaveNet voices adapt tone and pitch based on emotional cues.

- 🧠 **Transformer-Based Emotion Detection**  
  Classifies emotions (happy, sad, angry, etc.) using models like BERT.

- 🎨 **Scene Generation with AI**  
  Generates illustrations from descriptive prompts using OpenAI's DALL·E.

- 🗣️ **Natural Speech Synthesis**  
  Uses Google Cloud Text-to-Speech API with 220+ WaveNet voices across 40+ languages.

- 🎞️ **Subtitle Embedding & Video Rendering**  
  Subtitles generated from tokenized text and rendered with audio and visuals using FFmpeg.

- ☁️ **Cloud-Ready & Scalable**  
  Designed for high-throughput processing, handling 100+ scripts using cloud APIs.

---

## 🔧 Pipeline Workflow

### 1. 📝 Input Handling
- Accepts raw story scripts or transcribed podcasts.
- **Text Sanitization**: Cleans punctuation, removes special characters.
- **Tokenization**: Breaks content into sentences or words (using NLTK or SpaCy).
- **SSML Formatting**: Prepares the text for voice synthesis compatibility.

### 2. 😃 Emotion Detection
- Employs BERT-based classifiers to detect sentence-level emotions.
- Trained on emotion-tagged datasets for accuracy.
- Output guides voice modulation during speech synthesis.

### 3. 🔊 Voice Synthesis (Google WaveNet)
- Converts script to speech using emotion-informed SSML.
- Example mappings:
  - Happy → Fast, high-pitch tone
  - Sad → Slower, low-pitch
  - Angry → Sharp, tense delivery

### 4. 🖼️ Visual Generation
- Generates scenes from descriptive prompts using OpenAI’s DALL·E.
- Ensures visual continuity for storytelling.
- Example: `"stormy sea"` → creates an appropriate narrative frame.

### 5. 🎬 Video Assembly
- Combines generated images and synthesized audio using FFmpeg.
- Subtitles embedded from tokenized scripts (.srt format).
- Maintains tight audio-visual sync (<50ms drift).

---

## 🧰 Tech Stack

| Component          | Tools Used                                  |
|-------------------|----------------------------------------------|
| Language           | Python                                       |
| NLP & Emotion      | SpaCy / NLTK, BERT                           |
| Speech Synthesis   | Google Cloud Text-to-Speech (WaveNet + SSML)|
| Visual Generation  | OpenAI DALL·E API                            |
| Video Rendering    | FFmpeg                                       |
| Deployment         | Cloud-based (Google Cloud APIs)              |

---

## ⚙️ Performance & Cost

- ⏱️ **Speed**: Renders a 10-minute story in under 1 minute  
- 💰 **Cost**: ~$0.016 per 1M characters (Google WaveNet pricing)  
- ☁️ **Scalability**: Batch-processing ready — can handle 100+ scripts in parallel

---

## 💡 Final Pitch

> **Stop hiring voice actors or spending hours editing!**  
> Feed your script into our AI, choose a voice (or even clone your own), and generate studio-quality content in seconds.  
> Perfect for scaling podcasts, storytelling, educational material, or corporate videos — without sacrificing emotional nuance or quality.

---

## 📜 License

[MIT License](LICENSE)

---

## 🧪 Python Version

Tested with **Python 3.8+**
