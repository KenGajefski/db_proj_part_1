# This will hold all database functionality
import mysql
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime


class DBCreation:
    dbName = 'sampledb'

    TABLES = {}
    TABLES['paper'] = (
        "CREATE TABLE `paper` ("
        # TODO: Values for paperid need to be AUTO_INCREMENT. When you do this using the connector library, an error of
        # no default value is thrown. You can then add the data in through the shell and it will start at '2' instead 
        # of '1' We either need to swap over to another library or figure out how to do this in the 
        # front end when adding.
        " `paperid` INTEGER UNIQUE,"
        " `abstractPaper` VARCHAR(255),"
        " `titlePaper` VARCHAR(255),"
        " `pdfPaper` VARCHAR(255),"
        " PRIMARY KEY (`paperid`)"
        ") ENGINE=InnoDB")

    TABLES['author'] = (
        "CREATE TABLE `author` ("
        " `nameAuthor` VARCHAR(255),"
        " `affiliationsAuthor` VARCHAR(255),"
        " `emailAuthor` VARCHAR(255),"
        " PRIMARY KEY (`emailAuthor`)"
        ") ENGINE=InnoDB")

    # paperid should be AUTO_INCREMENT
    TABLES['authorList'] = (
        "CREATE TABLE `authorList` ("
        " `paperid` INTEGER,"
        " `email` VARCHAR(255),"
        " `significance` INTEGER,"
        " FOREIGN KEY (`paperid`) REFERENCES `paper` (`paperid`),"
        " FOREIGN KEY (`email`) REFERENCES `author` (`emailAuthor`)"
        ") ENGINE=InnoDB")

    TABLES['PCMember'] = (
        "CREATE TABLE `pcmember` ("
        " `memberid` INTEGER,"
        " `namePCM` VARCHAR(255),"
        " `emailPCM` VARCHAR(255),"
        " PRIMARY KEY (`emailPCM`),"
        " KEY (`memberid`)"
        ") ENGINE=InnoDB")

    TABLES['review'] = (
        "CREATE TABLE `review` ("
        # reportid should also be AUTO_INCREMENT. See comments on declaration of 'paper' table.
        " `reportid` INTEGER UNIQUE,"
        # TODO: Python and MySQL Connector DO NOT play nice with DATE values. This is being changed for
        # the purpose of trying to get the program to work.
        " `dateReview` DATE,"
        " `recommendationReview` VARCHAR(1),"
        " `commentReview` VARCHAR(255),"
        " `paperid` INTEGER NOT NULL,"
        " `email1` VARCHAR(255) NOT NULL,"
        " FOREIGN KEY (`paperid`) REFERENCES `paper` (`paperid`),"
        " FOREIGN KEY (`email1`) REFERENCES `pcmember` (`emailPCM`)"
        ") ENGINE=InnoDB")

    def drop_database(self, cursor):
        # Automatically drops db if it exists so we dont have to manually do it via mySQL
        try:
            cursor.execute("DROP DATABASE IF EXISTS {}".format(DBCreation.dbName))
            print("Database deleted successfully")
        except mysql.connector.Error as err:
            print("Failed dropping database: {}".format(err))

    def create_database(self, cursor, cnx):
        # TODO: Put in check to see if database exists, and drop if it does
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DBCreation.dbName))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
        try:
            cursor.execute("USE {}".format(DBCreation.dbName))
        except mysql.connector.Error as err:
            print("Database {} does not exist.".format(DBCreation.dbName))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                DBCreation.create_database(cursor)
                print("Database {} created successfully.".format(DBCreation.dbName))
                cnx.database = DBCreation.dbName
            else:
                print(err)
                exit(1)

    def create_table(self, cursor):
        for table_name in DBCreation.TABLES:
            table_description = DBCreation.TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def init_values(self, cursor, cnx):
        # AUTO_INCREMENT values can be added by using NULL. But since that throws an error, we should just number
        # these manually and do the rest in the front end
        add_paperValues = ("INSERT INTO paper "
                           "(paperid, abstractPaper, titlePaper, pdfPaper) "
                           "VALUES (0, 'abstract3', 'title0','pdf0'),"
                           "(1, 'abstract1', 'title1','pdf1'),"
                           "(2, 'abstract2', 'title2', 'pdf2'),"
                           "(3, 'abstract3', 'title3','pdf3'),"
                           "(4, 'abstract4', 'title4','pdf4'),"
                           "(5, 'abstract5', 'title5','pdf5'),"
                           "(6, 'abstract6', 'title6','pdf6'),"
                           "(7, 'abstract7', 'title7','pdf7'),"
                           "(8, 'abstract8', 'title8','pdf8'),"
                           "(9, 'abstract9', 'title9','pdf9')")

        add_authorValues = ("INSERT INTO author "
                            "(nameAuthor, affiliationsAuthor, emailAuthor) "
                            "VALUES ('Fotouhi', 'None', 'fotouhi@test.com'),"
                            "('Fotouhi', 'None', 'fotouhi@tes.com'),"
                            "('Fotouhi', 'None', 'fotouhi@t.com'),"
                            "('Nick Smith', 'None', 'lu@test.com'),"
                            "('Poe Dameron', 'RBL', 'poe@rbl.com'),"
                            "('D. Vader', 'EMPR', 'vader@sith.com'),"
                            "('Luke Copyright', 'None', 'luke@censorship.com'),"
                            "('Boy Wonder', 'Heroes', 'special@hero.com'),"
                            "('Duperman', 'Knockoffs', 'dupe@notreal.com'),"
                            "('Mattman', 'Knockoffs', 'matt@notreal.com')")

        add_authorListValues = ("INSERT INTO authorlist "
                                "(paperid, email, significance) "
                                "VALUES (0, 'fotouhi@test.com', 0),"
                                "(1, 'fotouhi@tes.com', 2),"
                                "(2, 'fotouhi@t.com', 4),"
                                "(3, 'lu@test.com', 6),"
                                "(4, 'poe@rbl.com', 8),"
                                "(5, 'vader@sith.com', 10),"
                                "(6, 'luke@censorship.com', 12),"
                                "(7, 'special@hero.com', 1),"
                                "(8, 'dupe@notreal.com', 3),"
                                "(9, 'matt@notreal.com', 5)")

        add_PCMemberValues = ("INSERT INTO pcmember "
                              "(namePCM, emailPCM) "
                              "VALUES ('PCM0', 'email0@email0.com'),"
                              "('PCM1', 'email1@email1.com'),"
                              "('PCM2', 'email2@email2.com'),"
                              "('PCM3', 'email3@email3.com'),"
                              "('PCM4', 'email4@email4.com'),"
                              "('PCM5', 'email5@email5.com'),"
                              "('PCM6', 'email6@email6.com'),"
                              "('PCM7', 'email7@email7.com'),"
                              "('PCM8', 'email8@email8.com'),"
                              "('PCM9', 'email9@email9.com'),"
                              "('Matt', 'matt@test.com'),"
                              "('John', 'john@test.com')")

        add_reviewValues = ("INSERT INTO review "
                            "(reportid, dateReview, recommendationReview, commentReview, paperid, email1) "
                            "VALUES (0, current_date() , 'Y', 'commentreview0', 0, 'matt@test.com'),"
                            "(1, current_date(), 'Y', 'commentreview1', 0, 'email0@email0.com'),"
                            "(2, current_date(), 'N', 'commentreview2', 2, 'email1@email1.com'),"
                            "(3, current_date(), 'N', 'commentreview3', 3, 'email2@email2.com'),"
                            "(4, current_date(), 'N', 'commentreview4', 4, 'email3@email3.com'),"
                            "(5, current_date(), 'N', 'commentreview5', 5, 'email4@email4.com'),"
                            "(6, current_date(), 'N', 'commentreview6', 6, 'email5@email5.com'),"
                            "(7, current_date(), 'N', 'commentreview7', 7, 'email6@email6.com'),"
                            "(8, current_date(), 'Y', 'commentreview8', 8, 'email7@email7.com'),"
                            "(9, current_date(), 'N', 'commentreview9', 9, 'email8@email8.com'),"
                            "(10, current_date(), 'N', 'commentReview10', 5, 'matt@test.com'),"
                            "(11, current_date(), 'N', 'commentReview11', 9, 'john@test.com')")

        cursor.execute(add_paperValues)
        cursor.execute(add_authorValues)
        cursor.execute(add_authorListValues)
        cursor.execute(add_PCMemberValues)
        cursor.execute(add_reviewValues)
        cnx.commit()
