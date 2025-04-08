# KUKU-FM-REPO
# 🎙️ Script-to-Voice: AI-Powered Script to Video Pipeline

![Tech Stack](https://img.shields.io/badge/Powered%20By-NLP%20%7C%20WaveNet%20%7C%20DALL·E%20%7C%20FFmpeg-blue)
![License](https://img.shields.io/github/license/team-kirmada/script-to-voice)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-green)

A fully automated end-to-end pipeline that converts raw scripts or podcast transcripts into emotionally expressive, subtitle-synced videos with AI-generated visuals.

---

## 🔍 Overview

`Script-to-Voice` is designed to streamline content creation by converting textual scripts into full multimedia videos. The pipeline leverages:

- **NLP** for emotion detection
- **Google WaveNet** for realistic voice synthesis
- **OpenAI’s DALL·E** for image generation
- **FFmpeg** for video assembly

### 🎯 Key Features

- 🎭 **Emotion-Aware Voice Modulation**
- 🧠 **Transformer-Based Emotion Detection**
- 🎨 **Scene Generation with AI (DALL·E)**
- 🗣️ **Natural SSML-based Speech Synthesis**
- 🎞️ **Subtitle Embedding and Video Rendering**
- ☁️ **Highly Scalable Cloud-Based Architecture**

---

## ⚙️ Architecture

```mermaid
graph LR
A[Input Script] --> B[Preprocessing & Tokenization]
B --> C[Emotion Detection (BERT)]
C --> D[Voice Synthesis (WaveNet)]
C --> E[Prompt Extraction for Visuals]
E --> F[Image Generation (DALL·E)]
D --> G[Audio Output]
F --> H[Visual Scenes]
G --> I[Subtitle Generation]
G --> J[Video Assembly (FFmpeg)]
H --> J
I --> J
J --> K[Final Video Output]
