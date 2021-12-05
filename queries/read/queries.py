QUERIES = {
        "GET_ALL_MAGAZINES": '''
                             SELECT *
                             FROM magazine
                             WHERE magazineName = (%s);
                             ''',
        "GET_MAGAZINES_BY_DATE":'''
                                SELECT *
                                FROM magazine
                                ORDER BY recCreateDate DESC;
                                ''',
        
}