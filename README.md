# AI Image Captioner

AI Image Captioner is a GenAI-based web application that automatically generates natural language descriptions for uploaded images using the BLIP (Bootstrapping Language-Image Pretraining) model.

## Project Objectives
- Generate accurate image captions
- Support JPG and PNG images
- Provide a fast and user-friendly interface

## Technology Stack
- Frontend: Streamlit
- Backend: Python
- Model: BLIP (Hugging Face)
- Libraries: Transformers, Torch, Pillow

## How It Works
1. User uploads an image
2. BLIP model analyzes the image
3. AI generates a descriptive caption

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
