class SearchFunc:
    @staticmethod
    def searchFotouhi(cursor, cnx):

        cursor.execute("USE sampleDB")
        S1 = 'fotouhi@t.com'
        S2 = 'fotouhi@t.com'

        # Getting a SQL syntax error on line 16 - works on the SQL
        # side but the conversion between SQL/Python is incorrect
        #query = ("SELECT emailAuthor, email, A.paperID, P.paperID, titlePaper"
        #         "FROM author, authorList A, paper P"
        #         "WHERE emailAuthor = %s AND email = %s AND A.paperID = P.paperID")
        query = "SELECT nameAuthor FROM author WHERE nameAuthor = 'Fotouhi'"
        query2 = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@t.com' AND email = 'fotouhi@t.com' AND A.paperID = P.paperID;"

        #cursor.execute(query)
        cursor.execute(query2)

        #cursor.execute(query, S1, S2)

        for (nameAuthor) in cursor:
            print("Fotouhi is author of", nameAuthor)
        for (titlePaper) in cursor:
            print("Fotouhi is author of", titlePaper)

        cursor.close()
        cnx.close()
