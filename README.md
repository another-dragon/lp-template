```markdown
# HTMX SPLASH Page SJM

A Django + HTMX splash page designed for Airbnb rental guests to access the WiFi network after providing their First Name, Last Name, and Email, and to collect consent for marketing and advertisement purposes (e.g., newsletters). The form includes validation and, upon successful submission, redirects the user to a home page with the title "You are connected". Tailwind CSS is used for styling to ensure a modern and responsive design that mimics Airbnb's aesthetic.

## Overview

The application is built using Django as the backend framework, with HTMX for handling dynamic content updates without a full page reload. Tailwind CSS is used for styling to create a familiar and user-friendly interface. The main functionality includes a splash page where users can enter their personal details to gain access to the WiFi network. This form is validated to ensure all fields are correctly filled out. Upon successful submission, the user is redirected to a home page confirming their connection. The backend handles storing user data and consent for marketing purposes.

### Project Structure

- **htmx_splash/**: Contains the main Django project settings and configuration files.
  - `__init__.py`
  - `asgi.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`
- **splash/**: Contains the application-specific files.
  - `forms.py`
  - `models.py`
  - `templates/splash/`
    - `form_errors.html`
    - `splash_page.html`
    - `home_page.html`
  - `urls.py`
  - `views.py`
  - `migrations/`
    - `0001_initial.py`
    - `__init__.py`
- **Dockerfile**: Defines the environment setup for running the application using Docker.
- **docker-compose.yml**: Defines the Docker Compose configuration for the web and database services.
- **.env**: Contains configuration settings for the project.
- **.gitignore**: Specifies patterns to ignore when tracking files in Git.
- **manage.py**: Django's command-line utility for administrative tasks.
- **requirements.txt**: Lists the dependencies required for the project.

## Features

- **User Authentication**: Guests can enter their First Name, Last Name, and Email to access the WiFi network.
- **Form Validation**: Ensures that all fields are correctly filled out before submission.
- **Marketing Consent**: Collects user consent for marketing and advertisement purposes.
- **Dynamic Content Updates**: Uses HTMX to handle form submission and validation without a full page reload.
- **Responsive Design**: Uses Tailwind CSS to create a modern and responsive design that mimics Airbnb's aesthetic.
- **Data Storage**: Stores user data and consent information in a PostgreSQL database.

## Getting Started

### Requirements

- Python
- Docker
- Docker Compose

### Quickstart

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd htmx_splash
   ```

2. **Create and configure the `.env` file**:
   ```sh
   cp .env.example .env
   # Update the .env file with your configuration settings
   ```

3. **Build and run the Docker containers**:
   ```sh
   docker-compose up --build
   ```

4. **Apply database migrations**:
   ```sh
   docker-compose exec web python manage.py migrate
   ```

5. **Access the application**:
   Open your web browser and navigate to `http://localhost:8000`.

### License

The project is proprietary (not open source). Copyright (c) 2024.
```