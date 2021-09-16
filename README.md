# Notes
This web-service serves in order to take notes store them and share with other people (if you wish ofc)

# Preview 

<img src="project_details/notes-gf.gif" border="10" width = 500 align=center ></a>


# Tech stack

<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/64/000000/python.png">
<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/django.png">
<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/64/000000/html-5.png">
<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/css3.png">
<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/bootstrap.png">

<br>

# Installation

1. Clone repository.
 
2. Create virtual environment and activate it.
    
    `python3 -m venv name_of_venv` 

3. Install requirements from the file. 

    `pip install -r requirements.txt`

4. Fill .env_sample with required data and rename the file to .env.

5. Make migrations `python manage.py makemigrations`  and make migrate. `python manage.py migrate`

6. Run the server. `pyton manage.py runserver` 


# Implemented
* CRUD functions for notes
* User Registration / Authentication system
* Password change / reset
* Like notes feature
* Tree strucure comment section (Mptt)
* Hide private notes
* Profile settings
* Filtering by tags
