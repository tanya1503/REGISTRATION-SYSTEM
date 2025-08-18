# 📝 Registration System (Django)

A web application built with **Django** that enables **signup and login functionality** for different types of users — **Patients** and **Doctors**. Upon successful login, users are redirected to their respective dashboards displaying their registered details.

---

## 📌 Features

- 🔑 **User Authentication** (Signup, Login, Logout)  
- 👨‍⚕️ **Role-based Access** (Doctor & Patient dashboards)  
- 🖼️ **Profile Picture Upload** during registration  
- 📍 **Address Fields** (line1, city, state, pincode)  
- ✅ **Password Validation** (password & confirm password check)  
- 🖥️ **User Dashboards** displaying signup details  
- 📂 Built using **Django’s authentication system**

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanya1503/REGISTRATION-SYSTEM.git
   cd REGISTRATION-SYSTEM

2. **Create virtual environment & activate**
   ```bash
   python -m venv env
   env\Scripts\activate     # On Windows
   source env/bin/activate  # On Mac/Linux
   
3. **Install dependencies**
   ```bash
   pip install django

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Start the development server**
   ```bash
   python manage.py runserver

6. **Access the app**  
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 🏥 Types of Users  

### 👤 Patient  
- Registers with personal details, profile picture, and address.  
- Redirected to **Patient Dashboard** after login.  

### 👨‍⚕️ Doctor  
- Registers with personal details, profile picture, and address.  
- Redirected to **Doctor Dashboard** after login.

## 📋 Signup Form Fields  

- First Name  
- Last Name  
- Profile Picture  
- Username  
- Email ID  
- Password  
- Confirm Password  
- Address (Line1, City, State, Pincode)  

✅ Includes validation to ensure **passwords match**.  

<details>
<summary>Click to expand</summary>

```text
registration/  
│── app1/                 # Main Django app  
│   ├── templates/         # HTML templates (signup, login, dashboard)  
│   ├── views.py           # Business logic  
│   ├── models.py          # User models  
│   ├── urls.py            # App routes  
│── registration/          # Project settings  
│── db.sqlite3             # Database  
│── manage.py
</details>


 Tech Stack 

- **Backend**: Django  
- **Database**: SQLite (default)  
- **Frontend**: HTML, CSS (Django Templates), Bootstrap  
- **Language**: Python  










