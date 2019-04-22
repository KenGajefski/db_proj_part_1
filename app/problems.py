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

        query = "SELECT titlePaper FROM author, authorList A, paper P WHERE emailAuthor = 'fotouhi@test.com'" \
                "AND email = 'fotouhi@test.com' AND A.paperID = P.paperID;"
        cursor.execute(query)

        for (titlePaper) in cursor:
            flash("Fotouhi is first author of {}".format(titlePaper))


class Prob6:
    def problem6(self, cursor, cnx):
        cursor.execute("USE sampledb;")
        query = ("SELECT P.paperID FROM authorList P, authorList D WHERE P.email = 'lu@test.com' "
                 "AND D.email =  'fotouhi@tes.com';")
        cursor.execute(query)
        for (paperID) in cursor:
            flash("The paperID coauthored by Lu and Fotouhi is {}".format(paperID))

        query2 = ("SELECT titlePaper FROM paper WHERE paperID = 3;")

        cursor.execute(query2)

        for (titlePaper) in cursor:
            flash("The title of the paper is: {}".format(titlePaper))

        # for (titlePaper) in cursor:
        #    flash("Papers coauthored by Lu and Fotouhi are {}".format(titlePaper))


class Prob7:
    print('placeholder')


class Prob8:
    print('placeholder')


class Prob9:
    def problem9(self, cursor):
        cursor.execute("USE sampledb;")
        query='SELECT paperid FROM review WHERE recommendationReview="N" AND email="matt@test.com" OR email="john@test.com"'
        cursor.execute(query)
        for (paperid) in cursor:
            flash('Rejected paper id: {}'.format(paperid))


class Prob10:
    def problem10(self,cursor):
        cursor.execute('USE sampledb')
        query='SELECT paperid FROM review WHERE recommendationReview="Y" HAVING COUNT(*) > 2'
        cursor.execute(query)
        for (paperid) in cursor:
            flash('Approved paper id: {}'.format(paperid))
