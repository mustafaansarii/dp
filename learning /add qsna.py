import csv
import requests

CSV_FILE = "coding_questions.csv"  # Update with the actual CSV file path
API_URL = "http://127.0.0.1:5000/add-qsn"


def add_questions_from_csv(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            payload = {
                "topic": row.get("topic"),
                "title": row.get("title"),
                "qsnlink": row.get("qsnlink")
            }

            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                print(f"Successfully added: {row['title']}")
            else:
                print(f"Failed to add: {row['title']}. Error: {response.text}")


if __name__ == "__main__":
    add_questions_from_csv(CSV_FILE)
