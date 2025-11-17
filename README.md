# 📩 SpamShield

**SpamShield** is a machine learning-powered web application designed to detect **Spam vs Not Spam** messages with high accuracy. Built using **TF-IDF** and **Linear SVM**, SpamShield protects your inbox by analyzing both single messages and bulk messages from CSV files.

---

## 🚀 Features

### 🔹 ML Model
- Trained on the **SMS Spam Collection Dataset**  
- Text converted to numerical features using **TF-IDF Vectorizer**  
- Classification using **Linear SVM**  
- Achieves **>95% accuracy**  
- Model (`spam_model.pkl`) and vectorizer (`tfidf.pkl`) are saved for reuse  

### 🔹 Web Application
- Input box for **single message detection**  
- Displays **Spam / Not Spam** with confidence score  
- Upload CSV to analyze **multiple messages at once**  
- Download results as CSV  

---

## 📁 Project Structure
├── app.py
├── spam_model.pkl
├── tfidf.pkl
├── templates/
│ └── index.html
├── static/
│ └── styles.css
├── dataset/
│ └── spam.csv
└── README.md


---

## 🧪 Tech Stack
- **Python**  
- **scikit-learn**  
- **Flask**  
- **Pandas**  
- **Joblib**  
- **HTML / CSS**  

---

## ▶️ How to Run Locally
1. Clone the repository:
```bash
git clone https://github.com/your-username/SpamShield.git
cd SpamShield
