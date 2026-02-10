import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

def debug_linkedin():
    if not ACCESS_TOKEN:
        print("Error: No ACCESS_TOKEN found in .env")
        return

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    print("--- 1. Checking Me (Member Profile) ---")
    try:
        response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"Name: {data.get('localizedFirstName')} {data.get('localizedLastName')}")
            print(f"Person URN: urn:li:person:{data.get('id')}")
        else:
            print(f"Me failed: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- 2. Checking Administered Organizations ---")
    try:
        url = "https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&role=ADMINISTRATOR&state=APPROVED"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            elements = data.get("elements", [])
            if not elements:
                print("No administered organizations found.")
            for el in elements:
                org_urn = el.get("organizationalTarget")
                print(f"Admin for Org: {org_urn}")
        else:
            print(f"Org check failed: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_linkedin()
