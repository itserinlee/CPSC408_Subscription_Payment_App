# reference: https://medium.com/@shikhar022/automating-mysql-reports-using-python-1fc3aa8240e7


import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "final_project"
)

cursor = connection.cursor()

def reportForAdmin():
    '''
    queries the database to generate a report for the admin of:
    summary statistics
    could also include the views based on index
    '''

    query = '''
        SELECT category, COUNT(category) AS CountOfCategory, ROUND(AVG(cost), 2) AS AvgCost
        FROM magazine
        GROUP BY category
        ORDER BY AvgCost DESC;
    '''

    columnHeaders = ['category', 'category_count', 'avg_cost']

    cursor.execute(query)
    result = list(cursor.fetchall())
    print(f'{result=}')

    if len(result) != 0:
        df = pd.DataFrame(result, columns=columnHeaders)
        df.to_csv('admin_report.csv', index=False)   


def reportForClient(givenUsername: str):
    '''
    queries the database to generate a report for the customer
    their payments and subscription information
    as well as their current profile information
    but NOT their customer info which contains credentials that should be abstracted away
    '''

    # query = '''
    #         SELECT paymentDate, paymentAmount
    #         FROM payment
    #         ORDER BY paymentDate DESC LIMIT 1;
    # '''

    query = '''
        SELECT firstName, lastName
        FROM customer
        WHERE username = %s
    '''

    # columnHeaders = ['last_payment', 'payment_amount']
    columnHeaders = ['first_name', 'last_name']

    cursor.execute(query, (givenUsername, ))
    result = list(cursor.fetchall())
    print(f'{result=}')

    if len(result) != 0:
        df = pd.DataFrame(result, columns=columnHeaders)
        df.to_csv(f'{username}_report.csv', index=False)

reportForAdmin()
username = input('Enter your username: ')
reportForClient(username)