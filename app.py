# """
# Simple Login Web App - Cyber Lab Project
# Stack: Flask (backend) + HTML/Jinja templates (frontend)

# Security features demonstrated:
#   - Password hashing (never store plain-text passwords)
#   - Signed, HttpOnly, SameSite session cookies
#   - CSRF token on the login form
#   - Brute-force protection (lockout after repeated failures)
#   - Generic error messages (no username enumeration)
#   - Security headers (CSP, X-Frame-Options, etc.)
# """

# {% extends "base.html" %}
# {% block title %}Cyber Lab | Security Center{% endblock %}
# {% block body %}

# <style>
# * { box-sizing: border-box; }

# .cyber {
#     min-height: 100vh;
#     background: #081119;
#     color: #e6f3f7;
#     font-family: Arial, sans-serif;
#     padding: 25px;
# }
# .cyber button, .cyber input, .cyber textarea { font: inherit; }
# .cyber button { cursor: pointer; }
# .cyber .layout {
#     max-width: 1350px;
#     margin: auto;
# }
# .cyber .topbar {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     flex-wrap: wrap;
#     gap: 15px;
#     margin-bottom: 30px;
# }
# .cyber .brand {
#     font-size: 26px;
#     font-weight: bold;
#     color: #53e0e6;
# }
# .cyber .sub { color: #93aab8; margin-top: 8px; }
# .cyber .online {
#     background: #103a33;
#     color: #61e6bd;
#     padding: 10px 16px;
#     border-radius: 30px;
# }
# .cyber .grid {
#     display: grid;
#     grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
#     gap: 18px;
# }
# .cyber .panel {
#     background: #111e29;
#     border: 1px solid #233845;
#     border-radius: 14px;
#     padding: 22px;
# }
# .cyber .stat {
#     cursor: pointer;
#     transition: .2s;
# }
# .cyber .stat:hover, .cyber .tool:hover {
#     border-color: #48d5e0;
#     transform: translateY(-3px);
#     box-shadow: 0 0 18px #20b9ca16;
# }
# .cyber .stat h3 {
#     color: #9bb6c3;
#     font-size: 14px;
# }
# .cyber .stat h2 {
#     color: #4ed4de;
#     font-size: 26px;
# }
# .cyber .muted { color: #91a9b7; font-size: 14px; }
# .cyber .section-title { margin: 32px 0 17px; }
# .cyber .tool {
#     cursor: pointer;
#     transition: .2s;
#     min-height: 170px;
# }
# .cyber .tool .emoji { font-size: 30px; }
# .cyber .tool h3 { color: #52d9e1; }
# .cyber .tool p { color: #96acba; line-height: 1.6; font-size: 14px; }
# .cyber .activity-row {
#     border-bottom: 1px solid #233845;
#     padding: 13px 0;
#     color: #b8ccd6;
# }
# .cyber .activity-row:last-child { border: none; }
# .cyber .green { color: #5de5bb; }
# .cyber .btn {
#     background: #24bbc8;
#     color: #061117;
#     border: 0;
#     border-radius: 8px;
#     padding: 11px 16px;
#     font-weight: bold;
# }
# .cyber .btn:hover { background: #62e1e6; }
# .cyber .secondary {
#     background: #233642;
#     color: #d9e8ef;
#     border: 1px solid #344b58;
# }
# .cyber input, .cyber textarea {
#     width: 100%;
#     background: #09141c;
#     border: 1px solid #29414e;
#     border-radius: 8px;
#     padding: 12px;
#     color: white;
#     margin: 8px 0;
# }
# .cyber .toolbox {
#     margin-top: 20px;
#     padding: 20px;
#     background: #111e29;
#     border: 1px solid #233845;
#     border-radius: 12px;
# }
# .cyber .toolbox h2 { color: #53dce5; }
# .cyber .toolbox h3 { margin-top: 0; }
# .cyber .close {
#     float: right;
#     background: #233642;
#     color: white;
#     border: 0;
#     border-radius: 8px;
#     padding: 8px 13px;
# }
# .cyber .output {
#     background: #07121a;
#     padding: 13px;
#     border-radius: 8px;
#     white-space: pre-wrap;
#     overflow-wrap: anywhere;
#     color: #67e1c2;
#     margin-top: 12px;
# }
# .cyber .quiz-option {
#     display: block;
#     width: 100%;
#     text-align: left;
#     background: #172733;
#     color: white;
#     border: 1px solid #304654;
#     padding: 13px;
#     margin: 8px 0;
#     border-radius: 8px;
# }
# .cyber .quiz-option:hover { border-color: #52d9e1; }
# .cyber .footer {
#     text-align: center;
#     color: #718a98;
#     margin-top: 35px;
# }
# @media(max-width:600px) {
#     .cyber { padding: 12px; }
#     .cyber .brand { font-size: 21px; }
# }
# </style>

# <div class="cyber">
# <div class="layout">

#     <header class="topbar">
#         <div>
#             <div class="brand">🛡 CYBER LAB</div>
#             <div class="sub">Security learning &amp; monitoring center</div>
#         </div>
#         <div class="online">● System Online</div>
#     </header>

#     <h2>Welcome, {{ session.get('username', 'Student') }}</h2>
#     <p class="muted">Your cybersecurity learning workspace.</p>

#     <!-- Clickable status cards -->
#     <div class="grid">

#         <div class="panel stat" onclick="showTool('account')">
#             <h3>🔐 Account Status</h3>
#             <h2>Secure</h2>
#             <p class="muted">Click to view session information</p>
#         </div>

#         <div class="panel stat" onclick="showTool('health')">
#             <h3>🖥 Lab Status</h3>
#             <h2>Online</h2>
#             <p class="muted">Click to check lab information</p>
#         </div>

#         <div class="panel stat" onclick="showTool('security')">
#             <h3>🛡 Security Mode</h3>
#             <h2>Protected</h2>
#             <p class="muted">Click to view security details</p>
#         </div>

#         <div class="panel stat" onclick="showTool('account')">
#             <h3>👤 Current User</h3>
#             <h2>{{ session.get('username', 'Student') }}</h2>
#             <p class="muted">Click to view your session</p>
#         </div>

#     </div>

#     <h2 class="section-title">🧪 Cybersecurity Lab Tools</h2>

#     <div class="grid">

#         <div class="panel tool" onclick="showTool('password')">
#             <div class="emoji">🔑</div>
#             <h3>Password Strength Checker</h3>
#             <p>Check password strength and learn how to create stronger passwords.</p>
#         </div>

#         <div class="panel tool" onclick="showTool('network')">
#             <div class="emoji">🌐</div>
#             <h3>Network Security</h3>
#             <p>Explore ports, protocols, network threats and protection.</p>
#         </div>

#         <div class="panel tool" onclick="showTool('phishing')">
#             <div class="emoji">🎣</div>
#             <h3>Phishing Awareness</h3>
#             <p>Test your ability to identify suspicious messages.</p>
#         </div>

#         <div class="panel tool" onclick="showTool('web')">
#             <div class="emoji">🧱</div>
#             <h3>Web Security</h3>
#             <p>Learn about common web vulnerabilities and their prevention.</p>
#         </div>

#         <div class="panel tool" onclick="showTool('encryption')">
#             <div class="emoji">🔒</div>
#             <h3>Encryption Lab</h3>
#             <p>Encrypt and decrypt your own text using AES encryption.</p>
#         </div>

#         <div class="panel tool" onclick="showTool('quiz')">
#             <div class="emoji">🕵️</div>
#             <h3>Cybersecurity Quiz</h3>
#             <p>Answer security questions and test your knowledge.</p>
#         </div>

#     </div>

#     <!-- Dynamic tool panel -->
#     <div id="toolArea" class="toolbox" style="display:none;">
#         <button class="close" onclick="closeTool()">✕ Close</button>
#         <div id="toolContent"></div>
#     </div>

#     <h2 class="section-title">📋 Activity Overview</h2>

#     <div class="panel">
#         <div class="activity-row"><span class="green">●</span> Dashboard loaded</div>
#         <div class="activity-row"><span class="green">●</span> Authenticated user session active</div>
#         <div class="activity-row"><span class="green">●</span> Cyber Lab learning tools available</div>
#         <div class="activity-row"><span class="green">●</span> Browser-based security tools ready</div>
#     </div>

#     <div class="footer">
#         Cyber Lab | Educational Cybersecurity Project
#         <br><br>
#         <form action="{{ url_for('logout') }}" method="POST">
#             <button class="btn" type="submit">🚪 Sign Out</button>
#         </form>
#     </div>

# </div>
# </div>

# <script>
# const area = document.getElementById("toolArea");
# const content = document.getElementById("toolContent");

# function showTool(name) {
#     area.style.display = "block";
#     area.scrollIntoView({behavior:"smooth", block:"start"});

#     const tools = {

#     account: `
#         <h2>👤 Account & Session</h2>
#         <p>Username: <b>{{ session.get('username', 'Student') }}</b></p>
#         <p>Authentication: <span class="green">Session active</span></p>
#         <p>This demo confirms that you have reached the dashboard
#         through your login flow. It does not independently verify
#         your account security.</p>
#     `,

#     health: `
#         <h2>🖥 Lab Status</h2>
#         <h3 class="green">Application interface loaded</h3>
#         <p>This dashboard is running in your browser.</p>
#         <p>Deployment: Vercel</p>
#         <p>Backend: Flask</p>
#         <p>Current page: Dashboard</p>
#         <p>Note: This is a UI status, not a live server health check.</p>
#     `,

#     security: `
#         <h2>🛡 Security Information</h2>
#         <p>Login authentication is used to access this dashboard.</p>
#         <ul>
#             <li>Use unique passwords.</li>
#             <li>Never share credentials.</li>
#             <li>Always sign out on shared devices.</li>
#             <li>Use HTTPS websites for sensitive information.</li>
#         </ul>
#     `,

#     password: `
#         <h2>🔑 Password Strength Checker</h2>
#         <p>Enter a sample password to evaluate it locally.</p>
#         <input id="pwInput" type="password" placeholder="Enter a sample password">
#         <button class="btn" onclick="checkPassword()">Check Strength</button>
#         <div id="pwResult" class="output">Result will appear here.</div>
#         <p class="muted">Do not enter your real password. This tool is a basic educational checker.</p>
#     `,

#     network: `
#         <h2>🌐 Network Security Learning</h2>
#         <h3>Common network protocols</h3>
#         <ul>
#             <li><b>HTTP:</b> Web communication, usually unencrypted.</li>
#             <li><b>HTTPS:</b> Encrypted web communication using TLS.</li>
#             <li><b>DNS:</b> Resolves domain names into IP addresses.</li>
#             <li><b>SSH:</b> Secure remote access to systems.</li>
#             <li><b>TCP:</b> Reliable connection-based communication.</li>
#         </ul>
#         <h3>Security practices</h3>
#         <p>Use firewalls, update devices, secure Wi-Fi and avoid
#         unknown network connections.</p>
#     `,

#     phishing: `
#         <h2>🎣 Phishing Awareness Simulator</h2>
#         <p>Read the sample message:</p>
#         <div class="output">
#         URGENT! Your bank account will be blocked today.
#         Click this unknown link immediately and enter your password!
#         </div>
#         <p>What should you do?</p>
#         <button class="quiz-option" onclick="phishAnswer(false)">
#             A. Click the link immediately
#         </button>
#         <button class="quiz-option" onclick="phishAnswer(true)">
#             B. Verify through the bank's official website or app
#         </button>
#         <button class="quiz-option" onclick="phishAnswer(false)">
#             C. Share your password with the sender
#         </button>
#         <div id="phishResult" class="output"></div>
#     `,

#     web: `
#         <h2>🧱 Web Security Learning</h2>
#         <h3>Common vulnerabilities</h3>
#         <ul>
#             <li><b>SQL Injection:</b> Unsafe input affecting database queries.</li>
#             <li><b>XSS:</b> Malicious script injection into webpages.</li>
#             <li><b>CSRF:</b> Tricking a logged-in browser into unwanted actions.</li>
#             <li><b>Weak authentication:</b> Poorly protected login systems.</li>
#         </ul>
#         <h3>Prevention</h3>
#         <ul>
#             <li>Parameterized database queries.</li>
#             <li>Input validation and output encoding.</li>
#             <li>CSRF protection.</li>
#             <li>Strong password hashing.</li>
#         </ul>
#     `,

#     encryption: `
#         <h2>🔒 Encryption Lab — AES-GCM</h2>
#         <p>Type a message and a passphrase. This demo encrypts it in your browser.</p>
#         <textarea id="plainText" rows="3" placeholder="Enter text to encrypt"></textarea>
#         <input id="cryptoPass" type="password" placeholder="Enter encryption passphrase">
#         <button class="btn" onclick="encryptText()">Encrypt</button>
#         <div id="cryptoResult" class="output">Encrypted output will appear here.</div>
#         <p class="muted">The encrypted result can be decrypted below using the same passphrase.</p>
#         <textarea id="cipherText" rows="4" placeholder="Paste encrypted output here to decrypt"></textarea>
#         <input id="decryptPass" type="password" placeholder="Passphrase for decryption">
#         <button class="btn" onclick="decryptText()">Decrypt</button>
#         <div id="decryptResult" class="output">Decrypted text will appear here.</div>
#     `,

#     quiz: `
#         <h2>🕵️ Cybersecurity Quiz</h2>
#         <h3>Question 1: Which of the following is the safest action when you receive an unexpected email attachment?</h3>
#         <button class="quiz-option" onclick="quizAnswer(false)">A. Open it immediately</button>
#         <button class="quiz-option" onclick="quizAnswer(true)">B. Verify the sender and scan it before opening</button>
#         <button class="quiz-option" onclick="quizAnswer(false)">C. Forward it to everyone</button>
#         <div id="quizResult" class="output"></div>
#     `
#     };

#     content.innerHTML = tools[name] || "<h2>Tool not found</h2>";
# }

# function closeTool() {
#     area.style.display = "none";
#     content.innerHTML = "";
# }

# function checkPassword() {
#     const p = document.getElementById("pwInput").value;
#     let score = 0;
#     if (p.length >= 8) score++;
#     if (p.length >= 12) score++;
#     if (/[A-Z]/.test(p)) score++;
#     if (/[a-z]/.test(p)) score++;
#     if (/[0-9]/.test(p)) score++;
#     if (/[^A-Za-z0-9]/.test(p)) score++;

#     let result = "Weak";
#     if (score >= 5) result = "Strong";
#     else if (score >= 3) result = "Moderate";

#     document.getElementById("pwResult").textContent =
#         "Strength: " + result + " | Score: " + score + "/6";
# }

# function phishAnswer(correct) {
#     document.getElementById("phishResult").textContent = correct
#         ? "Correct! Verify suspicious messages through official channels. Never click urgent unknown links."
#         : "Incorrect. Urgent messages asking you to click links or share credentials are warning signs.";
# }

# function quizAnswer(correct) {
#     document.getElementById("quizResult").textContent = correct
#         ? "Correct! Verify the sender and scan suspicious attachments before opening."
#         : "Not safe. Unexpected attachments should be verified before opening.";
# }

# // AES-GCM encryption using a passphrase-derived key
# async function deriveKey(passphrase, salt) {
#     const encoder = new TextEncoder();
#     const material = await crypto.subtle.importKey(
#         "raw", encoder.encode(passphrase), "PBKDF2", false, ["deriveKey"]
#     );

#     return crypto.subtle.deriveKey(
#         {
#             name: "PBKDF2",
#             salt: salt,
#             iterations: 150000,
#             hash: "SHA-256"
#         },
#         material,
#         { name: "AES-GCM", length: 256 },
#         false,
#         ["encrypt", "decrypt"]
#     );
# }

# function toBase64(buffer) {
#     const bytes = new Uint8Array(buffer);
#     let binary = "";
#     for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
#     return btoa(binary);
# }

# function fromBase64(text) {
#     return Uint8Array.from(atob(text), c => c.charCodeAt(0));
# }

# async function encryptText() {
#     const text = document.getElementById("plainText").value;
#     const pass = document.getElementById("cryptoPass").value;
#     const result = document.getElementById("cryptoResult");

#     if (!text || !pass) {
#         result.textContent = "Please enter both a message and a passphrase.";
#         return;
#     }

#     try {
#         const salt = crypto.getRandomValues(new Uint8Array(16));
#         const iv = crypto.getRandomValues(new Uint8Array(12));
#         const key = await deriveKey(pass, salt);

#         const encrypted = await crypto.subtle.encrypt(
#             { name: "AES-GCM", iv: iv },
#             key,
#             new TextEncoder().encode(text)
#         );

#         const packageText = [
#             toBase64(salt),
#             toBase64(iv),
#             toBase64(encrypted)
#         ].join(".");

#         result.textContent = packageText;
#         document.getElementById("cipherText").value = packageText;
#     } catch (e) {
#         result.textContent = "Encryption failed. Use the deployed HTTPS site.";
#     }
# }

# async function decryptText() {
#     const packageText = document.getElementById("cipherText").value.trim();
#     const pass = document.getElementById("decryptPass").value;
#     const result = document.getElementById("decryptResult");

#     if (!packageText || !pass) {
#         result.textContent = "Enter the encrypted text and passphrase.";
#         return;
#     }

#     try {
#         const parts = packageText.split(".");
#         if (parts.length !== 3) throw new Error("Invalid format");

#         const salt = fromBase64(parts[0]);
#         const iv = fromBase64(parts[1]);
#         const ciphertext = fromBase64(parts[2]);
#         const key = await deriveKey(pass, salt);

#         const decrypted = await crypto.subtle.decrypt(
#             { name: "AES-GCM", iv: iv },
#             key,
#             ciphertext
#         );

#         result.textContent = new TextDecoder().decode(decrypted);
#     } catch (e) {
#         result.textContent = "Decryption failed. Wrong passphrase or invalid encrypted text.";
#     }
# }
# </script>

# {% endblock %}




import os
import time
import secrets

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Session security settings
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False  # True when deployed with HTTPS

# Demo credentials
USERNAME = "student"
PASSWORD_HASH = generate_password_hash("Lab@2026!")

# Simple login attempt protection
login_attempts = {}
MAX_ATTEMPTS = 5
LOCK_TIME = 60  # seconds


@app.before_request
def security_headers():
    pass


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        csrf_form = request.form.get("csrf")
        csrf_session = session.get("csrf")

        # CSRF validation
        if not csrf_form or csrf_form != csrf_session:
            error = "Invalid request. Please refresh and try again."

        else:
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            ip = request.remote_addr or "unknown"
            now = time.time()

            attempts = login_attempts.get(ip, {"count": 0, "locked_until": 0})

            if now < attempts["locked_until"]:
                error = "Too many attempts. Please wait before trying again."

            elif username == USERNAME and check_password_hash(PASSWORD_HASH, password):
                session.clear()
                session["username"] = username
                session["csrf"] = secrets.token_hex(32)
                login_attempts.pop(ip, None)
                return redirect(url_for("dashboard"))

            else:
                attempts["count"] += 1

                if attempts["count"] >= MAX_ATTEMPTS:
                    attempts["locked_until"] = now + LOCK_TIME
                    attempts["count"] = 0

                login_attempts[ip] = attempts
                error = "Invalid username or password."

    # Generate CSRF token for the login form
    if "csrf" not in session:
        session["csrf"] = secrets.token_hex(32)

    return render_template("login.html", error=error, csrf=session["csrf"])


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        user=session["username"]
    )


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
