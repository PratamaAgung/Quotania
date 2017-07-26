# Quotania
This is a web-based application for sharing quotes

## General Info
Quotania is built with `AngularJS` (version 1.6.4) as the front-end framework and `Flask` (version 0.12.2) as the back-end framework. This application use `PostgreSQL` version 9.5.7 as its database system.

## Setup
### Python Library
This project use `SQLAlchemy` for connection between Flask and PostgreSQL.
### Database Preparation
In the local postgre, create user `admin` with password `12345`. After that, create database with name `quotania` which is accessible by user `admin`.
### Unit Test
For unit test, we use separate database from the database used in the main application. Create database named `testdb` which is still accessible by user `admin`. Make sure the database is empty before executing unittest.
 
## Run
Run the application by executing command
```
python3 mainApp.py
```
Quotania will launch in localhost on port 2000.

Run unit test by executing command
```
python3 testApp.py
```

## Milestone
### Implementation 1
Done:
- Raw html + css

To be done:
- Add AngularJS App
- Push Quote into DB
- Add next and preceding function (for changing quote)
- Add like quote function
- Add unittest

### Implementation 2
Done:
- Raw html + css
- Add AngularJS app
- Push Quote into DB

To be done:
- Add next and preceding function (for changing quote)
- Add like quote function
- Add unittest

### Final
Done:
- Raw html + css
- Add AngularJS app
- Push Quote into DB
- Add next and preceding function (for changing quote)
- Add like quote function
- Add unittest