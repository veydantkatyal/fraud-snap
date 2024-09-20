import os
import sys
import torch
import pandas as pd
from torchvision import transforms
from PIL import Image
from model import load_model  # Assuming your model is in a separate file named 'model.py'
from pyngrok import ngrok


# Define data transformations for preprocessing the images (resize, normalize, etc.)
data_transforms = {
    'val': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
}

# Function to load and preprocess images
def load_image(image_path):
    image = Image.open(image_path).convert('RGB')  # Ensure image is in RGB format
    image = data_transforms['val'](image).unsqueeze(0)  # Apply transforms and add batch dimension
    return image

# Function to process the images and predict using the trained model
def process_folder(folder_path, model):
    results = []
    
    # Iterate over the images in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".tif"):
            image_path = os.path.join(folder_path, filename)
            image = load_image(image_path).to(device)
            
            with torch.no_grad():
                output = model(image)
                _, predicted = torch.max(output, 1)
                confidence = torch.softmax(output, dim=1).max().item() * 100
                is_forged = bool(predicted.item())  # 0 -> genuine, 1 -> forged
                results.append((filename, 'Forged' if is_forged else 'Genuine', confidence))
    
    # Save results to CSV
    df = pd.DataFrame(results, columns=["file_name", "prediction", "confidence"])
    df.to_csv("prediction_results.csv", index=False)
    print("Results saved to 'prediction_results.csv'")

def expose_app():
    # Expose the app using ngrok for remote access
    public_url = ngrok.connect(8501)
    print(f"Streamlit app is running publicly at: {public_url}")

def main():
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]

    # Load the pre-trained model
    print("Loading model...")
    model = load_model()
    model.eval()  # Set the model to evaluation mode
    
    # Set up device
    global device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    # Process the folder of images
    print(f"Processing images in folder: {folder_path}")
    process_folder(folder_path, model)

    # Optionally expose the app using ngrok (for Streamlit app exposure)
    expose_app()

if __name__ == "__main__":
    main()
