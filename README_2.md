# Steps to create a Django Project

1. Creade a folder for the new project
2. Open VS code and a terminal at that project
3. Create a Virtual Environment
   - Mac: Python3 - m venv venv

4 Activate the venv - Mac: source venv/bin/activate

5 Install the required dependencies - Both OS: pip instal django (pip3, if your on MAC)

6. Create the django project (One time use Command)

- Both OS: django-admin startproject NAME_FOLDER .
  Expectation is: config folder, venv and manage.py file

7. Update setting.py recongnize **_static_** and **_template_** path

7.1 - Inside static create folders js., CSS, and images

8. Add miscs: .gitignore, README.md

9. To generate the requirement.xtx file:
   - Both: Pip freeze > requirement.txt (pip3 on Mac)
