import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

def find_urn():
    if not ACCESS_TOKEN:
        print("Error: No LINKEDIN_ACCESS_TOKEN found in .env")
        return

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    print("--- Attempting to find your Person URN ---")
    
    # Try the userinfo endpoint (OpenID Connect)
    try:
        response = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)
        if response.status_code == 200:
            data = response.json()
            sub = data.get('sub')
            print(f"SUCCESS! Your Person URN is: urn:li:person:{sub}")
            return
        else:
            print(f"UserInfo failed ({response.status_code}). Trying /v2/me...")
    except Exception as e:
        print(f"UserInfo Error: {e}")

    # Try the legacy /v2/me endpoint
    try:
        response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
        if response.status_code == 200:
            data = response.json()
            person_id = data.get('id')
            print(f"SUCCESS! Your Person URN is: urn:li:person:{person_id}")
        else:
            print(f"Me failed ({response.status_code}).")
            print("Response:", response.text)
            print("\n[TIP] Go to the Token Inspector: https://www.linkedin.com/developers/tools/oauth/token-inspector")
            print("It will show your URN at the bottom of the page.")
    except Exception as e:
        print(f"Me Error: {e}")

if __name__ == "__main__":
    find_urn()
