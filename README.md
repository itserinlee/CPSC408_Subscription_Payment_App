# Payment Processing App for Magazine Subscriptions
***Database Management - CPSC 408, (Fall 2021)***

*Tarek El-Hajjaoui, Erin Lee, Connor Lydon*


### Summary
This a payment processing console app for magazine subscriptions. The database runs on a cloud instance. Instructions for interacting with the app below.


### Instructions
1. Install pip packages.
```
pip3 install -r requirements.txt
```
2. Run the application.
```
python3 app.py
```


### Source files

***

<dl>
  <dt>app.py</dt>
  <dd>main program</dd>
  <dt>controllers/db_helper.py</dt>
  <dd>database functions</dd>
  <dt>controllers/ui_helper.py</dt>
  <dd>user interface functions</dd>
  <dt>data/ </dt>
  <dd>a directory containing a flat file with individual CSV tables & randomly generated data</dd>
  <dt>generateReport.py</dt>
  <dd>exports data to a CSV depending on what the user selects</dd>
  <dt>meta_info/ </dt>
  <dd>directory containing outline & rubric for the project</dd>
  <dt>models/parser.py</dt>
  <dd>contains the parser for reading through flat files & reading them into the object types</dd>
  <dt>models/db_model.py</dt>
  <dd>the main database interface that works with the MYSQL database</dd>
  <dt>models/record_types.py</dt>
  <dd>the object types that are read into before putting them into the database</dd>  
  <dt>queries/ </dt>
  <dd>directory containing all of the queries that are used in the program</dd>
  <dt>requirements.txt</dt>
  <dd>contains all of the required packages</dd>
  <dt>test.py</dt>
  <dd>contains a function that prints the .env contents</dd>
  <dt>views/ </dt>
  <dd>directory containing the ui & how each user is treated differently</dd>
</dl>

***
