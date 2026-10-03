\# Day 52 – Environment Configuration \& DevOps Basics



\## Project

ZecPath Admin Backend



\## 1. Environment Configuration



Created `.env.example` to define environment variables without storing real secrets.



Configured placeholders for:

\- Django SECRET\_KEY

\- Database credentials

\- Razorpay credentials

\- OpenAI API key

\- Redis URL

\- Email credentials



Real `.env` files are excluded from Git using `.gitignore`.



\## 2. Secrets Management



The following are protected from Git commits:



\- `.env`

\- `.venv`

\- Python cache files



No real API keys, passwords, payment secrets, or database credentials are stored in the repository.



\## 3. CI/CD Pipeline



Created GitHub Actions workflow:



`.github/workflows/ci.yml`



The workflow:

\- Runs on pushes to `main`

\- Runs on pull requests to `main`

\- Checks out the repository

\- Installs Python 3.12

\- Installs project dependencies

\- Runs Django system checks



\## 4. Deployment Automation



Created:



`deploy.sh`



The deployment script automates:

\- Pulling the latest GitHub code

\- Activating the Python virtual environment

\- Installing dependencies

\- Running database migrations

\- Collecting static files

\- Restarting the Gunicorn service



\## 5. Deliverables



\- Environment configuration template

\- Secrets protection through `.gitignore`

\- Basic GitHub Actions CI pipeline

\- Automated deployment script

\- Deployment documentation



\## Status



Day 52 DevOps configuration and automation files have been created and prepared for GitHub/cloud deployment.

