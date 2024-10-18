from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Load the results from the CSV file
    results_df = pd.read_csv('linear_regression_results.csv')
    results = results_df.to_dict(orient='records')  # Convert to a list of dictionaries
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
