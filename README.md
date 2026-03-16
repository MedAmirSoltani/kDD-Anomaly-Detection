# 🛡️ KDD Anomaly Detection — Network Intrusion Classifier

A machine learning web application for **network intrusion detection** built on the **KDD Cup 1999** dataset. The project trains and compares five classification models, then deploys the best-performing pipeline via a **Flask web app** where users can input network traffic features and receive a real-time prediction.

---

## 🌐 Live Demo

Input network connection features through the web interface → select a model → get an instant classification: **normal** or **attack** (with attack type).

---

## 🗂️ Dataset

- **Source:** [KDD Cup 1999 — Network Intrusion Detection](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
- **Task:** Multi-class classification (normal traffic vs. various attack types: DoS, Probe, R2L, U2R)
- **Features:** 41 network connection attributes (duration, protocol type, service, flag, byte counts, etc.)

---

## 🤖 Models Trained

| Model | File |
|---|---|
| Decision Tree | `dt_model.joblib` |
| K-Nearest Neighbors | `knn_model.joblib` |
| Logistic Regression | `lr_model2.joblib` |
| Naive Bayes | `nb_model.joblib` |
| Support Vector Machine | `svm_model-2.joblib` |
| Full Preprocessing Pipeline | `full_pipeline.joblib` |

All models are serialized with `joblib` and loaded at runtime by the Flask app. The `full_pipeline.joblib` handles feature encoding, scaling, and transformation consistently across all models.

---

## 🔧 Project Structure

```
kDD-Anomaly-Detection/
├── app.py                  # Flask application (routing, model inference)
├── full_pipeline.joblib    # Preprocessing pipeline (encoding + scaling)
├── dt_model.joblib         # Decision Tree
├── knn_model.joblib        # K-Nearest Neighbors
├── lr_model2.joblib        # Logistic Regression
├── nb_model.joblib         # Naive Bayes
├── svm_model-2.joblib      # Support Vector Machine
└── templates/              # HTML frontend (Jinja2 templates)
```

---

## ⚙️ How It Works

1. **Preprocessing:** Raw network connection data is passed through `full_pipeline.joblib` — handles categorical encoding (protocol type, service, flag) and numerical scaling
2. **Inference:** The preprocessed input is fed to the selected model
3. **Prediction:** The app returns whether the connection is **normal** or an **attack**, with the attack category

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install flask scikit-learn joblib pandas numpy
```

### Run the App

```bash
git clone https://github.com/MedAmirSoltani/kDD-Anomaly-Detection.git
cd kDD-Anomaly-Detection
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML Models | scikit-learn |
| Serialization | joblib |
| Backend | Flask (Python) |
| Frontend | HTML / Jinja2 |
| Dataset | KDD Cup 1999 |

---

## 👤 Author

**Mohamed Amir Soltani**  
AI Engineer | MS Big Data — UTT  
[GitHub](https://github.com/MedAmirSoltani)
