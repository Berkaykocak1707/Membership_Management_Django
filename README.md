# Membership_Management_Django

This project is built using Django 4.2.3. It is a web application for membership management with social media integration.

## Getting Started

Navigate to the project folder and install the required dependencies using the following command:
pip install -r requirements.txt


### Basic Settings

- `DEBUG`: True. (It is recommended to set this to `False` in a production environment.)
- `ALLOWED_HOSTS`: Currently empty. Should be populated appropriately when deploying to production.
- `SECRET_KEY`: It's essential to have a secure and unique secret key. It is recommended to change this key when setting up your copy of the project. You can generate a new secret key using third-party services or tools like [Django Secret Key Generator](https://djecrety.ir/).

### Applications

The following Django applications are active in this project:
- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes
- django.contrib.sessions
- django.contrib.messages
- django.contrib.staticfiles
- Membership
- social_django

### Middleware

The project uses the following middleware:
- django.middleware.security.SecurityMiddleware
- django.contrib.sessions.middleware.SessionMiddleware
- django.middleware.common.CommonMiddleware
- django.middleware.csrf.CsrfViewMiddleware
- django.contrib.auth.middleware.AuthenticationMiddleware
- django.contrib.messages.middleware.MessageMiddleware
- django.middleware.clickjacking.XFrameOptionsMiddleware
- social_django.middleware.SocialAuthExceptionMiddleware

### URL Routing

Main URL configuration file: 'Membership_Management_Django.urls'

### Static Files

- URL path for static files: 'static/'

## Running the Application

Navigate to the project folder and start the server using the following command:
python manage.py runserver


### Social Media Login

This project supports user authentication through social media integrations (e.g., Google, Facebook, Twitter, etc.). To enable this feature, you need to obtain the application key (API Key) and secret from the respective social media platform. These credentials should be added to the `settings.py` file.

Example:
```python
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'YOUR_GOOGLE_OAUTH2_KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YOUR_GOOGLE_OAUTH2_SECRET'
You can obtain this information from the developer console of the respective social media platform. Follow the documentation for each platform to understand how to get the application key and secret.
