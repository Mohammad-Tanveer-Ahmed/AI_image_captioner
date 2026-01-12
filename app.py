import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

st.set_page_config(page_title="AI Image Captioner", page_icon="🧠")

st.markdown("<h1 style='text-align:center;'>🧠 AI Image Captioner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Upload an image to generate a caption</p>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

uploaded_file = st.file_uploader("➕ Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, use_container_width=True)

    with st.spinner("Generating caption..."):
        inputs = processor(image, return_tensors="pt")
        output = model.generate(**inputs, max_length=50)
        caption = processor.decode(output[0], skip_special_tokens=True)

    st.markdown("### ✨ Generated Caption")
    st.success(caption)
    st.code(caption)
