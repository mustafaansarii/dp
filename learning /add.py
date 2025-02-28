import pandas as pd
import requests
import time

df = pd.read_csv('coding_questions.csv')

# Define the URL for the POST request
url = "http://127.0.0.1:5000/api/add_question"

# Loop through each row in the DataFrame and send the POST request
for index, row in df.iterrows():
    payload = {
        "topic": row["Category"],
        "title": row["Question"],
        "practice_link": row["Practice Link"]
    }

    response = requests.post(url, json=payload)

    # Check if the POST request was successful
    if response.status_code == 200:
        print(f"Successfully added question: {row['Question']}")
    else:
        print(f"Failed to add question: {row['Question']}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")  # Printing the response body for debugging

    # Wait for 2 seconds before making the next POST request

