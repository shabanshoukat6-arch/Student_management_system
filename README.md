# Student Management System

A web-based Student Management System developed using Python and Django. This project uses Django Forms to collect, validate, and manage student information.

## Features

- Add new student records using Django Forms.
- View all student records on the dashboard.
- Edit existing student information.
- Delete student records (if implemented).
- Validate form data before saving.
- Store student information in an SQLite database.
- Display success messages after form submission.
- Use HTML and CSS for the user interface.
- Manage student records through Django Admin.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Forms:** Django ModelForm
- **Template Engine:** Django Template Language (DTL)

## Student Information

The system manages the following student details:

- Name
- Age
- Roll Number
- Gender
- Email
- Department
- Created At

## Project Setup

### 1. Clone or Download the Project

Download the project or clone its repository, then open the project folder in VS Code.

### 2. Create a Virtual Environment

```bash
virtualenv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\scripts\activate
```

### 4. Install Django

```bash
pip install django
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin Account (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

## How Django Forms Work

The project uses Django ModelForm to connect the student form with the database model.

1. The form displays student input fields.
2. The user enters student information.
3. Django validates the submitted data.
4. Valid data is saved to the database.
5. The user is redirected to the dashboard or receives a success message.
6. Invalid data is displayed with validation errors.

## Django Admin Panel

The Django Admin Panel can be used to manage student records.

URL:

http://127.0.0.1:8000/admin/

Create a superuser before accessing the admin panel.

## Future Improvements

- Search students by name or roll number.
- Add pagination to the student list.
- Add authentication and user permissions.
- Improve responsive design.
- Add export functionality for student records.

## Author

**Muhammad Shaban Shoukat**

## License

This project is intended for educational and learning purposes.
