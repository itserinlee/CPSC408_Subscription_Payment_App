# A trigger is a special type of stored procedure
# that automatically runs when an event occurs in the database server
# DML triggers run when a user tries to modify data
# through INSERT, UPDATE, or DELETE statements on a table or view

import mysql.connector
import pprint


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nosplits35!",
    database = "final_project"
)

cursor = connection.cursor()

def convert(value: str):
    '''
    converts the given string passed as a parameter to be the most restrictive data type for the execute() function
    so that when the cursor executes a query, it will try to force the types to match
    '''
    
    types = [int, float, str]   # order needs to be this way bc int is most restrictive data type conversion
    if value == '':
        return None
    for t in types:
        try:
            return t(value)
        except:
            pass


def dataCleaner(path: str):
    '''
    reads in a CSV files & type converts to a list of tuples
    returns a variable called dataCleaned of a list type
    '''

    with open(path, 'r', encoding = 'utf-8') as f:
        data = f.readlines()

    data = [line.strip().split(',') for line in data]
    dataCleaned = []

    for row in data[:]:
        row = [convert(element) for element in row]
        dataCleaned.append(tuple(row))
    
    return dataCleaned


def modifyPaymentCompleted(givenUsername: str, staging: list):  # fulfills the transaction requirement
    '''
    first, this needs knowledge of the login credentials from the customer table
    needs to check last payment date in the payment table
    then would check the value of payment amount
    if that amount was 0 at the last recorded date, then the payment was not completed
    update the value of the attribute paymentComplete in subscription table
    '''

    cursor.execute('''DROP TRIGGER IF EXISTS validatePaymentComplete''')

    # trigger = ''

    trigger = '''
        CREATE TRIGGER validatePaymentComplete
        AFTER INSERT
        ON payment
        FOR EACH ROW
        BEGIN

            UPDATE subscription
            SET startDate = CURRENT_DATE
            FROM subscription s
            WHERE s.subID = 1
        END;
        '''
            # INNER JOIN payment p ON s.payID = p.payID
            # WHERE p.paymentAmount IS NOT NULL
            # SET paymentCompleted = 1
            # WHERE c.username = ''' + givenUsername + ''';\nEND;

    cursor.execute(trigger)
    cursor.commit()

    # trigger2 = '''
    #     CREATE TRIGGER validatePaymentComplete
    #     BEFORE INSERT
    #     ON payment
    #     FOR EACH ROW
    #     BEGIN

    #         UPDATE subscription
    #         FROM subscription AS s
    #         INNER JOIN payment AS p ON s.subID = p.subID;
        
    #     END;
    # '''

    # result = cursor.fetchall()
    # return result


def loadStagingCSV(path: str):
    '''
    reads in & parses Profile.CSV using dataCleaner() function
    loading this CSV into a list to be passed throughout program is used in lieu of inserting data via staging table
    '''

    staging = dataCleaner(path)
    staging = staging[1:]                                                  # this throws away the headers of the CSV                                                # this throws away the headers of the CSV

    return staging


# redo set up
# receiveStaging = loadStagingCSV('../../data/Subscription.csv')
# receiveStaging2 = loadStagingCSV('../../data/Payment.csv')

# gets input
print(f'\nAdmin wants to check on the status of the subscription.')
print(f'In particular, if the last payment a customer made was completed...\n')
username = input('Enter your username: ')
# invokes function
modifyPaymentCompleted(username)