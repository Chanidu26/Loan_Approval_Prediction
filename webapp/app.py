from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Correct way to load models with pickle
with open('model/scaler_model.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('model/SVM_model.pkl', 'rb') as svm_file:
    svm_model = pickle.load(svm_file)

with open('model/logistic_model.pkl', 'rb') as logistic_file:
    logistic_model = pickle.load(logistic_file)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        try:
            no_of_dependents = int(request.form['no_of_dependents'])
            education = 1 if request.form['education'] == 'Graduate' else 0
            self_employed = 1 if request.form['self_employed'] == 'Yes' else 0
            income_annum = int(request.form['income_annum'])
            loan_amount = int(request.form['loan_amount'])
            loan_term = int(request.form['loan_term'])
            cibil_score = int(request.form['cibil_score'])
            residential_assets_value = int(request.form['residential_assets_value'])
            commercial_assets_value = int(request.form['commercial_assets_value'])
            luxury_assets_value = int(request.form['luxury_assets_value'])
            bank_asset_value = int(request.form['bank_asset_value'])

            # Create a DataFrame
            feature_names = [
                'no_of_dependents', 'education', 'self_employed', 'income_annum',
                'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
                'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'
            ]
            df = pd.DataFrame([[
                no_of_dependents, education, self_employed, income_annum, loan_amount,
                loan_term, cibil_score, residential_assets_value, commercial_assets_value,
                luxury_assets_value, bank_asset_value
            ]], columns=feature_names)

            # Scale the data
            df_scaled = scaler.transform(df)

            # Predict
            prediction = svm_model.predict(df_scaled)
            result = "Approved" if prediction[0] == 1 else "Rejected"

            return render_template('index.html', prediction=result)

        except Exception as e:
            return render_template('index.html', prediction=f"Error: {str(e)}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
