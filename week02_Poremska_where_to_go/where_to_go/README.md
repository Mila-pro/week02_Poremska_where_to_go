# Where To Go — Django Project

##  How to Run the Project
 **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt

   python manage.py migrate
   
   python manage.py runserver

open in the browser:
http://127.0.0.1:8000/
