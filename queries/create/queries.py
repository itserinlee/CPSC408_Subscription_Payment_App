QUERIES = {
        "CREATE_MAGAZINE": 
                        '''
                        CREATE TABLE IF NOT EXISTS magazine (
                        magID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        magazineName VARCHAR(50),
                        cost FLOAT NOT NULL,
                        category VARCHAR(50),
                        recStatus BOOLEAN,
                        recCreateDate DATE DEFAULT (CURRENT_DATE)
                        );
                        ''',
        "CREATE_CUSTOMER":
                        '''
                        CREATE TABLE IF NOT EXISTS customer (
                        custID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        firstName VARCHAR(50),
                        lastName VARCHAR(50),
                        username VARCHAR(50),
                        password VARCHAR(50),
                        recCreateDate DATE DEFAULT (CURRENT_DATE)
                        );
                        ''',
        "CREATE_PROFILE": 
                        '''
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
                        ''',
        "CREATE_SUBSCRIPTION": 
                        '''
                        CREATE TABLE IF NOT EXISTS subscription (
                        magID INTEGER NOT NULL,
                        custID INTEGER NOT NULL,
                        subID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        paymentCompleted BOOLEAN,
                        startDate DATE,
                        endDate DATE,
                        numMagsMailed INTEGER,
                        CONSTRAINT FK_subscription_magID FOREIGN KEY (magID) REFERENCES magazine(magID),
                        CONSTRAINT FK_subscription_custID FOREIGN KEY (custID) REFERENCES customer(custID)
                        );
                        ''',
        "CREATE_PAYMENT":
                        '''
                        CREATE TABLE IF NOT EXISTS payment (
                        cardCode INTEGER,
                        cardNumber VARCHAR(25),
                        payID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        subID INTEGER NOT NULL,
                        paymentAmount FLOAT NOT NULL,
                        paymentType BOOLEAN,
                        paymentDate DATE,
                        recCreateDate DATE DEFAULT (CURRENT_DATE),
                        CONSTRAINT FK_subscription_subID FOREIGN KEY (subID) REFERENCES subscription(subID)
                        );
                        '''
}