# Creating My First API

A Basic RESTful API that stores Users Data.

## Install Flask

`pip install flask-restful`


## API Testing Tool

Choose your testing tool. I chose Postman for mine. 

Postman: https://www.getpostman.com/downloads/


## HTTP Requests

The HTTP Requests you can do are listed here:

  - GET - Retrieve a selected user
  - POST - Creating a new user
  - PUT - Update an existing user or create a new one
  - DELETE - Delete a User from the stored data 

## Testing in Postman

First run your program in your Terminal. 

#### Retrieve a User from the stored data
  
  - Select GET, Enter your URL with the name you wish to retrieve ```http://YOUR-URL/user/[NAME]``` 
  - Click on Send
  - The results will be displayed below

#### Create a New User

  - Select POST, and enter the name you wish to add.```http://YOUR-URL/user/[NAME]```
  - On the Headers section add the "age" and "occupation" Keys and their associated Values
  - Click on Send
  
#### Update a User in Postman

  - Select PUT, change the URL to the name you wish to update ```http://YOUR-URL/user/[NAME]```
  - On the Headers section add the "age" and "occupation" Keys and their associated Value
  - Click on Send
  
#### Delete a User

   - Select DELETE, update your URL to the one you wish to remove. ```http://YOUR-URL/user/[NAME]```
   - Click on Send


  
