# Simple Login Web App (Flask + HTML) - Cyber Lab Project

## Run locally in VS Code (macOS)
1. Open this folder in VS Code (File > Open Folder).
2. Open the terminal (Ctrl + `) and run:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py
   ```
3. Browse to http://127.0.0.1:5001
   (Port 5001 is used because macOS AirPlay Receiver occupies port 5000.)
4. Demo login: student / Lab@2026!   (also: admin / Admin#Secure9)
5. Optional: `python test_app.py` runs the automated security tests.

If `python3` is not found, install it with `brew install python` or from python.org.

## Deploy to Vercel (recommended)
1. Push this folder to a GitHub repo.
2. vercel.com > Add New > Project > import the repo > Deploy.
3. Project Settings > Environment Variables: add SECRET_KEY = (any long random string).
4. Redeploy. Done.
(Or CLI: `npm i -g vercel` then `vercel` inside this folder.)

## Netlify
Netlify hosts static sites and JS functions; it does not run Flask apps.
Use Vercel for this project's backend.

## Security features to explain in your report
- Password hashing (Werkzeug PBKDF2/scrypt)
- CSRF token on the login form
- Lockout after 5 failed attempts (5 min)
- Generic error message (no username enumeration) + constant-time hash check
- HttpOnly / SameSite / Secure cookies, 30 min session expiry
- Security headers (CSP, X-Frame-Options, nosniff, no-store)

## Limitations (good for a "future work" section)
Demo users are hardcoded; the lockout list lives in memory (resets on serverless cold start).
A production app would use a database, Redis for rate limiting, MFA, and HTTPS-only cookies.
