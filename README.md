# Loan Approval Prediction using Machine Learning

## Project Overview

This project uses Machine Learning to predict whether a loan application should be approved or rejected based on applicant information such as gender, marital status, education level, income, loan amount, and credit history.

The project demonstrates the complete machine learning workflow, including data preprocessing, label encoding, model training, evaluation, visualization, and deployment preparation.

---

## Dataset Information

Features:

- Gender
- Married
- Education
- ApplicantIncome
- LoanAmount
- CreditHistory

Target Variable:

- LoanStatus

Target Classes:

- 1 = Approved
- 0 = Rejected

---

## Project Workflow

1. Data Collection
2. Data Exploration
3. Data Preprocessing
4. Label Encoding
5. Feature and Target Separation
6. Train-Test Split
7. Model Training
8. Prediction
9. Model Evaluation
10. Model Saving
11. Deployment Preparation

---

## Data Preprocessing

Categorical variables were converted into numerical values using Label Encoding.

Examples:

| Original Value | Encoded Value |
|----------------|--------------|
| Male | 1 |
| Female | 0 |
| Yes | 1 |
| No | 0 |

This step allows machine learning algorithms to process the data.

---

## Model Used

### Logistic Regression

The Logistic Regression algorithm was selected as the primary classification model for this project.

Benefits:

- Simple and efficient
- Easy to interpret
- Suitable for binary classification
- Fast training and prediction

---

## Model Evaluation

Evaluation metrics used:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score

Results:

- Accuracy: 50%
- Precision: 100%
- Recall: 50%
- F1-Score: 67%

Note:

The dataset contains only 10 records for learning purposes, so the evaluation results are not representative of real-world performance.

---

## Confusion Matrix

The confusion matrix was used to visualize model predictions and classification errors.

Example:

![Confusion Matrix](confusion_matrix.png)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib
- Streamlit
- Google Colab

---

## Project Structure

loan-approval-prediction/

├── notebook.ipynb

├── app.py

├── loan_model.pkl

├── requirements.txt

├── README.md

└── confusion_matrix.png

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mirukyilikal/loan-approval-prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

- Use a larger real-world dataset
- Hyperparameter tuning
- Cross-validation
- Feature engineering
- Compare multiple classification algorithms
- Deploy using Streamlit Cloud

---

## Learning Outcomes

Through this project, the following machine learning concepts were practiced:

- Data preprocessing
- Label encoding
- Classification
- Logistic Regression
- Model evaluation
- Confusion Matrix
- Precision, Recall, and F1-Score
- Model deployment preparation

---

## Author

**Miruk Yilikal**

Fourth-Year Electrical and Computer Engineering Student

Addis Ababa University

Interests:
- Artificial Intelligence
- Machine Learning
- Data Analytics
- Frontend Development
- Health-Tech Innovation
