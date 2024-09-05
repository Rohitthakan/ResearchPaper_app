ResearchPapers_app
Overview
ResearchPapers_app is a simple web application that allows users to search for research papers, view search results, and save specific papers to their personal collection. The application uses Django for the backend and HTML, CSS, Bootstrap for the frontend.

Features
Search Page:

Input field for entering keywords to search for research papers.
Display of research papers with details including:
Paper Title
Authors
Publication Year
Citation Count
"Save" button to add papers to the user's collection.

Saved Papers Page:

View the list of saved papers.
Display the same details as the search results.
Option to remove papers from the collection.

Technologies Used
Backend: Django
Frontend: HTML, CSS, Bootstrap

Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/Rohitthakan/ResearchPapers_app.git

Navigate to the Project Directory:

bash
Copy code
cd ResearchPapers_app
Set Up a Virtual Environment (recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies:

bash
Copy code
pip freeze > requirements.txt
pip install -r requirements.txt

Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate

Run the Development Server:

bash
Copy code
python manage.py runserver
Open Your Browser: Navigate to http://127.0.0.1:8000/ to view the application.

Usage
Search Page:

Enter keywords in the search input field and press Enter or click the search button.
View search results with details about each paper.
Click "Save" to add a paper to your saved papers list.

Saved Papers Page:

Access the saved papers page to view all saved papers.
Click "Remove" to delete papers from your collection.
Project Structure
researchpapers/: Main Django application directory

migrations/: Migration files
static/: Static files (CSS)
templates/: HTML templates
views.py: Django views
urls.py: URL routing
models.py: Django models 
