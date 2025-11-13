# 🔮 Crime Type Prediction App

## 🧩 Project Overview

The **Crime Type Prediction App** is a **Machine Learning web application** that predicts the **most likely type of crime** for a given **Indian district, state, and year** based on **historical crime data**.

---

### 🔍 Problem Statement

Crime prevention and law enforcement planning often rely on analyzing historical crime trends.  
However, **manual analysis** cannot capture complex correlations between **geography, time, and crime types**.

This project uses **machine learning** to:
- Identify the **most probable crime** type in a given region and year  
- Help law enforcement **anticipate and allocate resources** effectively  
- Enable **data-driven policymaking** using predictive analytics  

---

## 📊 Dataset Source

- **Dataset Name:** Crime Statistics of India (compiled from NCRB data)
- **File:** `crime_dataset.csv`
- **Size:** ~5,000+ district-level records from multiple years
- **Key Features:**
  - `state_name` — State name  
  - `district_name` — District name  
  - `year` — Year of report  
  - Multiple columns for crime counts (murder, theft, rape, etc.)

---

### 🧹 Data Preprocessing Steps

| Step | Operation | Description |
|------|------------|--------------|
| 1️⃣ | Data Cleaning | Removed missing or inconsistent records |
| 2️⃣ | Feature Encoding | Label encoded categorical columns (`state_name`, `district_name`) |
| 3️⃣ | Feature Selection | Selected relevant features for classification |
| 4️⃣ | Target Creation | Generated `top_crime` (most frequent crime type per row) |
| 5️⃣ | Normalization | Scaled numerical data for model stability |

---

## ⚙️ Methods

### 🧠 Approach

Two machine learning models were trained and compared:

| Model | Type | Strengths | Weaknesses | Accuracy |
|--------|------|------------|-------------|-----------|
| **Random Forest Classifier** | Ensemble (Decision Trees) | High accuracy, handles non-linearity | Larger model size | **0.85** |
| **Logistic Regression** | Statistical | Simple, interpretable | Assumes linearity | 0.62 |

✅ **Selected Model:** Random Forest (best-performing)

---

### 🔬 Methodology Diagram

```text
          ┌───────────────────────────────┐
          │   Crime Dataset (CSV File)    │
          └──────────────┬────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │ Data Preprocessing & Cleaning       │
        │ - Handle missing values             │
        │ - Encode categorical columns        │
        │ - Create target variable (top_crime)│
        └──────────────────┬─────────────────┘
                           │
                           ▼
       ┌────────────────────────────────────┐
       │ Model Training & Evaluation         │
       │ - Train Random Forest, LogisticReg. │
       │ - Compare accuracies                │
       │ - Save best model as .pkl           │
       └──────────────────┬─────────────────┘
                          │
                          ▼
          ┌──────────────────────────────────┐
          │ Streamlit Web App (app.py)       │
          │ - User inputs: Year, State, Dist │
          │ - Outputs: Predicted Crime Type  │
          └──────────────────────────────────┘
