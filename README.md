# Library-System
## A flask library management system

## Stacks used

- HTML
- CSS
- JavaScript
- Bootstrap
- Flask(python framework)
- SQLAlchemy(postgreSQL)
- Flask forms 
- ChartJS


## [Installation](#installation)
## Features

- [Create, Upadate , Read and Delete Books and Members](#crud-operations)
- [Import books from Frappe API](#import-books-from-frappe-api)
- [Issue a book to a member](#issue-a-book)
- [Return a book from a member](#return-a-book)
- [Manage Transactions](#transaction-records)
- [Search book or author](#search-books-and-authors)
- [See reports of top 10 popular books and most paying customers](#reports)

***
## Installation
- Run the command to cole the repository
```sh
  git clone https://github.com/nealwaga/Library-System.git
```
- Install all requirements with
```sh
cd Library-System
pip install -r requirements.txt
```
- Set your secret key in /library/\_\_init\_\_.py file
- for creating a local DB
```sh
python
>>from library import db
>>db.create_all()
```
- run commad to start the server
```sh
flask run
```
***
