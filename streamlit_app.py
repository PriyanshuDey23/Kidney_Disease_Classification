import streamlit as st
import base64
import requests
from PIL import Image
import io


# Page configuration
st.set_page_config(page_title="Kidney Disease Classification", layout="wide")

# Title
st.title("Kidney Disease Classification")

# Layout
col1, col2 = st.columns([1, 1])

# Upload Image Section
with col1:
    st.subheader("Upload an Image")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

# Prediction Section
with col2:
    st.subheader("Prediction Results")

    # Button to trigger prediction
    if st.button("Predict"):

        if uploaded_file is not None:
            # Convert the image to base64
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="JPEG")
            img_byte_arr = img_byte_arr.getvalue()
            base64_data = base64.b64encode(img_byte_arr).decode("utf-8")

            # Sending the base64 image data to your prediction API (Flask Backend)
            url = "http://localhost:8080/predict"  # Flask endpoint for prediction
            headers = {"Content-Type": "application/json"}
            payload = {"image": base64_data}

            # Make POST request to Flask backend
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                # Handle raw string response from the Flask backend
                prediction = response.text  # The response will be just the string, e.g., "The Chicken is having Coccidiosis"
                st.write(prediction)  # Display the result directly in Streamlit
            else:
                st.error(f"Error: {response.text}")
        else:
            st.warning("Please upload an image to predict.")