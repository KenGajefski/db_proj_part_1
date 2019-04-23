from flask import flash


class Paper:
    def insert(self, cursor, cnx, user_id, user_abst, user_title, user_pdf):
        cursor.execute("USE sampledb")
        query = 'INSERT INTO paper (paperid, abstractPaper, titlePaper, pdfPaper) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (user_id, user_abst, user_title, user_pdf))
        cnx.commit()
        query2='SELECT paperid, abstractPaper, titlePaper, pdfPaper FROM paper WHERE paperid=%s'
        cursor.execute(query2, (user_id,))
        for (paperid) in cursor:
            flash("Inserted paper with id: {}".format(paperid))

    def delete_paper(self, cursor, cnx, user_id):
        cursor.execute("USE sampledb")
        query1 = 'DELETE FROM review WHERE paperid=%s'
        query2 = 'DELETE FROM authorlist WHERE paperid=%s'
        query3 = 'DELETE FROM paper WHERE paperid=%s'
        cursor.execute(query1, (user_id,))
        cursor.execute(query2, (user_id,))
        cursor.execute(query3, (user_id,))
        cnx.commit()

    def update_paper(self, cursor, cnx, user_id, user_abst, user_title, user_pdf):
        cursor.execute("USE sampledb")
        query = 'UPDATE paper SET abstractPaper=%s, titlePaper=%s, pdfPaper=%s WHERE paperid=%s'
        cursor.execute(query, (user_abst, user_title, user_pdf, user_id))
        cnx.commit()


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


class Prob7:
    def problem7(self, cursor, cnx):
        cursor.execute("USE sampledb;")
        query = ("SELECT email FROM review GROUP BY email HAVING COUNT(*) > 1;")
        cursor.execute(query)
        for (email) in cursor:
            flash("The email of the PCMember(s) who reviews the most papers is {}".format(email))

        query2=("SELECT namePCM FROM PCMember WHERE emailPCM = 'email0@email0.com';")
        cursor.execute(query2)
        for (namePCM) in cursor:
            flash("The name of the reviewer with email {} is {}".format(email, namePCM))

class Prob8:
    print('placeholder')


class Prob9:
    def problem9(self, cursor):
        cursor.execute("USE sampledb;")
        query='SELECT paperid FROM review WHERE recommendationReview="N" AND email = "matt@test.com" OR email = "john@test.com"'
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
