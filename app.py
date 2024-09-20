%%writefile app.py
import streamlit as st
import torch
from torchvision import models, transforms
from PIL import Image
import torch.nn as nn
import time
import pandas as pd

# Load the trained model (architecture + weights)
@st.cache_resource
def load_model():
    model = models.resnet50(pretrained=False)  # Use the same model as trained
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)  # Assuming binary classification (genuine vs forged)

    model.load_state_dict(torch.load('forgery_detection_model.pth', map_location=torch.device('cpu')))
    model.eval()
    return model

# Define the image transformations (same as during training)
data_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Prediction function
def predict_image(image, model):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = data_transforms(image)

    if image.shape[0] != 3:
        st.error("Image has an unexpected number of channels.")
        return None, None

    image = image.unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        confidence = torch.softmax(output, dim=1).max().item() * 100
    return predicted.item(), confidence

# Streamlit app interface
st.set_page_config(page_title="Document Forgery Detection", layout="wide")

# Display the title and a brief description
st.title("🔍 Document Forgery Detection")
st.markdown("**Upload images of documents and find out if they are _genuine_ or _forged_ using our advanced detection model.**")

# Upload images
uploaded_files = st.file_uploader("Upload one or more document images:", type=["jpg", "png", "jpeg", "tif", "tiff"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"🖼️ You've uploaded {len(uploaded_files)} document(s).")

    model = load_model()  # Load model only when files are uploaded

    # Create tabs for better navigation
    tab1, tab2, tab3 = st.tabs(["📝 Predictions", "📊 Download Results", "📖 Documentation"])

    # Tab 1: Predictions
    with tab1:
        st.subheader("📋 Results")
        y_true = []
        y_pred = []
        file_names = []
        results = []

        cols = st.columns(3)  # Display images in 3-column layout

        # Process and predict for each uploaded file
        for i, uploaded_file in enumerate(uploaded_files):
            image = Image.open(uploaded_file)
            with cols[i % 3]:
                st.image(image, caption=f"{uploaded_file.name}", use_column_width=True)

                label, confidence = predict_image(image, model)

                if label is not None:
                    y_true.append(label)
                    y_pred.append(label)
                    file_names.append(uploaded_file.name)
                    result_label = "Genuine" if label == 0 else "Forged"

                    # Display result with color coding
                    st.markdown(f"<span style='color: {'green' if label == 0 else 'red'}'>**{result_label}** - Confidence: {confidence:.2f}%</span>", unsafe_allow_html=True)

                    # Store the result for later
                    results.append({
                        "File Name": uploaded_file.name,
                        "Result": result_label,
                        "Confidence": f"{confidence:.2f}%",
                    })
                    time.sleep(0.5)  # Simulate processing time for better UX

    # Tab 2: Download Results
    with tab2:
        st.subheader("📊 Download Prediction Report")
        if results:
            report_df = pd.DataFrame(results)
            st.write(report_df)

            # Allow users to download the CSV
            csv = report_df.to_csv(index=False)
            st.download_button("Download Prediction Report", csv, "prediction_report.csv", "text/csv", key="download-report")
        else:
            st.info("Please make predictions first in the 'Predictions' tab.")

    # Tab 3: Documentation
    with tab3:
        st.subheader("📖 How the Detection Works")
        st.markdown("""
        Our forgery detection model is based on ResNet50, a deep learning model pre-trained on the ImageNet dataset.
        We fine-tuned the model using a custom dataset of genuine and forged documents.

        ### Steps:
        1. Upload one or more images in common formats (JPG, PNG, TIFF).
        2. The model will analyze each document to determine whether it's genuine or forged.
        3. Results include confidence scores for each prediction.

        ### Limitations:
        - The model works best with clean, high-quality images of documents.
        - For very complex forgeries, the model may require additional tuning and training data.
        """)

else:
    st.info("Please upload document images to begin the analysis.")
