import mysql
import mysql.connector
from app.login_form import LoginForm


class SearchFunc:
    @staticmethod
    def searchFotouhi():
        cnx = mysql.connector.connect(user='john', password='pass1234', database='sampledb')
        cursor = cnx.cursor()
        query = "SELECT nameAuthor FROM author WHERE nameAuthor ='Fotouhi'"
        cursor.execute(query)

        for (nameAuthor) in cursor:
            print("{} is author of ").format(nameAuthor)
        cursor.close()
        cnx.close()
