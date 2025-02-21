import streamlit as st
import numpy as np
# from keras.models import load_model
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# File paths
MODEL_PATH = "Model/keras_Model.h5"
LABELS_PATH = "Model/labels.txt"

# Load the trained Keras model
@st.cache_resource
def load_trained_model():
    return load_model(MODEL_PATH, compile=False)

model = load_trained_model()

# Load class labels dynamically from labels.txt
def load_labels():
    with open(LABELS_PATH, "r") as f:
        return [label.strip() for label in f.readlines()]

LABELS = load_labels()

# Streamlit UI
st.title("Blood Group Detection from Fingerprint")

uploaded_file = st.file_uploader("Upload a fingerprint image", type=["jpg", "png", "jpeg", "bmp"])

if uploaded_file:
    image_data = Image.open(uploaded_file).convert("RGB")
    st.image(image_data, caption="Uploaded Image", use_column_width=True)

    # Resize and preprocess image
    size = (224, 224)
    image_data = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)

    # Convert image to array and normalize
    image_array = np.asarray(image_data).astype(np.float32)
    normalized_image_array = (image_array / 127.5) - 1  # Match your script's normalization
    input_tensor = np.expand_dims(normalized_image_array, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(input_tensor)[0]  # Get first (only) sample output
    
    # Get the highest probability class
    predicted_index = np.argmax(prediction)
    predicted_label = LABELS[predicted_index]
    confidence_score = prediction[predicted_index]

    # Display all class probabilities
    st.subheader("Class Probabilities:")
    probs = {LABELS[i]: round(pred, 4) for i, pred in enumerate(prediction)}
    st.json(probs)  # Display in structured JSON format
    
    # # Display the final prediction
    # st.subheader("Predicted Class Index:")
    # st.code(predicted_index)

    # st.success(f"Predicted Blood Group: **{predicted_label}** (Confidence: {confidence_score:.2%})")
    clean_label = " ".join(predicted_label.split()[1:])  # Remove the index if present
    st.success(f"Predicted Blood Group: **{clean_label}** (Confidence: {confidence_score:.2%})")
