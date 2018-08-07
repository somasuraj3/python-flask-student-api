# Student Information Management API

# Setup :

1. Install Python 3.4

2. Install pip

3. Install pipenv
    command: pip install --user pipenv

4. Install dependencies
    command: pipenv install

5. Run the application
    command: pipenv run python app.py


# API Documentation

# Method        Resource            Description             Request Body Example
1  GET           /students          Gets all students       NA
2  GET           /students/{id}     Gets requested student  NA
3  POST          /students          Adds student            sid=4, name="Student Name"
4  PUT           /students/{id}     Updates student         name="Student Name"
5  DELETE        /students/{id}     Deletes student         NA