QUERIES = {
        "CHECK_AGENCY": '''
                        DROP TABLE IF EXISTS agency;
                        '''
        ,
        "CHECK_EXPEDITION": '''
                        DROP TABLE IF EXISTS expedition;
                        '''
        ,
        "CHECK_ASTRONAUT": 
                        '''
                        DROP TABLE IF EXISTS astronaut;
                        '''
        ,
        "CHECK_ASTRO_EXPED": 
                        '''
                        DROP TABLE IF EXISTS astro_expedition;
                        '''
        ,
        "CREATE_AGENCY": '''
                        CREATE TABLE agency(
                        agencyID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        Name VARCHAR(50),
                        Origin VARCHAR(20)
                        );
                        ''',
        "CREATE_EXPEDITION":
                        '''
                        CREATE TABLE expedition(
                        expeditionNumber INTEGER NOT NULL PRIMARY KEY,
                        Duration INTEGER
                        );
                        ''',
        "CREATE_ASTRONAUT": 
                        '''
                        CREATE TABLE astronaut(
                        astronautID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        Name VARCHAR(50),
                        Age INTEGER,
                        Agency INTEGER NOT NULL,
                        CONSTRAINT FK_astronaut_agency FOREIGN KEY (Agency) REFERENCES agency(AgencyID)
                        );
                        ''',
        "CREATE_ASTRO_EXPED": 
                        '''
                        CREATE TABLE astro_expedition(
                        ID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        Expedition INTEGER NOT NULL,
                        Astronaut INTEGER NOT NULL,
                        CONSTRAINT FK_astro_expedition_exp FOREIGN KEY (Expedition) REFERENCES expedition(expeditionNumber),
                        CONSTRAINT FK_astro_expedition_astro FOREIGN KEY (Astronaut) REFERENCES astronaut(astronautID)
                        );
                        ''',
        "INSERT_AGENCY":
                        '''
                        INSERT INTO agency 
                        (Name, Origin)
                        VALUES (%s, %s)
                        ''',
        "INSERT_EXPEDITION":
                        '''
                        INSERT INTO expedition 
                        (expeditionNumber, Duration)
                        VALUES (%s, %s)
                        ''',
        "INSERT_ASTRONAUT":
                        '''
                        INSERT INTO astronaut 
                        (astronautID, Name, Age, Agency)
                        VALUES (%s, %s, %s, %s)
                        ''',
        "INSERT_ASTRO_EXPED":
                        '''
                        INSERT INTO astro_expedition 
                        (ID, Expedition, Astronaut)
                        VALUES (%s, %s, %s)
                        ''',
        "GET_AGENCY_ID":
                        '''
                        SELECT agencyID
                        FROM agency;
                        ''',
        "GET_ASTRONAUT_ID": 
                        '''
                        SELECT astronautID
                        FROM agency;
                        ''',
        "GET_ASTRO_EXPED_ID": 
                        '''
                        SELECT ID
                        FROM astro_expedition;
                        '''
}