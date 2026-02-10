import os
import requests
from dotenv import load_dotenv

# Load the current .env
load_dotenv()

TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

def find_urn():
    if not TOKEN:
        print("Error: No LINKEDIN_ACCESS_TOKEN found in .env")
        return

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    print("Checking token for Person URN...")
    
    # Try userinfo first (OpenID Connect)
    try:
        response = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)
        if response.status_code == 200:
            data = response.json()
            sub = data.get("sub")
            print("SUCCESS! Your Person URN is: urn:li:person:" + sub)
            return
    except:
        pass

    # Try /me (Legacy)
    try:
        response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
        if response.status_code == 200:
            data = response.json()
            person_id = data.get("id")
            print("SUCCESS! Your Person URN is: urn:li:person:" + person_id)
            return
    except:
        pass

    print("Could not find URN directly. Please regenerate your token in the tool")
    print("and make sure to check [openid] and [profile] as well as [w_member_social].")

if __name__ == "__main__":
    find_urn()
