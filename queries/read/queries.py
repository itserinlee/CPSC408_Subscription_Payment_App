QUERIES = {
        "MAGS_GET_ALL":
                        '''
                        SELECT *
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
                        '''
}