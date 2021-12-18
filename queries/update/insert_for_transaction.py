import mysql.connector
import pprint


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "final_project"
)


cursor = connection.cursor()


def createTables():
    '''
    this function drops tables & then creates/re-creates the tables in final_project db every time this program runs
    '''

    cursor.execute('''DROP TABLE IF EXISTS payment;''')
    cursor.execute('''DROP TABLE IF EXISTS subscription;''')
    cursor.execute('''DROP TABLE IF EXISTS profile;''')
    cursor.execute('''DROP TABLE IF EXISTS customer;''')
    cursor.execute('''DROP TABLE IF EXISTS magazine;''')
    

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS magazine (
                    magID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    magazineName VARCHAR(50),
                    cost FLOAT NOT NULL,
                    recStatus BOOLEAN,
                    recCreateDate DATE DEFAULT (CURRENT_DATE),
                    category VARCHAR(50)
                    );
    ''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS customer (
                    custID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    firstName VARCHAR(50),
                    lastName VARCHAR(50),
                    username VARCHAR(50),
                    password VARCHAR(50),
                    recCreateDate DATE DEFAULT (CURRENT_DATE)
                    );
    ''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS profile (
                    custContID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    custID INTEGER NOT NULL,
                    phoneNum CHAR(12) NOT NULL,
                    zipCode CHAR(5) NOT NULL,
                    state CHAR(2) NOT NULL,
                    city VARCHAR(100) NOT NULL,
                    streetAddress VARCHAR(150) NOT NULL,
                    contactType BOOLEAN,
                    recUpdateDate DATE DEFAULT (CURRENT_DATE),
                    recStatus BOOLEAN,
                    startDate DATE,
                    endDate DATE,
                    CONSTRAINT FK_profile_custID FOREIGN KEY (custID) REFERENCES customer(custID)
                    );
    ''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS subscription (
                    subID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    numMagsMailed INTEGER,
                    paymentCompleted BOOLEAN,
                    startDate DATE,
                    endDate DATE,
                    magID INTEGER NOT NULL,
                    custID INTEGER NOT NULL,
                    CONSTRAINT FK_subscription_magID FOREIGN KEY (magID) REFERENCES magazine(magID),
                    CONSTRAINT FK_subscription_custID FOREIGN KEY (custID) REFERENCES customer(custID)
                    );
    ''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS payment (
                    payID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    subID INTEGER NOT NULL,
                    paymentAmount FLOAT NOT NULL,
                    paymentType BOOLEAN,
                    paymentDate DATE,
                    cardNumber VARCHAR(25),
                    cardCode INTEGER,
                    recCreateDate DATE DEFAULT (CURRENT_DATE),
                    CONSTRAINT FK_subscription_subID FOREIGN KEY (subID) REFERENCES subscription(subID)
                    );
    ''')


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


def magazine(staging: list):

    magazineData = list(set([(row[0], row[1], row[2], row[3], row[4], row[5]) for row in staging]))

    # SQL Date Data Types
    # DATETIME - format: YYYY-MM-DD HH:MI:SS

    query = '''
    INSERT INTO magazine (magID, magazineName, cost, recStatus, recCreateDate,category) VALUES(%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(query, magazineData)                               # magazineData is a list of tuples
    connection.commit()

    print(f'Insertion of data into magazine table: COMPLETE')


def customer(staging: list):

    customerData = list(set([(row[0], row[1], row[2], row[3], row[4], row[5]) for row in staging]))

    query = '''
    INSERT INTO customer (custID, firstName, lastName, username, password, recCreateDate) VALUES(%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(query, customerData)                               # customerData is a list of tuples
    connection.commit()

    print(f'Insertion of data into customer table: COMPLETE')


def profile(staging: list):

    # step 1: collect the data from the CSV to be loaded into profile table
     
    profileData = list(set([(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]) for row in staging]))

    # step 2: write query that performs INSERT
    # bonus: SQL server is going to generate an ID number since AUTO_INCREMENT

    query = '''
    INSERT INTO profile (
                        custContID,
                        custID,
                        phoneNum,
                        zipCode,
                        state,
                        city,
                        streetAddress,
                        contactType,
                        recUpdateDate,
                        recStatus,
                        startDate,
                        endDate
                        )
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(query, profileData)                                   # profileData is a list of tuples
    connection.commit()

    print(f'Insertion of data into profile table: COMPLETE')


def subscription(staging: list):

    subscriptionData = list(set([(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in staging]))

    query = '''
    INSERT INTO subscription (subID, numMagsMailed, paymentCompleted, startDate, endDate, magID, custID) VALUES(%s,%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(query, subscriptionData)                               # subscriptionData is a list of tuples
    connection.commit()

    print(f'Insertion of data into subscription table: COMPLETE')


def payment(staging: list):
    
    print('HERE')
    paymentData = list(set([(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in staging]))

    print('WHAT ABOUT HERE')

    query = '''
    INSERT INTO payment (payID, subID, paymentAmount, paymentType, paymentDate, cardNumber, cardCode, recCreateDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    '''

    print('TRYING HERE TOO?')
    cursor.executemany(query, paymentData)                               # paymentData is a list of tuples
    connection.commit()

    print(f'Insertion of data into payment table: COMPLETE')

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

    print(f'Transaction: COMPLETE')


def loadCSV(csv: str):

    staging = dataCleaner(csv)
    staging = staging[1:]                                                 # this throws away the headers of the CSV

    return staging


def populateData():

    # createTables()
    # receiveStaging = loadCSV('magazineTable.csv')
    # print('Loaded magazine csv file.')
    # magazine(receiveStaging)

    # receiveStaging = loadCSV('Customer-Table 1.csv')
    # print('Loaded customer csv file.')
    # customer(receiveStaging)

    # receiveStaging = loadCSV('Profile-Table 1.csv')
    # print('Loaded profile csv file.')
    # profile(receiveStaging)

    # receiveStaging = loadCSV('Subscription-Table 1.csv')
    # print('Loaded subscription csv file.')
    # subscription(receiveStaging)

    receiveStaging = loadCSV('../../data/Payment.csv')
    print('Loaded payment csv file.')
    payment(receiveStaging)


if __name__ == '__main__':
    populateData()