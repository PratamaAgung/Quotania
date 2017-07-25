# Quotania
This is a web-based application for sharing quotes

## General Info
Quotania is built with `AngularJS` (version 1.6.4) as the front-end framework and `Flask` (version 0.12.2) as the back-end framework. This application use `PostgreSQL` version 9.5.7 as its database system.

## Setup
### Python Library
This project use `SQLAlchemy` for connection between Flask and PostgreSQL.
### Database Preparation
In the local postgre, create user `admin` with password `12345`. After that, create database with name `quotania` which is accessible by user `admin`.
 
## Run
Run the application by executing command
```
python3 mainApp.py
```
Quotania will launch in localhost on port 2000.

## Milestone
### Implementasi 1
Telah dibuat :
- Raw html + css

Rencana pengerjaan :
- Add AngularJS App
- Push Quote into DB
- Add next and preceding function (for changing quote)
- Add like quote function

### Implementasi 2
Telah dibuat:
- Raw html + css
- Add AngularJS app
- Push Quote into DB

Rencana pengerjaan:
- Add next and preceding function (for changing quote)
- Add like quote function

### Final
Done:
- Raw html + css
- Add AngularJS app
- Push Quote into DB
- Add next and preceding function (for changing quote)
- Add like quote function
