import os
import sys

# Add scripts folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from automation import LinkedInDigitalFTE

def main():
    print("==========================================")
    print("      MARSA EMPOWER - DIGITAL FTE         ")
    print("      Aisha: LinkedIn Automation          ")
    print("==========================================")
    
    aisha = LinkedInDigitalFTE()
    
    # Check for CLI arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--run":
        aisha.run_loop()
    else:
        # Default: Manual run
        content = aisha.generate_content()
        aisha.post_to_linkedin(content)
        print("\n[TIP] Run with '--run' for continuous 3-hour automation.")

if __name__ == "__main__":
    main()
