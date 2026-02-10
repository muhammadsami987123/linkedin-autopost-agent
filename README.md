# 🏭 Aisha: The LinkedIn Automation Digital FTE

> "Always On. Always Caring. Always Empowering."

Aisha is a **Digital FTE (Full-Time Equivalent)** built to manage the [Marsa Empower](https://www.linkedin.com/company/marsa-empower/) LinkedIn presence. Following the **AI Agent Factory** methodology, Aisha operates as an autonomous digital employee dedicated to women's safety, health, and growth.

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- **Python 3.10+** installed.
- **pip** (Python package manager).

### 2. Installation
Navigate to the `digital-fte` directory and install the necessary libraries:
```bash
cd digital-fte
pip install requests python-dotenv
```

### 3. Configuration
1.  Copy the `example.env` file to a new file named `.env`:
    ```bash
    cp example.env .env
    ```
2.  Open `.env` and fill in your credentials.

---

## 🔑 How to get LinkedIn API Access

To allow Aisha to post on your behalf, you need a LinkedIn Access Token:

1.  **Go to the LinkedIn Developer Portal**: [linkedin.com/developers](https://www.linkedin.com/developers/).
2.  **Create an App**: Give it a name (e.g., "Marsa Aisha FTE") and link it to your company page.
3.  **Request Permissions**: Go to the **Products** tab and add:
    *   `Share on LinkedIn`
    *   `Sign In with LinkedIn`
4.  **Get Client ID/Secret**: Found under the **Auth** tab.
5.  **Generate Access Token**:
    *   Use the [LinkedIn OAuth 2.0 Tool](https://www.linkedin.com/developers/tools/oauth) to generate a **3-legged access token**.
    *   Ensure you select the `w_member_social` or `w_organization_social` scope.
    *   Copy the token into your `.env` as `LINKEDIN_ACCESS_TOKEN`.
6.  **Find Organization ID**: Your URN id can be found in the URL of your LinkedIn company page admin view (e.g., `urn:li:organization:12345678`).

---

## 🚀 Usage

Aisha can be run in two modes:

### Manual Test Run
Generates and "publishes" a single post to your terminal for verification.
```bash
python main.py
```

### 24/7 Automation Mode
Aisha starts her autonomous loop, posting every 3 hours.
```bash
python main.py --run
```

---

## 📂 Project Structure

- **`specs/`**: Contains the Markdown blueprints (Aisha's "Charter").
- **`skills/`**: The core logic folders. Each skill (like `linkedin-automation`) contains a `SKILL.md` explaining *what* it does and *how*.
- **`scripts/`**: The actual Python implementation (`automation.py`).
- **`main.py`**: The entry point/orchestrator.

---

## 🎭 Aisha's Voice & Mission
- **Mission**: Care • Safety • Growth.
- **Voice**: Sophisticated, professional, and empathetic.
- **Content Focus**: Women's safety protocols, hormonal health, financial independence, and community growth.

*Built with Plot CLI (Claude Code) following Panaversity Agent Factory Standards.*
