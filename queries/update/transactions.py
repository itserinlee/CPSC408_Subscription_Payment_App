import mysql.connector
import pprint


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "final_project"
)

cursor = connection.cursor()


def modifyPaymentCompleted(givenUsername: str):  # fulfills the transaction requirement
    '''
    first, this needs knowledge of the login credentials from the customer table
    needs to check last payment date in the payment table
    then would check the value of payment amount
    if that amount was 0 at the last recorded date, then the payment was not completed
    update the value of the attribute paymentComplete in subscription table
    '''

    cursor.execute('''DROP TRIGGER IF EXISTS validatePaymentComplete;''')

    sql = '''
        START TRANSACTION;
        CREATE TRIGGER validatePaymentComplete
        AFTER INSERT
        ON payment
        FOR EACH ROW
        UPDATE subscription
        SET startDate = CURRENT_DATE
        WHERE subID = 1;
        COMMIT;
        '''

    # TRY THIS IN TRIGGER:
    # SET paymentCompleted = 1

    cursor.execute(sql, multi=True)
    connection.commit()


# gets input
print(f'\nAdmin wants to check on the status of the subscription.')
print(f'In particular, if the last payment a customer made was completed...\n')
username = input('Enter your username: ')
# invokes function
modifyPaymentCompleted(username)