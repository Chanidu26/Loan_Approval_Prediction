# Loan Approval Machine Learning Project

This repository contains the code and documentation for a machine learning project focused on predicting loan approval status based on various features such as income, education, loan amount, no of dependants and more.

## Project Overview

The primary goal of this project is to develop a model that predicts whether a loan application will be approved or not. This prediction can help financial institutions streamline their loan approval processes and minimize risks.

### Implementation
- **Import Dataset:** Import the dataset from Kaggle.  
- **Exploratory Data Analysis (EDA):** Analyze the dataset structure, visualize relationships between features, and identify patterns or anomalies.  
- **Data Preprocessing:** Handle missing values, encode categorical variables, and scale features to ensure consistency.  
- **Feature Engineering:** Select relevant features, remove redundant ones, and create new features to enhance model performance.  
- **Data Splitting:** Divide the dataset into training and testing sets to evaluate model performance.  
- **Model Training:** Utilize SVM and Logistic Regression machine learning algorithms to determine the best fit for the dataset.  
- **Cross-Validation:** Perform cross-validation to ensure the model generalizes well to unseen data.  
- **Model Evaluation:** Measure performance using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.  
- **Model Comparison:** Compare the performance of SVM and Logistic Regression based on evaluation metrics and select the best model.

## Data Information
The dataset used for this project contains information on applicants such as:
- **No of dependents**
- **Education**
- **Applicant Income**
- **self employability**
- **Loan Amount**
- **Loan Amount Term**
- **cibil score**
- **Assets**
- **Loan Status**

### Data Source
The dataset is publicly available and can be accessed [here](#).

## Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Jupyter Notebook:** For data analysis and model development

## Algorithms Used and Accuracy Performance
- **SVM (Support Vector Machine)** - Testing (93%) and Training (94%)
- **Logistic Regression** - Testing (91%) and Training (92%)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Chanidu26/Loan_Approval_Prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd webapp
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application in the `/webapp` directory.
2. Run the Jupyter Notebook to preprocess data and train the model:
   ```bash
   python app.py
   ```
3. Evaluate the model and save the trained model for deployment.

## File Structure
```
loan-approval-ml/
├── dataset/
│   ├── loan_approval_dataset.csv
├── notebook/
│   ├── Loan_Approvel_Prediction.ipynb
├── webapp/
│   ├── env
│   ├── model
│   ├── templates
│   ├── app.py
│   ├── requirements.txt
└── README.md
```

## Future Enhancements
- Deploying the model using Flask
- Integrating with a front-end application for real-time predictions.
- Using advanced techniques like hyperparameter tuning and ensemble methods to improve model accuracy.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any features or bug fixes.

## License
This project is licensed under the [MIT License](LICENSE).
