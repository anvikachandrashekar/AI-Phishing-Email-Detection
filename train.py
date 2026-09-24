import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("email.csv")

# Rename columns
df = df.rename(columns={
    "Message": "email_text",
    "Category": "label"
})

# Clean labels (IMPORTANT FIX)
df["label"] = df["label"].astype(str).str.strip().str.lower()

# Convert to numeric
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Remove invalid rows
df = df.dropna(subset=["label"])

# Features and labels
X = df["email_text"]
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# NLP: Convert text → numbers using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# TEST MANUALLY
test_email = ["URGENT! Your bank account has been suspended. Click here now!"]
vec = vectorizer.transform(test_email)
print("Test Prediction:", model.predict(vec))