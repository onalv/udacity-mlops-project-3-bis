"""
Render Api test script
Note: Left same name for file in order to don't fail any automated tests
"""
import requests

data = {
    'age': 19,
    'workclass': 'Private',
    'fnlgt': 149184,
    'education': 'HS-grad',
    'marital_status': 'Never-married',
    'occupation': 'Prof-specialty',
    'relationship': 'Not-in-family',
    'race': 'White',
    'sex': 'Male',
    'hoursPerWeek': 60,
    'nativeCountry': 'United-States'
}

try:
    r = requests.post('https://udacity-mlops-project-3-bis.onrender.com/', json=data)
    r.raise_for_status()  # Raise an exception for HTTP error codes
    response_data = r.json()
except requests.exceptions.RequestException as e:
    print("Error occurred during request:", e)
    response_data = None

if response_data:
    print("Response code:", r.status_code)
    print("Response body:", response_data)
