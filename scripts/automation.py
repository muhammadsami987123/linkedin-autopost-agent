import os
import time
import requests
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

# Aisha's Identity & Configuration
MISSION = "Empowering Voices. Protecting Futures. Create a digital ecosystem where every woman feels safe, supported, and equipped to lead through our pillars: Uncompromising Safety, Radical Community, and Holistic Growth."
VOICE = "Aisha (Professional, Empathetic, Sophisticated, and Empowering)"
COMPANY_NAME = "Marsa Empower"
LINKEDIN_PAGE_URL = "https://www.linkedin.com/company/marsa-empower/"

# API Configuration
CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
ORG_ID = os.getenv("LINKEDIN_ORGANIZATION_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI Client
client = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)

class LinkedInDigitalFTE:
    def __init__(self):
        self.skill_name = "linkedin-automation"
        self.last_post_time = None
        self.interval_seconds = 3 * 60 * 60  # 3 hours

    def generate_content(self):
        """
        Generate a LinkedIn post using OpenAI (Aisha's brain).
        Integrates Marsa's core values: Safety, Community, and Growth.
        """
        if not client:
            print("Warning: OpenAI API Key missing. Using fallback content.")
            return self.fallback_content()

        print(f"[{datetime.now()}] AISHA IS ANALYZING MARSA'S MISSION...")
        
        prompt = f"""
        You are {VOICE}, the Digital FTE for {COMPANY_NAME}.
        
        PRIMARY MISSION:
        We create a digital ecosystem where every woman feels safe, supported, and equipped to lead.
        
        CORE PILLARS (Choose ONE specifically for this post):
        1. Uncompromising Safety: Using advanced AI for harassment detection and SOS signals (Sentinel Mode).
        2. Radical Community: Spaces where shared experiences become collective strength and wisdom.
        3. Holistic Growth: Providing tools, capital, and mentorship for professional and personal acceleration.
        
        TONE:
        Sophisticated yet empathetic. Technology should be seen as a "Shield, not a weapon."
        
        FORMAT:
        MARSA | Aisha
        [Empowering Header]
        [Insightful body about the chosen pillar - use short, impactful paragraphs]
        [Call to Action: Be Part of the Change / Stay Empowered]
        [Hashtags: #MarsaEmpower #DigitalFTE #Aisha #WomenSafety #EmpoweringFutures]
        
        Generate a post that feels premium and authentic to our website (marsa-empower.vercel.app).
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are Aisha, the sophisticated AI Digital FTE of Marsa Empower. You speak with authority and grace."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI Generation Error: {e}")
            return self.fallback_content()

    def fallback_content(self):
        """
        Static fallback content if AI fails.
        """
        topics = [
            "Safety: Understanding Sentinel Mode and how it can protect you during late nights.",
            "Health: Period care and hormonal balance - how Aisha's health hub helps.",
            "Growth: Why financial independence is the ultimate empowerment for women.",
            "Safety: The SOS Signal - broadcast your distress with one tap."
        ]
        topic = topics[int(time.time() / self.interval_seconds) % len(topics)]
        
        content = f"MARSA | Aisha\n\n"
        content += f"Mission: {MISSION} \n\n"
        content += f"Today's Insight: {topic}\n\n"
        content += "Stay Safe. Stay EMPOWERED. 🛡️🏥🔮\n\n"
        content += f"#MarsaEmpower #WomenSafety #DigitalFTE #Aisha #FutureIsFemale"
        return content

    def generate_image_prompt(self):
        """
        Generate a prompt for image generation.
        """
        return "Minimalist Apple-style aesthetic, soft purple and white gradients, clean typography, MARSA logo, empowering women theme, high resolution."

    def post_to_linkedin(self, content):
        """
        Post real content to LinkedIn using the newer /v2/posts API.
        """
        print(f"[{datetime.now()}] ATTEMPTING POST TO LINKEDIN (v2/posts)...")
        
        if not ACCESS_TOKEN or not ORG_ID:
            print("Error: Missing Access Token or Organization ID in .env")
            return

        print(f"DEBUG: Using Author URN: {ORG_ID}")

        # Modern LinkedIn API endpoint (v2/posts)
        url = "https://api.linkedin.com/v2/posts"
        
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
            # Note: Newer LinkedIn APIs sometimes require a version header, 
            # but v2/posts is generally available on standard OAuth tokens.
        }
        
        # Structure for the newer 'posts' API
        payload = {
            "author": ORG_ID,
            "commentary": content,
            "visibility": "PUBLIC",
            "distribution": {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": []
            },
            "lifecycleState": "PUBLISHED",
            "isReshareDisabledByAuthor": False
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 201:
                print("-" * 30)
                # Safe print for Windows terminal
                print(content.encode('ascii', 'ignore').decode('ascii')) 
                print("-" * 30)
                print(f"SUCCESS: Post live on {COMPANY_NAME} Page!")
            else:
                print(f"FAILED to post: {response.status_code}")
                print(response.text)
                if response.status_code == 403:
                    print("\n[HINT] This usually means your token lacks 'w_organization_social' scope")
                    print("or you haven't clicked 'Verify' in the Developer Portal settings.")
        except Exception as e:
            print(f"API Error: {str(e)}")

    def run_loop(self):
        print(f"==========================================")
        print(f"Aisha's Digital FTE is now ACTIVE.")
        print(f"Behavior: POSTING IMMEDIATELY (within 30s)")
        print(f"Schedule: Then recurring every 3 hours.")
        print(f"==========================================")
        
        while True:
            # Step 1: Generate and Post IMMEDIATELY
            content = self.generate_content()
            self.post_to_linkedin(content)
            
            # Step 2: Sleep for the interval
            print(f"Aisha is now monitoring. Next autonomous post in 3 hours...")
            time.sleep(self.interval_seconds)

if __name__ == "__main__":
    aisha = LinkedInDigitalFTE()
    # For initial test, we run once. 
    # In production, we would run aisha.run_loop()
    print("--- AISHA (DIGITAL FTE) TEST RUN ---")
    content = aisha.generate_content()
    aisha.post_to_linkedin(content)
    print("Test Complete.")
