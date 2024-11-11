# Healthcare Website Project

This project is a healthcare web application built with Django, providing an intuitive interface for users to access various healthcare services, make appointments, and contact the clinic. The project is modular, with reusable templates and organized structure, following Django best practices.

## Folder Structure

```plaintext
HealthcareWebsite/            # Root project directory
├── .gitignore                # Specifies files to be ignored by version control
├── manage.py                 # Django's command-line utility for administrative tasks
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation for the project
├── .env                      # Environment variables file (excluded from version control)
├── db.sqlite3                # Database file (if using SQLite)
├── my_django_project/        # Main project folder (contains settings and main config files)
│   ├── __init__.py
│   ├── asgi.py               # ASGI entry-point for asynchronous applications
│   ├── settings.py           # Django settings file
│   ├── urls.py               # Main URL declarations for the project
│   └── wsgi.py               # WSGI entry-point for serving the application
│
├── apps/                     # Directory for custom applications
│   └── clinicapp/            # Application folder
│       ├── __init__.py
│       ├── admin.py          # Admin configuration for clinicapp
│       ├── apps.py           # App configuration
│       ├── models.py         # Database models
│       ├── tests.py          # Unit tests
│       ├── views.py          # Views handling HTTP requests
│       ├── urls.py           # URL routing for clinicapp
│       ├── forms.py          # Forms for handling user input (optional)
│       ├── signals.py        # Signal handlers (optional)
│       └── migrations/       # Database migrations
│           └── __init__.py
│
├── templates/                # HTML templates for the project
│   ├── base.html             # Base layout template
│   └── clinicapp/            # Templates specific to clinicapp
│       ├── about.html
│       ├── appointment.html
│       ├── contact.html
│       ├── feature.html
│       ├── index.html
│       ├── service.html
│       ├── team.html
│       ├── testimonial.html
│       └── 404.html          # Custom 404 error page
│
├── static/                   # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                    # User-uploaded files
│   └── uploads/
│
├── staticfiles/              # Collected static files for deployment
│   └── ...
└── docs/                     # Additional project documentation (optional)
```

## Features

- **Appointment Scheduling**: Users can easily schedule appointments with the healthcare center.
- **Service Information**: Detailed pages about various medical services offered, such as Cardiology, Neurology, etc.
- **Contact Form**: A contact form for users to send inquiries.
- **Team Information**: A section to display information about the healthcare team.
- **Testimonials**: A section for patient reviews and testimonials.
- **Custom Error Handling**: A custom 404 error page for a better user experience.

## Tech Stack

- **Backend**: Django (Python) for handling server-side operations.
- **Frontend**: HTML, CSS, and JavaScript for structure and styling.
- **Database**: SQLite for local development; can be switched to PostgreSQL or MySQL for production.
- **Deployment**: Configured for production with ASGI and WSGI settings, and uses collectstatic for managing static files.

## Setup and Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/OumaCavin/healthcare-website.git
   cd healthcare-website
   ```

2. **Create a Virtual Environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**  
   Create a `.env` file in the root directory to store sensitive information like database credentials and secret keys. This file should be added to `.gitignore`.

5. **Run Migrations**  
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

8. **Access the Website**  
   Open your browser and go to `http://127.0.0.1:8000` to view the website.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please follow coding standards and write clear documentation for new features.

## Acknowledgements

- Django documentation for providing guidance on the project setup and configuration.
- Bootstrap for the front-end framework and styling.
- FontAwesome for social media icons.
- Any other libraries or resources used.

## Future Features

- **User Authentication**: Add login, registration, and profile management features.
- **Appointment Reminders**: Implement email or SMS reminders for upcoming appointments.
- **Payment Integration**: Integrate payment options for paid services.
- **Blog Section**: Provide health-related articles and updates.
- **API Integration**: Add API endpoints to allow third-party integrations or mobile app support.

## Running Tests

To run tests, use the following command:
```bash
python manage.py test clinicapp
```

## Deployment

For production deployment:
1. Set `DEBUG = False` in `settings.py`.
2. Configure static files:
   ```bash
   python manage.py collectstatic
   ```
3. Set up a production-ready web server, such as Gunicorn with Nginx.

## License

This project is licensed under the MIT License.

