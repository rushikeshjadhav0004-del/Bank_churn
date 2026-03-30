📊 Bank Customer Churn Prediction
🚀 Project Overview

This project focuses on predicting whether a bank customer will churn (leave the bank) or not using Machine Learning techniques.

The model analyzes customer data such as credit score, age, balance, and activity to identify churn patterns and help businesses improve customer retention.

📂 Dataset
Dataset used: Bank_Churn.csv
Target variable: Exited
0 → Customer stays
1 → Customer churns
🔑 Features Used:
CreditScore
Age
Tenure
Balance
NumOfProducts
HasCrCard
IsActiveMember
EstimatedSalary
⚙️ Project Workflow
1. Data Preprocessing
Removed unnecessary columns:
CustomerId, Surname
Checked:
Missing values
Duplicate records
Feature separation:
X → Input features
y → Target variable
2. Exploratory Data Analysis (EDA)
Distribution plots for numerical features
Count plots for categorical features
Relationship with churn (Exited)
Correlation heatmap
3. Handling Imbalanced Data
Applied SMOTE (Synthetic Minority Oversampling Technique)
Used only on training data to avoid data leakage
4. Model Building

Models used:

Logistic Regression
Random Forest Classifier
Support Vector Machine (SVM)
Gradient Boosting Classifier
5. Pipeline & Preprocessing
Used Pipeline for clean workflow
Applied:
StandardScaler (for numerical features)
Used ColumnTransformer
6. Model Evaluation

Metrics used:

Accuracy
Precision
Recall
F1-score
Confusion Matrix
ROC-AUC Curve
7. Hyperparameter Tuning
Used GridSearchCV for:
Random Forest
Gradient Boosting
Optimized parameters like:
Number of estimators
Max depth
Learning rate
8. Threshold Tuning
Adjusted prediction threshold (e.g., 0.3 instead of 0.5)
Improved recall for churn class
9. Feature Importance
Visualized most important features influencing churn
10. Model Saving

Final model saved using:

joblib.dump(best_model, "best_model.pkl")
📈 Results
Achieved improved performance using:
SMOTE
Hyperparameter tuning
Gradient Boosting
Balanced trade-off between:
Recall (important for churn detection)
Accuracy
🛠️ Technologies Used
Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
Imbalanced-learn (SMOTE)
Joblib
▶️ How to Run
Clone the repository:
git clone <your-repo-link>
Install dependencies:
pip install -r requirements.txt
Run the notebook:
jupyter notebook
📌 Future Improvements
Deploy using Streamlit / Flask
Add real-time prediction UI
Try advanced models (XGBoost, LightGBM)
Feature engineering
👨‍💻 Author

Rushikesh Jadhav
