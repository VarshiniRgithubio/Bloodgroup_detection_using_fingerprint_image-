# Blood Group Detection from Fingerprint

This is a **Streamlit** application for detecting blood groups from fingerprint images using a pre-trained **Keras (TensorFlow) model**.

## 📌 Prerequisites
Make sure you have the following installed on **Windows**:
- **Python 3.10+** (Ensure it's added to PATH during installation)
- **Git** (for cloning the repository)
- **pip** (comes with Python)

## 🚀 Installation & Setup
Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/blood_group_detection_using_fingerprint_cnn.git
cd blood_group_detection_using_fingerprint_cnn
```

### 2️⃣ Create a Virtual Environment (Without Conda)
```sh
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
```sh
venv\Scripts\activate
```

### 4️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 📂 Project Structure
```
├── Model/
│   ├── keras_Model.h5   # Trained model file
│   ├── labels.txt       # Labels for classification
├── app.py               # Main Streamlit app
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
```

## 🛠 Troubleshooting
- If `streamlit` is not recognized, make sure the virtual environment is activated.
- If TensorFlow is missing, try running:
  ```sh
  pip install tensorflow
  ```
- If you face Python version issues, ensure you’re using **Python 3.10+**.

## 📜 License
This project is **open-source**. Feel free to modify and improve it! 🎉

