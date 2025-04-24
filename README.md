# **Open-License Media Search Application**
**Overview**
The Open-License Media Search Application is a web-based platform built using Django that allows users to search, browse, and interact with openly-licensed media content. The application integrates with the Openverse API to provide users with access to a vast collection of media, including images and audio, all of which are freely available under open licenses.

This application provides a robust user account management system, a rich media search interface, and follows software engineering best practices, including modularity, containerization, automated testing, and clean code practices.

## **Features**
1. User Account Management
User Registration and Authentication: Secure user registration, login, and authentication using Django’s built-in authentication system.

Manage Recent Searches: Users can save, retrieve, and delete their recent searches to make repeated searches more convenient.

Secure Data Handling: The application ensures secure storage and handling of user data following best practices.

2. Media Search Interface
Integration with Openverse API: Fetch and display media results from Openverse API (https://api.openverse.org/v1/) for openly-licensed media.

Graphical Web Interface: An intuitive and responsive front-end interface to search and browse media.

Advanced Search & Filtering: Ability to filter results by media type, license, creator, and other criteria to refine search results.

Play & Display Media: Users can view or play media content directly within the web interface.

3. Software Engineering Best Practices
Modular & Scalable Architecture: The application follows object-oriented programming (OOP) principles and utilizes design patterns to ensure the codebase is modular and scalable.

Containerization with Docker: The application can be containerized using Docker, making it easy to deploy in any environment.

Automated Build & Deployment: The project includes automated build strategies for seamless deployment and integration.

Automated Testing: The system is equipped with automated tests to ensure stability and reduce bugs.

Clean and Well-Documented Code: The application follows coding best practices, including clear code comments and documentation.

Efficient API Integration: The Openverse API is integrated efficiently, and OAuth 2.0 or other APIs can be added for enhanced functionality.

## **Technologies Used**
Backend: Django (Python)

Frontend: HTML, CSS (Bootstrap), JavaScript (for dynamic elements)

Database: SQLite for local development

Containerization: Docker

API Integration: Openverse API (https://api.openverse.org/v1/) and OAuth 2.0 for Logging with Google and GitHub

Authentication: Django’s built-in authentication system

Testing: Django’s test framework

## **Installation**
**Prerequisites**
Before installing the application, make sure your system meets the following prerequisites:

Python (version 3.12 or higher)

SQLite for local development

Docker (for containerized deployment)

pip (Python package manager)

1. Clone the Repository
Start by cloning the project repository to your local machine:

git clone https://github.com/Hamzaa134/openverse-backend.git

2. Install Dependencies

pip install -r requirements.txt
3. Set Up the Database
Configure the database in the Django settings.

SQLite (default):
4. Apply Database Migrations
Run the following command to apply the database migrations:

python manage.py migrate
This will create the necessary database tables.
5. Run the Development Server
Once all setup steps are complete, start the development server:
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.

## **Testing the Installation**
After completing the installation, test the system to ensure everything is working as expected.

Run Automated Tests:
python manage.py test
or 
python manage.py test search.tests

Once the installation is complete, you can start interacting with the media search interface and explore the functionality.
## **Demonstrating the System**
1. User Account Management
Registration: Users can sign up by providing their username, email, and password. Django handles user authentication securely.

Login: After registration, users can log in to access saved search results and manage their recent searches.

Manage Recent Searches: Users can view and delete recent searches on their profile page.

2. Media Search Interface
Search: Users can enter keywords in the search bar to find media.

Filters: Use advanced filters (type and license) to refine the search results.

Media Display: The system displays images and audio that match the search criteria.

Play Media: Users can play or view media directly within the web interface.
## **Writing New Tests**
Create test files inside the tests/ folder in your app directory.

Use Django’s TestCase class to write tests for your models, views, or forms.

Example unit test for MediaContent model:

from django.test import TestCase
from .models import MediaContent

class MediaContentTestCase(TestCase):
    def test_creation(self):
        media = MediaContent.objects.create(
            title="Sample Media",
            license_type="Public Domain",
            creator="John Doe"
        )
        self.assertEqual(media.title, "Sample Media")
        self.assertEqual(media.license_type, "Public Domain")

## **Extending the System**

The system is designed to be extensible. To add new features:

Create New Views: Add custom views in views.py.Ensure that the new views are linked in urls.py.

Add New Models: Define new models to manage custom media content.

Customize the Frontend: Modify templates in templates/.

## **Containerization with Docker**
The application can be containerized using Docker. This simplifies deployment and ensures that the application runs consistently across different environments.

Build the Docker image:
docker build -t search .
Run the container:
docker run -d -p 8000:8000 search

You can access the application at http://localhost:8000/.


