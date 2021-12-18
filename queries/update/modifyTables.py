import mysql.connector
import pprint


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "final_project"
)

cursor = connection.cursor()


def modifyContactType(userInput: int, userID: int):  # fulfills UPDATE requirement of project
    '''
    takes in a boolean value: 1 for text and 0 for call
    this function is to update a preference about the way customer is notified about subscription
    '''

    query = "UPDATE profile SET contactType = %s WHERE custContID = %s;"

    cursor.execute(query, (userInput, userID))
    connection.commit()

    print(f'{cursor.rowcount} record(s) updated')
    print(f'Process completed.')


def deleteAccount(givenUsername: str, recStatus: int = 1): # CHANGE ME: when this is called, pass the parameter

    query = '''
        UPDATE profile
        SET recStatus = %s
        WHERE custContID IN (
                                SELECT profile.custContID
                                FROM customer c
                                WHERE c.custID = profile.custID
                                AND c.username = %s
                            );
    '''

    cursor.execute(query, (recStatus, givenUsername))
    connection.commit()

# gets input
print(f'How do you want to receive notifications about your subscription?')
userInput = input('Enter 1 for text or 0 for call: ')
userID = input('Enter your ID to update your preferences: ')
# call function
modifyContactType(int(userInput), int(userID))


# gets 2nd input
print(f'This is for when you need to delete a customer.')
username = input('Enter your username: ')
# call function
deleteAccount(username)