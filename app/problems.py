# Rename to Prob 4
class SearchFunc:
    @staticmethod
    def searchFotouhi(cursor, cnx):
        cursor.execute("USE sampleDB")
        query2 = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@t.com' " \
                 "AND email = 'fotouhi@t.com' AND A.paperID = P.paperID;"
        cursor.execute(query2)
        for (nameAuthor) in cursor:
            print("Fotouhi is author of", nameAuthor)
        for (titlePaper) in cursor:
            print("Fotouhi is author of", titlePaper)
        cursor.close()
        cnx.close()
        # This is how you clear session
        # session.pop('name', None)
