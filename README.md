# PAXFUL_API

#### Python Developer Intern Test Assignment

A simple WebAPP for records of Books built based on Restful API Standards

Technology Used:

- Django Rest Framework 3.11

- Django 2.1

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites


#### Step 1


The necessary requirements are having Python 3,pip and git client configured on your machine.


    `git clone https://github.com/abdul0214/PAXFUL_API`


    `cd PAXFUL_API`

#### Step 2    

run following command to create a virtual env

    Linux/macOS `python3 -m venv env --no-site-packages`

    Windows: `py -m venv env`


Then, run the following to activate the virtual

    Linux/macOS : `source env/bin/activate`

    Windows: `.\env\Scripts\activate`

#### Step 3

install all the required packages by running the following command:

    Linux/macOS : `pip install -r requirements.txt`

    Windows: `pip install -r requirements.txt`



Now we are all set to get our application up and running.



## Running App

Run the App using the simple command:

    `python manage.py runserver`


Make sure you have port 8000 available on your PC.

Depending on your combination of Hardware and Software, the following paths may be different. In Most cases, they will be same and hence you can go ahead and use the following links:


1. For getting the entire list of Books currently in the database, use the following URL to get the List of Books in the Database:

   <http://127.0.0.1:8000/api/v1/books/>



A sample response may look as follows: -

`

    {
        "id": 6,
        "title": "A Passage to India"
    },

    {
        "id": 7,
        "title": "One Hundred Years of Solitude"
    },

    {
        "id": 8,
        "title": "Don Quixote"
    },

    {
        "id": 9,
        "title": "Anna Karenina"
    },

    {
        "id": 10,
        "title": "Beloved"
    },
`

 - In case of no Book records in the database,
an empty list will be returned with an __HTTP__ Status code of __204__, indicating absence of content.  -


2.For getting the Book detail of the single Book, in accordance with API Design Standards, we will use the following URL patter where we replace <id> with book id we are interested in getting. :

`http://127.0.0.1:8000/api/v1/books/<book_id>`


Hence for getting Book details of Book with id 2, we use the following URL.



 <http://127.0.0.1:8000/api/v1/books/2/>




 A sample response may look as follows:





    "id": 2,
    "title": "One Hundred Years of Solitude",
    "author": {
        "id": 2,
        "name": "Mr. David Smith"
    }





 - In case of an Book record not existing for
the given book id, following response will be
returned with a status code of
be returned with an __HTTP__ Status code of __404__, indicating absence of requested
content.



`


    "detail": "Not found."




`




In the case of any errors, the exception handling
built into the system will catch the exception
and provide the following response.

`
"An Unexpected error occured, please try again later"`




## Running the tests

Tests are located in the

_PAXFUL_REST/BOOK_REST/tests_


However, they can run directly from the project root folder through the following command:


`

     python manage.py test BOOK_REST


`
There are a total of 6 test cases. Detailed comments on the tests are found inside the relevant .py files.

## Seeding Sample Data into the database

A python script titled 'SampleData_Seeding.py' has been created and placed in PAXFUL_REST Directory. This script seeds artificial sample data into the Database.

Example Usage may be as follows:
  - Example Usage for seeding 10 records(default argument value)

     python SampleData_Seeding.py


  - Example Usage for seeding 10 records(default argument value)

    python SampleData_Seeding.py -delete True


## Notes

The app was developed on a machine with Linux-64 based OS. Although the app has been testes on Windows 10 based machine and works as expected, some errors may be encountered when running on any other OS or different version of Anaconda packages.


Therefore, we specify the main requirements as follows:

    - Anaconda - 4.8.3
    - Python - 3.6
    - Django Rest Framework - 3.11
    - Django 2.1
    - Faker 4.1.1

In case of any unexpected errors, please feel free to contact me on the following e-mail address, I will be available immediately:
  <abdul.wahab@ut.ee>
