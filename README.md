# PAXFUL_API

#### Python Developer Intern Test Assignment

A simple WebAPP for records of Books built based on Restful API Standards

Technology Used: 

- Django Rest Framework 3.11

- Django 2.1

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

The necessary requirements are having Anaconda toolkit installed on your machine.

Based on your OS, Anaconda toolkit can be downloaded from the following link:

 <https://www.anaconda.com/products/individual>

Make sure to find the installation instructions and install Anaconda correctly have it added to  PATH environment variable.


Once Anaconda is installed and setup, we need to create an environment and install required packages. This can be done by running the following command in the terminal:

`conda create --name Django --file requirements.txt`

requirements.txt file is located in the root of the repository. 

Once created, activate the environment by running the following command:

`conda activate Django`


We are all set for now. 

Using your CLI navigate to the directory where you want to place your copy of the project using 

`cd <directory_path>`

Then download your copy of the project from GitHub using the following command:


`git clone https://github.com/abdul0214/PAXFUL_API`

OR Download a zipped copy from:

<https://github.com/abdul0214/PAXFUL_API>

 If you downloaded a zipped copy, the unzip it using a tool of your choice.

Once cloned/downloaded, move inside the directory using CLI.

`cd PAXFUL_API/PAXFUL_REST`


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


`

    
    "id": 2,
    "title": "One Hundred Years of Solitude",
    "author": {
        "id": 2,
        "name": "Mr. David Smith"
    }
`




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
There are a total of 6 test cases. Detailed comm
ents on the tests are found inside the relevant .py files.



