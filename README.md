# Simple Library System

A simple Django-based library system with test classes and an API endpoint.

## Author
**Kennedy Taragon**  
GitHub: [KennedyTaragon](https://github.com/KennedyTaragon)

## Features
- Manage books and related data  
- Basic API endpoint for book data  
- Includes test classes for demonstration  

## Setup
```bash
# Clone the repository
git clone https://github.com/KennedyTaragon/Simple-Libary-System-with-test-classes.git
cd Simple-Libary-System-with-test-classes

# Create virtual environment
python3 -m venv .vas
source .vas/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
