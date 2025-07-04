#  Fitness Studio Booking API

This is a simple RESTful API built with Django and Django REST Framework that allows users to:
- View upcoming fitness classes
- Book a spot in a class
- View their own bookings

---

##  Tech Stack

- Python 3.11.4
- Django 5.2.4
- Django REST Framework 3.16.0
- SQLite (default DB)

---

###  features

✅ View all upcoming fitness classes with timezone conversion  
✅ Book a class if slots are available  
✅ View bookings using client email  
✅ Handles overbooking and missing input  
✅ Supports dynamic timezone via `?timezone=` query param

---

#### Setup Instructions

##### 1. Clone the Repository

```bash
git clone https://github.com/Midhunos/fitness_project.git
cd fitness_project

# create virtual envirionment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# install all dependencies
pip install -r requirements.txt

# run all the migrations 
python manage.py makemigrations
python manage.py migrate

# add the seed data and run it
python seed_data.py

# run server
python manage.py runserver

```
###   Endopints
# to fetcth the classes (get)
 /api/classes/?timezone=Asia/Kolkata 

#  to book the slot (post)
 /api/book/

Request Body:
    {
  "class_id": 2,
  "client_name": "Midhun S",
  "client_email": "midhun@gmail.com"
}
 
# to see the bookings (get)

/api/bookings/?email=midhun@gmail.com
