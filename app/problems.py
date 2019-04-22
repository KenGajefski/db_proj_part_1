from flask import flash

class Prob4:
    def searchFotouhi(self, cursor, cnx):
        cursor.execute("USE sampleDB")
        query2 = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@t.com' " \
                 "AND email = 'fotouhi@t.com' AND A.paperID = P.paperID;"
        cursor.execute(query2)
        for (titlePaper) in cursor:
            flash("Fotouhi is author of {}".format(titlePaper))
        cursor.close()
        cnx.close()
        # This is how you clear session
        # session.pop('name', None)

class Prob5:
    def problem5(self, cursor, cnx):
        cursor.execute("USE sampleDB")

        for (titlePaper) in cursor:
            flash("Fotouhi is first author of {}".format(titlePaper))
