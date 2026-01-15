# 🛡️ Web Application Firewall (WAF) Simulator

Web Application Firewall (WAF) Simulator is a cyber-security project that dEemonstrates how modern WAF systems protect web applications by inspecting incoming HTTP requests and blocking malicious payloads. The system detects common web attacks such as SQL Injection, Cross-Site Scripting (XSS), Path Traversal, and Command Injection using a rule-based inspection engine.

This project focuses on defensive (blue-team) security techniques and provides a clear understanding of how input validation and request filtering help prevent web-based attacks. It serves as a strong academic and GitHub portfolio project for students interested in cyber security and secure application development.

---

## 🚀 Features

- Detects and blocks common web attacks:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Path Traversal
  - Command Injection
- Real-time inspection of user input
- Rule-based detection engine
- Security logging for detected attacks
- Simple and interactive Flask-based web interface
- Modular and extensible project structure

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML & CSS
- Rule-based security logic

---

## 📁 Project Structure

# 🛡️ Web Application Firewall (WAF) Simulator

Web Application Firewall (WAF) Simulator is a cyber-security project that demonstrates how modern WAF systems protect web applications by inspecting incoming HTTP requests and blocking malicious payloads. The system detects common web attacks such as SQL Injection, Cross-Site Scripting (XSS), Path Traversal, and Command Injection using a rule-based inspection engine.

This project focuses on defensive (blue-team) security techniques and provides a clear understanding of how input validation and request filtering help prevent web-based attacks. It serves as a strong academic and GitHub portfolio project for students interested in cyber security and secure application development.

---

## 🚀 Features

- Detects and blocks common web attacks:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Path Traversal
  - Command Injection
- Real-time inspection of user input
- Rule-based detection engine
- Security logging for detected attacks
- Simple and interactive Flask-based web interface
- Modular and extensible project structure

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML & CSS
- Rule-based security logic

---

## 📁 Project Structure

waf-simulator/
│
├── app.py
├── waf_engine.py
├── rules.py
├── logger.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css

## ▶️ How to Run the Project

1. Install the required dependency  

pip install flask

2.Start the application

python app.py

3.Open your browser and visit

http://127.0.0.1:5000

🧠 How It Works

1.The user enters a request payload through the web interface

2.The WAF engine analyzes the input using predefined security rules

3.If a malicious pattern is detected, the request is blocked and flagged

4.Attack details are logged for security analysis

5.Safe inputs are allowed and marked as secure

🧪 Sample Test Payloads

| Input Payload               | Result                     |
| --------------------------- | -------------------------- |
| `hello world`               | Safe Request               |
| `<script>alert(1)</script>` | XSS Attack Detected        |
| `' OR '1'='1`               | SQL Injection Detected     |
| `../etc/passwd`             | Path Traversal Detected    |
| `ls && whoami`              | Command Injection Detected |

📌 Use Cases

1.Learning web security fundamentals

2.Understanding Web Application Firewall behavior

3.Cyber-security academic projects

4.Defensive security (blue-team) practice

5.Secure coding demonstrations

👨‍💻 Author

Vishaal S
GitHub: https://github.com/vishaal360

📄 License

This project is licensed under the MIT License
