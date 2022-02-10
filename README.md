# Screenshots

There will be screenshots of our Vet App.

### Register

![Register](/screenshots/Register.png)

### Login

![Login](/screenshots/Login.png)

### Create Pet

![CreatePet](/screenshots/CreatePet.png)

### Create Owner

![CreateOwner](/screenshots/CreateOwner.png)

### Create Match

![CreateMatch](/screenshots/Match.png)

### Matched Home

The section that pointed with an arrow shows that only authorized people could see that section.
![MatchedHome](/screenshots/MatchedHome.png)

### Update Pet

![UpdatePet](/screenshots/UpdatePet.png)

### Update Owner

![Update Owner](/screenshots/UpdateOwner.png)

### Updated Non Registered Home

Updated home page for daily non registered users.
![UpdatedHome](/screenshots/NonStaffHome.png)

### Updated Regular User Home Page

Updated home page for regular users.
![UpdatedUserHome](/screenshots/RegularHome.png)

# About

A vet application built with Django. Either could be used for normal web page or store the data.

# Installation
Change your directory to where u want to clone this repository with CD commands and;
```git
https://github.com/obdagli/VeterinerWebsite.git
```
Create a virtualenv to use our requirements like a storage, also creating a virtualenv provides us independency about our system.
```python
python -m venv env
source env/bin/activate #for windows its: env\Scripts\activate
```
Install the requirements:
```git
pip install -r requirements.txt
```
Migrate to create sqlite3
```python
python manage.py migrate
```
To run server:
```git
python manage.py runserver
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
