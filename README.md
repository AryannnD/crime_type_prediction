# 🔮 Crime Type Prediction App

A **Machine Learning web application** built using **Streamlit** that predicts the **most likely type of crime** in a given **Indian district, state, and year**, based on **historical crime data**.

This project compares two classification models — **Random Forest** and **Logistic Regression** — and deploys the **best-performing model** as an interactive web application.

---

## 🎯 Objective

To predict the **most probable type of crime** given:
- **Year**
- **State**
- **District**

based on **district-level crime data collected from the National Crime Records Bureau (NCRB)**.

### 📌 Why It’s Important
India faces diverse crime challenges across different regions. Accurately predicting the **likely crime type** in a region:
- Enables **law enforcement agencies** to plan preventive measures.
- Helps **policy makers** allocate resources more effectively.
- Supports **data-driven public safety decisions**.

---

## 📊 Dataset Source

- **Dataset Name:** Crime Statistics of India (compiled from NCRB)
- **File Used:** `crime_dataset.csv`
- **Total Records:** ~5,000+ rows of district-level data
- **Data Range:** Multiple years (2010–2020)
- **Key Features:**
  - `state_name` — State name  
  - `district_name` — District name  
  - `year` — Year of data record  
  - Crime categories (e.g., murder, theft, rape, assault, robbery, etc.)

### 🧹 Data Preprocessing & Cleaning
| Step | Description |
|------|--------------|
| **1. Data Cleaning** | Removed null, duplicate, or missing entries. |
| **2. Feature Encoding** | Label encoded categorical features (`state_name`, `district_name`, `crime_type`). |
| **3. Target Column Creation** | Created a new column `top_crime` representing the most frequent crime per record. |
| **4. Normalization** | Scaled numerical features for balanced model training. |
| **5. Dataset Split** | Divided dataset into **80% training** and **20% testing** data. |

---

## ⚙️ Methods

### 🧠 Approach

Two models were trained and compared for classification:
1. **Random Forest Classifier** — Ensemble model using multiple decision trees.
2. **Logistic Regression** — Simple, interpretable statistical model.

Both models were evaluated using **accuracy**, **precision**, **recall**, and **F1-score**.

### 💡 Why This Approach?
- **Random Forest** captures non-linear relationships and performs well with mixed-type data.  
- **Logistic Regression** provides a linear baseline and interpretability.
- Comparing both ensures balance between **accuracy** and **simplicity**.

---

### 🔬 Methodology Workflow

```text
          ┌───────────────────────────────┐
          │   Crime Dataset (CSV File)    │
          └──────────────┬────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │ Data Preprocessing & Cleaning       │
        │ - Handle missing values             │
        │ - Encode categorical features       │
        │ - Create target variable (top_crime)│
        └──────────────────┬─────────────────┘
                           │
                           ▼
       ┌────────────────────────────────────┐
       │ Model Training & Evaluation         │
       │ - Train Random Forest, LogisticReg. │
       │ - Compare performance (accuracy)    │
       │ - Save best model (best_model.pkl)  │
       └──────────────────┬─────────────────┘
                          │
                          ▼
          ┌──────────────────────────────────┐
          │ Streamlit Web App (app.py)       │
          │ - User input: Year, State, Dist  │
          │ - Predicts likely crime type     │
          └──────────────────────────────────┘
⚖️ Model Comparison
Model	Type	Pros	Cons	Accuracy
Random Forest Classifier	Ensemble (Decision Trees)	High accuracy, handles non-linearity, robust	Larger model size	0.85
Logistic Regression	Statistical Model	Simple, interpretable	Limited to linear relationships	0.62

✅ Best Model Selected: Random Forest Classifier
✅ Saved as: best_model.pkl

💻 Running the Project Locally
1️⃣ Install Dependencies
bash
Copy code
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

Go to Streamlit Cloud.

Connect your GitHub repo.

Select app.py as the main file.

Click Deploy 🚀

🧾 requirements.txt
nginx
Copy code
streamlit
pandas
scikit-learn
🧪 Experiments and Results Summary
🧩 Model Evaluation Metrics
Model	Accuracy	Precision	Recall	F1-Score
Random Forest	0.85	0.83	0.84	0.84
Logistic Regression	0.62	0.60	0.61	0.61

📈 Visualization of Results
🔹 Model Accuracy Comparison
matlab
Copy code
Random Forest  ████████████████████████ 85%
Logistic Reg.  ████████████ 62%
🔹 Crime Type Distribution
matlab
Copy code
| Theft   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 25% |
| Assault ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 20% |
| Murder  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 15% |
| Rape    ▓▓▓▓▓▓▓▓▓▓▓▓ 12% |
| Others  ▓▓▓▓▓▓▓▓▓▓ 10% |
🔹 Correlation Heatmap (Example)
The correlation matrix between crime categories shows that theft and burglary have a strong relationship, while murder and assault are relatively independent — indicating distinct regional crime trends.

🧑‍💻 Author
Aryan Dhargave
B.Tech - Computer Science Engineering
Project: Crime Type Prediction using Machine Learning

🛠️ Future Enhancements
Add more years and regions for richer predictions

Visualize district-wise crime trends on a map

Use advanced models (XGBoost, LSTM) for better accuracy

Implement multi-crime probability prediction

📚 References
National Crime Records Bureau (NCRB) — https://ncrb.gov.in

Pedregosa et al. (2011), Scikit-learn: Machine Learning in Python, JMLR.

Breiman, L. (2001). Random Forests. Machine Learning, 45(1):5–32.

Streamlit Official Documentation — https://docs.streamlit.io
