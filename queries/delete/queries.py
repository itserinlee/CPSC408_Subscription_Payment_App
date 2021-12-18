QUERIES = {
        "PAY_CHECK_TABLE": 
                        '''
                        DROP TABLE IF EXISTS payment;
                        '''
        ,
        "SUB_CHECK_TABLE": 
                        '''
                        DROP TABLE IF EXISTS subscription;
                        '''
        ,
        "PRO_CHECK_TABLE": 
                        '''
                        DROP TABLE IF EXISTS profile;
                        '''
        ,
        "CUST_CHECK_TABLE": 
                        '''
                        DROP TABLE IF EXISTS customer;
                        '''
        ,
        "MAG_CHECK_TABLE": 
                        '''
                        DROP TABLE IF EXISTS magazine;
                        ''',
        # TODO
        # (User) create a query that deletes a user's account (deletes customer which should also delete the profile record - cascade)
        "SOFT_DELETE":
                        '''
                        UPDATE profile
                        SET recStatus = %s
                        WHERE custContID IN (
                                SELECT profile.custContID
                                FROM customer c
                                WHERE c.custID = profile.custID
                                AND c.username = %s
                        );
                        '''
        # (Admin) create a query that deletes a magazine record (consider how it affects other tables)
}