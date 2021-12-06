QUERIES = {
        "MAGS_GET_ALL":
                        '''
                        SELECT magazineName
                        FROM magazine;
                        ''',
        "MAG_BY_NAME": 
                        '''
                        SELECT *
                        FROM magazine
                        WHERE magazineName = (%s);
                        ''',
        "MAGS_COUNT_BY_CAT":
                        '''
                        SELECT magazineName, category
                        FROM magazine
                        WHERE category LIKE "%(%s)%";
                        ''',
        "MAGS_COUNT_BY_YEAR":
                        '''
                        SELECT COUNT(magID) AS CountOfMag
                        FROM magazine
                        WHERE recCreateDate LIKE '(%s)-%';
                        ''',
        "MAGS_AVG_COST_BY_CAT":
                        '''
                        SELECT category, COUNT(category) AS CountOfCategory, ROUND(AVG(cost), 2) AS AvgCost
                        FROM magazine
                        GROUP BY category
                        ORDER BY AvgCost DESC;
                        ''',
        "CUST_GET_ALL":
                        '''
                        SELECT firstName, lastName, username
                        FROM customer;
                        ''',
        "CUST_GET_BY_YEAR":
                        '''
                        SELECT COUNT(custID) AS CountOfCust
                        FROM customer
                        WHERE recCreateDate LIKE '(%s)-%';
                        ''',
        "CUST_GET_BY_USERNAME":
                        '''
                        SELECT *
                        FROM customer
                        WHERE username = '(%s)';
                        ''',
}