import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

def debug():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Try userinfo
    print("Trying userinfo...")
    r = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)
    print(f"Status: {r.status_code}")
    print(f"Body: {r.text}")

if __name__ == "__main__":
    debug()
