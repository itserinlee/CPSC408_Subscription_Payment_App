import mysql.connector


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "final_project"
)

cursor = connection.cursor()


def single_customer_profile_view(givenUsername: str):  # fulfills the view requirement

    cursor.execute('''DROP VIEW IF EXISTS vw_customer_profile;''')

    query = '''
            CREATE VIEW single_customer_profile_vw
            AS SELECT c.custID,
            firstName,
            lastName,
            username,
            password,
            recCreateDate,
            custContID,
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
            FROM customer AS c, profile AS p
            WHERE c.custID = p.custID
            AND c.username = %s
    '''

    # if we wanted to, we could make this view only of continued customers
    # by adding the following to the WHERE clause: AND p.custContID IS NOT NULL;

    # OR
    # we just do a SELECT statement as a way to display this specifically if user wants

    cursor.execute(query, (givenUsername, ))
    connection.commit()

def single_customer_profile_view(givenUsername: str):  # fulfills the view requirement

    cursor.execute('''DROP VIEW IF EXISTS single_customer_profile_vw;''')

    query = '''
            CREATE VIEW single_customer_profile_vw
            AS SELECT c.custID,
            firstName,
            lastName,
            username,
            password,
            recCreateDate,
            custContID,
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
            FROM customer AS c, profile AS p
            WHERE c.custID = p.custID
            AND c.username = %s
    '''

    # if we wanted to, we could make this view only of continued customers
    # by adding the following to the WHERE clause: AND p.custContID IS NOT NULL;

    # OR
    # we just do a SELECT statement as a way to display this specifically if user wants

    cursor.execute(query, (givenUsername, ))
    connection.commit()


def all_customer_profile_view():

    cursor.execute('''DROP VIEW IF EXISTS vw_customer_profile;''')

    query = '''
            CREATE VIEW vw_customer_profile
            AS SELECT c.custID,
            firstName,
            lastName,
            username,
            password,
            recCreateDate,
            custContID,
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
            FROM customer AS c, profile AS p
            WHERE c.custID = p.custID
    '''


    cursor.execute(query)
    connection.commit()


def cont_customer_profile_view():

    cursor.execute('''DROP VIEW IF EXISTS vw_cont_customer_profile;''')

    query = '''
            CREATE VIEW vw_cont_customer_profile
            AS SELECT c.custID,
            firstName,
            lastName,
            username,
            password,
            recCreateDate,
            custContID,
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
            FROM customer AS c, profile AS p
            WHERE c.custID = p.custID
            AND p.custContID IS NOT NULL;
    '''

    # if we wanted to, we could make this view only of continued customers
    # by adding the following to the WHERE clause: AND p.custContID IS NOT NULL;

    # OR
    # we just do a SELECT statement as a way to display this specifically if user wants

    cursor.execute(query)
    connection.commit()

# gets input
print(f'\nAdmin wants to gather all information on a customer.')
username = input('Enter their username: ')
# invokes function
single_customer_profile_view(username)
all_customer_profile_view()
cont_customer_profile_view()