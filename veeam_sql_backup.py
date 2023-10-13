import requests
import json

veeam_api_url = "add url"
veaam_api_username = "my_username"
veamm_api_password = "my_password"

session = requests.Session()
session.verify = False # If needed for Veeam server SSL certificate

