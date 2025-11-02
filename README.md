# 🔮 Crime Type Prediction App

A **Machine Learning web application** built with **Streamlit** that predicts the most likely **type of crime** in a given Indian district, state, and year based on historical data.

This project compares two classification models — **Random Forest** and **Logistic Regression** — and deploys the best-performing model as an interactive web app.

---

## 📁 Project Structure

crime_type_prediction/
│
├── app.py # Streamlit web app for prediction
├── model_training.py # Model training, evaluation & saving
├── crime_dataset.csv # Dataset containing crime statistics
├── best_model.pkl # Trained model (Random Forest or Logistic Regression)
├── state_encoder.pkl # Encoder for state names
├── district_encoder.pkl # Encoder for district names
├── crime_encoder.pkl # Encoder for crime labels
├── requirements.txt # Dependencies for deployment
└── README.md # Project documentation

yaml
Copy code

---

## 🎯 Objective

To predict the **most likely type of crime** for a given:
- **Year**
- **State**
- **District**

based on historical district-level crime data.

---

## ⚙️ How It Works

1. **Data Preprocessing**  
   - Reads the dataset (`crime_dataset.csv`)  
   - Encodes categorical features (`state_name`, `district_name`)  
   - Creates a target column (`top_crime`) showing the most frequent crime type per record  

2. **Model Training**  
   - Trains and compares **Random Forest Classifier** and **Logistic Regression**  
   - Evaluates models using accuracy  
   - Saves the best model and encoders using `pickle`  

3. **Deployment**  
   - A **Streamlit** app (`app.py`) loads the saved model and encoders  
   - Takes user input for Year, State, and District  
   - Predicts and displays the most likely crime type

---

## 🧠 Machine Learning Models Used

| Model | Description | Pros | Cons |
|--------|--------------|------|------|
| **Random Forest Classifier** | Ensemble model combining multiple decision trees | High accuracy, handles non-linearity well | Larger model size |
| **Logistic Regression** | Statistical model for multi-class classification | Simple, interpretable | Limited to linear relationships |

---

## 📊 Evaluation

During training (`model_training.py`):
- Both models are trained on the same dataset.
- Accuracy is calculated and compared.
- The better-performing model is saved as `best_model.pkl`.

Example output:
🔹 Random Forest Accuracy: 0.85
🔹 Logistic Regression Accuracy: 0.62
✅ Best Model: Random Forest
✅ Model and encoders saved successfully!

yaml
Copy code

---

## 💻 Running the Project Locally

### 1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Train Models
bash
Copy code
python model_training.py
3️⃣ Run Streamlit App
bash
Copy code
streamlit run app.py
The app will open in your default browser at:

arduino
Copy code
http://localhost:8501
🌐 Deploy on Streamlit Cloud
Push all project files to a GitHub repository.

Go to https://share.streamlit.io.

Connect your GitHub repo.

Select app.py as the main file.

Click Deploy 🚀

🧾 requirements.txt
nginx
Copy code
streamlit
pandas
scikit-learn


🧑‍💻 Author
Aryan Dhargave
B.Tech Computer Science Engineering
Project: Crime Type Prediction using Machine Learning

🛠️ Future Enhancements

Add more years and regions for richer predictions

Visualize district-wise crime trends on a map

Use advanced models (XGBoost, LSTM) for better accuracy

Implement multi-crime probability prediction
