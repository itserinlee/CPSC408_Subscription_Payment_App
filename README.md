# Python_SQL_MagazineApp
Tarek El-Hajjaoui, Erin Lee, Connor Lydon


# summary
supplied is our program for interacting with our Magazine Subscription Database. It is already initialized and set up to run on the cloud instance. Follow the instructions below 


# to use

1. pip3 install -r requirements.txt
2. python3 app.py


server credentials are already hard coded, but capability exists to use a more secure .env style.

if running the program for the first time in a local or cloud environment, set the first boolean in the DB_Model to true to build the tables.

the second boolean indicates if this will run on a server instance or not. it is preset for a server instance.

# references

referenced previous code, notes and slides from class.


# files included
app.py -- main program
controllers/db_helper -- miscellaneous database functions
controllers/ui_helper -- miscellaneous user interface functions
data/ -- this is a directory contains a flat file with all the info and individual CSV tables, this also includes randomly generated data
generateReport.py -- this exports the data to a CSV depending on what the user selects
meta_info/ -- contains outline and rubric for the project
models/parser.py -- this contains the parser for reading through flat files and reading them into the object types
models/db_model.py -- this is the main database interface that works with the MYSQL database
models/record_types -- these are the object types that are read into before putting them into the database
queries/ -- this contains all of the queries that are used in the program
requirements.txt -- this contains all of the required packages
test.py -- this is a function that prints the .env contents
views/ -- this contains the ui and how each user is treated differently
