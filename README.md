# 🚀 Fraud Snap: Document Forgery Detection

![Project Logo](https://drive.google.com/file/d/1ZVZWMoGNTbqFFtjZzaJHTISlfTKGy9ji/view?usp=sharing) 

## 📖 Description

This project is a **document forgery detection system** developed for the [Hackathon Name]. The goal is to use deep learning to detect forged documents based on image analysis.

Our model analyzes images of documents, classifies them as **genuine** or **forged**, and returns the confidence level of the prediction. It's a powerful tool to combat document fraud in industries like **healthcare**, **insurance**, and **legal sectors**.

## 📂 Dataset

The dataset used for this project consists of images of genuine and forged documents, specifically designed for document forgery detection. It includes:

- **Genuine Documents**: Real documents in different formats.
- **Forged Documents**: Manipulated versions of genuine documents created with various editing tools.

The dataset can be accessed via the following sources:

- **Doctor Bills Dataset**: [Download Here](https://madm.dfki.de/downloads-ds-doctor-bills)
- **Doctor Bills Dataset**: [Download Here](https://drive.google.com/drive/folders/11Kg6vjd4CbqwguFgpfClK6E_0_DqjJas?usp=sharing) (Drive link)
- NOTE: The 2nd link is a drive link with images categorized into forged and genuine accordingly

Dataset distribution:

| Type      | Genuine | Forged |
|-----------|---------|--------|
| Type 01a  | 30      | 9      |
| Type 01b  | 20      | 0      |
| Type 02   | 40      | 12     |

Ensure that the dataset is pre-processed correctly (resize, normalization, etc.) before feeding it into the model.

---

## 📝 Table of Contents
1. [Features](#Features)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Technologies Used](#Technologies-Used)
5. [Screenshots](#Screenshots)
6. [Contributing](#Contributing)
7. [License](#License)
8. [Team Members](#Team-Members)

## ⭐ Features

- 🔍 **Real-time document forgery detection** using a trained deep learning model.
- 📄 **Batch processing** of multiple document images at once.
- 📊 **Confidence scoring** for each prediction.
- 🌐 **Web-based interface** built with Streamlit for easy interaction.
- 📥 **Downloadable reports** summarizing results in CSV format.

## 🛠 Installation

Follow these steps to run the project locally:

### Prerequisites

- **Python 3.7+**
- **pip** 
- **Git** 

### Setting Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/veydantkatyal/fraud-snap.git
   cd fraud-snap
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Depedencies**

   ```bash
   pip install -r requirements.txt
4. **Run the Streamlit App**

   ```bash
   streamlit run app.py
The app will be hosted locally, and you can access it by visiting [http://localhost:8501](http://localhost:8501) in your browser.

## 🚀 Usage

- **Upload Document Images**: Click on the "Upload" button to select one or more document images (JPG, PNG, TIFF).
- **Process the Images**: The app will analyze each document and display whether it's genuine or forged.
- **Download Report**: After processing, you can download the prediction report as a CSV file.
- **Batch Processing**: You can upload multiple documents simultaneously for bulk forgery detection.

---

## 💻 Technologies Used

- **Streamlit**: Interactive web app framework for data science.
- **PyTorch**: Deep learning framework for model training and inference.
- **torchvision**: Image transformations and pre-trained models.
- **Pandas**: Data manipulation and CSV handling.
- **Pillow**: Image processing in Python.
- **pyngrok**: Expose the local app to the web (for development).

---

## 🖼 Screenshots

### Home Page

![Home Page Screenshot](link-to-your-screenshot-1)

### Prediction Results

![Prediction Results Screenshot](link-to-your-screenshot-2)

---

## 🤝 Contributing

We welcome contributions! To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request, and we'll review it ASAP!

---

## Contributors

Thank you to all contributors! 😊

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team Members

| Name           | GitHub Profile                                       |
|----------------|------------------------------------------------------|
| Veydant Katyal      | [veydantkatyal](https://github.com/veydantkatyal) |
| Aditya Agarwal | [Aditya Agarwal](https://github.com/LabSample)   |




