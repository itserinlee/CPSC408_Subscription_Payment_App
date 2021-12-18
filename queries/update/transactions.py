import mysql.connector


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nosplits35!",
    database = "final_project"
)

cursor = connection.cursor()

def payment(staging: list):
    
    paymentData = list(set([(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in staging]))

    query = '''
    INSERT INTO payment (payID, subID, paymentAmount, paymentType, paymentDate, cardNumber, cardCode, recCreateDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(query, paymentData)                               # paymentData is a list of tuples
    connection.commit()

    print(f'Insertion of data into payment table: COMPLETE')



def modifyPaymentCompleted(givenUsername: str):  # fulfills the transaction requirement
    '''
    first, this needs knowledge of the login credentials from the customer table
    needs to check last payment date in the payment table
    then would check the value of payment amount
    if that amount was 0 at the last recorded date, then the payment was not completed
    update the value of the attribute paymentComplete in subscription table
    '''

    # receiveStaging = loadCSV('Payment-Table 1.csv')
    # print('Loaded payment csv file.')
    # payment(receiveStaging)

    paymentData = [(800, 1234123412341237, 6, 60, 1, '2021-12-12', '2021-11-11')]

    query = '''
    INSERT INTO payment (payID, subID, paymentAmount, paymentType, paymentDate, cardNumber, cardCode, recCreateDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(query, paymentData)                               # paymentData is a list of tuples
    connection.commit()


    cursor.execute('''DROP TRIGGER IF EXISTS validatePaymentComplete;''')

    sql = '''
        START TRANSACTION;
        CREATE TRIGGER validatePaymentComplete
        AFTER INSERT
        ON payment
        FOR EACH ROW
        UPDATE subscription s
        INNER JOIN customer c ON s.custID = c.custID
        SET s.paymentCompleted = 1
        WHERE c.username = 'e_lee';
        COMMIT;
    '''

    cursor.execute(sql, multi=True)
    connection.commit()


# gets input
print(f'\nAdmin wants to check on the status of the subscription.')
print(f'In particular, if the last payment a customer made was completed...\n')
username = input('Enter your username: ')
# invokes function
modifyPaymentCompleted(username)