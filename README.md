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

📁 Project Structure

secure-notes/
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

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/secure-notes-flask.git

2️⃣ Navigate to Project
cd secure-notes-flask

3️⃣ Create Virtual Environment
python -m venv venv

4️⃣ Activate Virtual Environment
Linux / macOS
source venv/bin/activate

Windows
venv\Scripts\activate

5️⃣ Install Dependencies
pip install -r requirements.txt
🗄 Database Setup
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

▶️ Run Application
flask --app run.py --debug run

Open in browser:
http://127.0.0.1:5000

🔮 Future Improvements
Rich Text Editor
Markdown Support
Public/Private Notes
Email Verification
Password Reset System
REST API Integration
Docker Deployment

📚 Learning Outcomes
This project demonstrates:
      Flask Authentication Flow
      SQLAlchemy ORM Design
      Secure Password Handling
      Flask-WTF Forms
      CRUD Operations
      Session Management
      Modular Flask Architecture
      Responsive UI Design

👨‍💻 Author

Developed by: Mathivadhana V
