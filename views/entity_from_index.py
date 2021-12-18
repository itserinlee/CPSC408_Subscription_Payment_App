import mysql.connector


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "final_project"
)

cursor = connection.cursor()


def magazine():

    cursor.execute('''DROP VIEW IF EXISTS magazine_vw;''')

    query = '''
            CREATE VIEW magazine_vw
            AS SELECT magID,
            magazineName,
            cost,
            category,
            recStatus,
            recCreateDate
            FROM magazine;
    '''

    cursor.execute(query)
    connection.commit()


def subscription(givenUsername: str):

    cursor.execute('''DROP VIEW IF EXISTS magazine_vw;''')

    query = '''
            CREATE VIEW magazine_vw
            AS SELECT magID,
            custID,
            subID,
            paymentCompleted,
            startDate,
            endDate,
            numMagsMailed
            FROM subscription
    '''

    cursor.execute(query)
    connection.commit()


def payment(givenUsername: str):

    cursor.execute('''DROP VIEW IF EXISTS payment_vw;''')

    query = '''
            CREATE VIEW payment_vw
            AS SELECT payID,
            subID,
            paymentAmount,
            paymentType,
            paymentDate,
            cardNumber,
            cardCode,
            recCreateDate
            FROM payment;
    '''

    cursor.execute(query)
    connection.commit()

# gets input
print(f'\nLooking into all 5 entities...')
# invokes function
magazine()
username = input('Enter a username: ')
subscription(username)
payment(username)