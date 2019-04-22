from flask import flash

class Prob4:

    def problem4(self, cursor, cnx):

        cursor.execute("USE sampleDB")

        query = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@t.com' " \
                "AND email = 'fotouhi@t.com' AND A.paperID = P.paperID;"
        cursor.execute(query)
        for (titlePaper) in cursor:
            flash("Fotouhi is author of {}".format(titlePaper))

        query2 = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@tes.com' " \
                 "AND email = 'fotouhi@tes.com' AND A.paperID = P.paperID;"
        cursor.execute(query2)
        for (titlePaper) in cursor:
            flash("Fotouhi is author of {}".format(titlePaper))

        query3 = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@test.com'" \
                 "AND email = 'fotouhi@test.com' AND A.paperID = P.paperID;"
        cursor.execute(query3)
        for (titlePaper) in cursor:
            flash("Fotouhi is author of {}".format(titlePaper))



class Prob5:
    def problem5(self, cursor, cnx):

        cursor.execute("USE sampleDB")

        for (titlePaper) in cursor:
            flash("Fotouhi is author of {}".format(titlePaper))

        query = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@test.com'" \
                 "AND email = 'fotouhi@test.com' AND A.paperID = P.paperID;"
        cursor.execute(query)

        for (titlePaper) in cursor:
            flash("Fotouhi is first author of {}".format(titlePaper))

class Prob6:
    def problem6(self, cursor, cnx):
        cursor.execute("USE sampledb;")
        query=('SELECT paperID, COUNT(*) FROM authorList GROUP BY paperID HAVING COUNT(*) > 1')
        cursor.execute(query)

        for (titlePaper) in cursor:
            flash("Papers coauthored by Lu and Fotouhi are {}".format(titlePaper))


class Prob7:
    print('placeholder')


class Prob8:
    print('placeholder')


class Prob9:
    def problem9(self, cursor):
        cursor.execute("USE sampledb;")


class Prob10:
    # Currently changing DB schema to be able to do this question
    print('placeholder')

