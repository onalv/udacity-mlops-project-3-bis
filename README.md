# Project: Deploying a ML Model to Cloud Application Platform with FastAPI

### Link to Repository:

https://github.com/onalv/udacity-mlops-project-3-bis

### Link to deployed application

https://udacity-mlops-project-3-bis.onrender.com/

This project focuses on deploying a machine learning model that predicts the salary category of an individual based on their financial attributes. The model, a Random Forest classifier, was trained using the UCI Machine Learning Repository's Census Income dataset. It aims to assist in financial analysis and planning by providing insights into salary categories. For more details on the model, its intended use, training data, and performance metrics, refer to the [Model Card](https://github.com/onalv/udacity-mlops-project-3-bis/blob/main/model_card.md).

### How to Use

The deployed model can be interacted with through a REST API hosted at https://udacity-mlops-project-3-bis.onrender.com/. To make predictions, send a POST request to the API with a JSON payload containing the individual's financial attributes. Below is an example of how to use the API with Python's `requests` library:

```python
import requests

# Example data
data = {
    'age': 35,
    'workclass': 'Private',
    'fnlgt': 215646,
    'education': 'HS-grad',
    'marital_status': 'Divorced',
    'occupation': 'Handlers-cleaners',
    'relationship': 'Not-in-family',
    'race': 'White',
    'sex': 'Male',
    'hoursPerWeek': 40,
    'nativeCountry': 'United-States'
}

# Sending a POST request to the API
response = requests.post('https://udacity-mlops-project-3-bis.onrender.com/', json=data)

# Checking if the request was successful
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Failed to get prediction, status code:", response.status_code)
```
