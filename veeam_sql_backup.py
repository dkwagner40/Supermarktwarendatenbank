import requests
import json

veeam_api_url = "https://your-veeam-server/api"
veeam_api_username = "your_username"
veeam_api_password = "your_password"

]with open("supermarket_goods.json", "r") as json_file:
    supermarket_goods_data = json.load(json_file)

session = requests.Session()
session.verify = False  # Might use it if Veeam server has a self-signed SSL certificate

login_url = f"{veeam_api_url}/token"
login_payload = {
    "grant_type": "password",
    "username": veeam_api_username,
    "password": veeam_api_password,
    "supermarket_goods": supermarket_goods  # Add the JSON data to the payload
}

response = session.post(login_url, json=login_payload)
token_data = response.json()

if "access_token" in token_data:
    access_token = token_data["access_token"]
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    print("Authenticated successfully!")

    jobs_url = f"{veeam_api_url}/jobs"
    response = session.get(jobs_url)
    jobs_data = response.json()
    print("List of Veeam jobs:")
    for job in jobs_data:
        print(f"Job ID: {job['Id']}, Name: {job['Name']}")

else:
    print("Authentication failed. Check your credentials.")
