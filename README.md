# AI-Based Phishing Email Detection

## Overview

AI-Based Phishing Email Detection is a machine learning project that analyzes email text and classifies it into two categories: **Ham (legitimate)** and **Spam**.

The system uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert email text into numerical features and **Logistic Regression** to perform the classification.

A Flask-based backend provides an API through which an email can be submitted for prediction along with the model's confidence score.

---

## Features

* Email text classification
* TF-IDF-based text feature extraction
* Logistic Regression classification
* Prediction through a Flask API
* Confidence score for predictions
* Pre-trained model and vectorizer saved using Pickle

---

## Technologies Used

* **Python**
* **Flask**
* **Flask-CORS**
* **Pandas**
* **Scikit-learn**
* **TF-IDF Vectorizer**
* **Logistic Regression**
* **Pickle**

---

## System Workflow

```text
Email Input
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression Model
     ↓
Prediction
     ↓
Ham / Spam + Confidence Score
```

---

## Machine Learning Approach

### 1. Dataset

The project uses an `email.csv` dataset containing email messages and their corresponding categories.

The dataset columns are processed as:

* `Message` → email text
* `Category` → classification label

The labels are converted into numerical values:

```text
Ham  → 0
Spam → 1
```

### 2. Text Vectorization

The email text is converted into numerical features using **TF-IDF Vectorization**.

English stop words are removed during the vectorization process.

### 3. Model

The classification model used is **Logistic Regression** with balanced class weights.

The dataset is divided into:

* **80% training data**
* **20% testing data**

The model is evaluated using classification accuracy.

---

## Backend API

The Flask application provides a `/predict` endpoint.

### Endpoint

```text
POST /predict
```

### Input

The API accepts an email in JSON format:

```json
{
    "email": "Your email text here"
}
```

### Output

The API returns:

```json
{
    "prediction": 1,
    "confidence": 0.501
}
```

Where:

```text
0 → Ham
1 → Spam
```

The confidence value represents the maximum predicted probability returned by the trained model.

---

## Project Structure

```text
AI-Phishing-Email-Detection/
│
├── app.py
├── train.py
├── model.pkl
├── vectorizer.pkl
├── email.csv
├── requirements.txt
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

*The structure above should be adjusted if your actual frontend folder/file names are different.*

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/anvikachandrashekar/AI-Phishing-Email-Detection.git
```

### 2. Navigate to the project directory

```bash
cd AI-Phishing-Email-Detection
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

The Flask server will start locally.

### 5. Test the application

Enter an email message through the project interface and submit it for classification.

The system returns the predicted category and confidence score.

---

## Example

### Input

```text
URGENT! Your bank account has been suspended.
Click here now to verify your account.
```

### Output

```text
Prediction: Spam
Confidence: 50.10%
```

---

## Model Files

The trained machine learning components are stored using Pickle:

* `model.pkl` – trained Logistic Regression model
* `vectorizer.pkl` – trained TF-IDF vectorizer

These files are loaded by the Flask application when the API starts.

---

## Future Enhancements

* Improve classificat
