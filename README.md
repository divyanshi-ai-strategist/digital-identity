# Digital Identity Aggregator

A robust, full-stack dashboard utilizing **FastAPI** and **Streamlit** to centralize professional identity data. This project implements a clean, service-oriented architecture to orchestrate data from the GitHub and LinkedIn APIs.

---

## 🏗️ Architecture Overview

The project is built on a decoupled **Client-Server** model, ensuring high maintainability and security:

- **Backend (FastAPI):** Acts as a secure proxy. It handles authentication headers, API orchestration, and data transformation.
- **Service Layer:** Encapsulates external API logic within dedicated service classes (`GitHubService`, `LinkedInService`), separating business logic from routing.
- **Frontend (Streamlit):** A reactive, Python-based UI that consumes the internal API endpoints to present a unified professional profile.
- **Package Management (uv):** Leverages `uv` for extremely fast, reliable, and reproducible dependency management.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12+ |
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | Streamlit |
| **Async HTTP** | HTTPX |
| **Manager** | uv |
| **Configuration** | Python-dotenv |

---

## 📂 Project Structure

```text
digital_identity/
├── backend/
│   ├── main.py               # FastAPI router and entry point
│   └── services/
│       ├── __init__.py
│       ├── exceptions.py      # Custom API exception handling
│       ├── github_service.py  # GitHub REST API logic
│       └── linkedin_service.py# LinkedIn OpenID Connect logic
├── frontend/
│   └── app.py                # Streamlit UI and navigation
├── .env                      # Environment variables (External API Keys)
├── pyproject.toml            # Project dependencies and metadata
└── README.md                 # Project documentation
```
## 🚀 Getting Started
1. Prerequisites
Ensure you have uv installed. If not, install it via:
```text
Bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```
2. Installation
Clone the repository and sync the environment:
```text
Bash
uv sync
```
3. API Configuration
Create a .env file in the root directory and provide your credentials:
Ini, TOML
```text
# GitHub Personal Access Token
GITHUB_TOKEN=ghp_your_github_token

# LinkedIn Long-Lived Access Token
LINKEDIN_TOKEN=your_linkedin_token

# Backend Configuration
BACKEND_API_URL=http://localhost:8000
```

4. Running the Application
The project requires both the backend and frontend to be running simultaneously.

Terminal 1: Start Backend
```text
Bash
uv run uvicorn backend.main:app --reload
```
Terminal 2: Start Frontend
```text
Bash
uv run streamlit run frontend/app.py
```

## 📋 Features
### 🔗 LinkedIn Integration
- Displays live professional profile data (Name, Email, Profile Picture).

- Implements a Service Layer that handles the OpenID Connect userinfo endpoint.

- Provides specific error feedback if tokens are expired (401 Unauthorized).

### 💻 GitHub Portfolio
- Fetches a real-time list of your repositories.

- Automatically filters out forked repositories to show original work.

- Displays repository descriptions, primary languages, and star counts.

### 🛡️ Error Handling
- The application implements custom exceptions to manage external API failures:

- Token Expiry: Explicitly catches 401 errors from LinkedIn and notifies the user.

- Rate Limiting: Catches 429 errors from GitHub to prevent app crashes during high traffic.

- Connection Failures: Gracefully handles network issues using HTTPX's exception hierarchy.

## 📜 License
Distributed under the MIT License.