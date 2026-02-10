# Skill: LinkedIn Automation (Aisha)

# Skill: LinkedIn Engagement & Community Growth

## Capabilities
- **Autonomous Content Generation**: Uses OpenAI (GPT-4o) to generate professional, mission-aligned posts based on Marsa's three pillars.
- **Instant Response System**: Triggers an immediate post upon script execution (`main.py --run`), ensuring posts happen within 30 seconds of manual intervention.
- **Scheduled Engagement**: Maintains a consistent 3-hour posting frequency for 24/7 visibility.
- **Mission Integration**: Deeply understands Marsa's core pillars: Safety, Community, and Growth.

## Procedure
1. **Initialize**: Validate environment variables (`LINKEDIN_ACCESS_TOKEN`, `OPENAI_API_KEY`, `LINKEDIN_ORGANIZATION_ID`).
2. **Instant Post**: Upon execution, immediately generate and publish content to LinkedIn to confirm the system is live.
3. **Generate Content**: Aisha uses OpenAI to draft a post focusing on one of the three pillars (Safety, Community, or Growth).
4. **Publish**: Access the LinkedIn API (`v2/posts`) to share the update with the world.
5. **Wait**: Enter a 3-hour wait state before the next autonomous cycle.

## Context
Aisha acts as the Digital FTE for Marsa Empower, ensuring that the brand's voice is consistently heard, empowering women through technology and community.

## Examples
- "Aisha just shared a new update on Sentinel Mode: Your passive safety companion for late-night commutes."
- "Empowering financial independence: Aisha's guide to wealth building for women."
