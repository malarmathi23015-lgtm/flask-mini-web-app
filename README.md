# 🔐 Secure Notes Flask App

A modern and secure note-taking web application built using Flask.

This project includes user authentication, password hashing, CRUD note management, Bootstrap dark UI, Flask-Login session handling, and SQLite database integration.

---

# 🚀 Features

## Authentication System

- User Registration
- User Login
- Logout System
- Session Authentication
- Password Hashing
- CSRF Protection

---

## Notes System

- Create Notes
- Edit Notes
- Delete Notes
- View Notes
- User-Specific Notes
- Search Notes

---

## Security Features

- Flask-Login Protection
- Password Hashing using Werkzeug
- Protected Routes
- User Ownership Validation
- CSRF Security

---

## UI Features

- Bootstrap 5 Responsive Design
- Dark Theme UI
- Dashboard Interface
- Flash Messages
- Responsive Layout

---

# 🛠 Technologies Used

- Python
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Bootstrap 5
- HTML5
- CSS3
- JavaScript

---

# 📁 Project Structure

```text
secure_notes/
│
├── app/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── create_note.html
│   │   ├── edit_note.html
│   │   ├── view_note.html
│   │   └── profile.html
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── note.py
│   │
│   ├── __init__.py
│   ├── auth.py
│   ├── forms.py
│   └── extensions.py
│
├── migrations/
├── instance/
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
'''
## ⚙️ Installation
Clone Repository
git clone https://github.com/YOUR_USERNAME/secure-notes-flask.git

Navigate Into Project
cd secure-notes-flask

Create Virtual Environment
python -m venv venv

Activate Virtual Environment
Linux / macOS
source venv/bin/activate

Windows
venv\\Scripts\\activate

Install Requirements
pip install -r requirements.txt

🗄 Database Setup
Initialize Migration
flask db init
Create Migration
flask db migrate -m "Initial migration"
Apply Migration
flask db upgrade

▶️ Run Application
flask --app run.py --debug run

Application runs on:
http://127.0.0.1:5000

🔮 Future Improvements
Rich Text Editor
Markdown Support
Note Categories
Public/Private Notes
Email Verification
Password Reset
REST API
Docker Deployment

📚 Learning Outcomes

This project demonstrates:

Flask Authentication
Flask Application Structure
SQLAlchemy ORM
Flask-WTF Forms
Database Relationships
CRUD Operations
Session Management
Secure Password Handling
Responsive UI Design

👨‍💻 Author

Developed by Mathivadhana V give this atfer installation ggive out project structure
