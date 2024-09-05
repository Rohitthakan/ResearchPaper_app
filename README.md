ResearchPapers_app

Overview

ResearchPapers_app is a simple web application designed to help users search for research papers, view search results, and save specific papers to their personal collection. The application leverages Django for the backend and utilizes HTML, CSS, and Bootstrap for the frontend.

Features

Search Page

Search Input: Enter keywords to search for research papers.
Results Display: View a list of research papers with the following details:
Paper Title
Authors
Publication Year
Citation Count
Save Button: Add papers to your personal collection.

Saved Papers Page

Saved Papers List: View all papers you’ve saved.
Details Display: Shows the same information as the search results.
Remove Option: Remove papers from your collection.
Technologies Used
Backend: Django
Frontend: HTML, CSS, Bootstrap

Installation

Clone the Repository:

git clone https://github.com/Rohitthakan/ResearchPapers_app.git
Navigate to the Project Directory:

cd ResearchPapers_app
Set Up a Virtual Environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

pip freeze > requirements.txt
pip install -r requirements.txt
Run Migrations:

python manage.py makemigrations
python manage.py migrate
Run the Development Server:

python manage.py runserver
Open Your Browser: Navigate to http://127.0.0.1:8000/ to view the application.

Usage

Search Page

Enter keywords in the search input field and press Enter or click the search button.
View search results with details about each paper.
Click "Save" to add a paper to your saved papers list.

Saved Papers Page

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
