# This will hold all database functionality
import mysql
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime


class DBCreation():
    dbName = 'sampledb'

    TABLES = {}
    TABLES['paper'] = (
        "CREATE TABLE `paper` ("
        " `paperid` INTEGER,"
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
        " `memberid` INTEGER AUTO_INCREMENT,"
        " `namePCM` VARCHAR(255),"
        " `emailPCM` VARCHAR(255),"
        " PRIMARY KEY (`emailPCM`),"
        " KEY (`memberid`)"
        ") ENGINE=InnoDB")

    TABLES['review'] = (
        "CREATE TABLE `review` ("
        " `reportid` INTEGER,"
        # Python and MySQL Connector DO NOT play nice with DATE values. This is being changed for
        # the purpose of trying to get the program to work. Will be refactored at TBD
        " `dateReview` DATE,"
        " `recommendationReview` VARCHAR(255),"
        " `commentReview` VARCHAR(255),"
        " `paperid` INTEGER NOT NULL UNIQUE,"
        " `email` VARCHAR(255) NOT NULL UNIQUE,"
        " FOREIGN KEY (`paperid`) REFERENCES `paper` (`paperid`),"
        " FOREIGN KEY (`email`) REFERENCES `pcmember` (`emailPCM`)"
        ") ENGINE=InnoDB")

    def create_database(self, cursor, cnx):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DBCreation.dbName))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
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
        add_paperValues = ("INSERT INTO paper "
                           "(paperid, abstractPaper, titlePaper, pdfPaper) "
                           "VALUES (3, 'abstract3', 'title3','pdf3'),"
                           "(0, 'abstract0', 'title0','pdf0'),"
                           "(5, 'abstract5', 'title5', 'pdf5'),"
                           "(11, 'abstract11', 'title11','pdf11'),"
                           "(2, 'abstract2', 'title2','pdf2'),"
                           "(7, 'abstract7', 'title7','pdf7'),"
                           "(1, 'abstract1', 'title1','pdf1'),"
                           "(9, 'abstract9', 'title9','pdf9'),"
                           "(10, 'abstract10', 'title10','pdf10'),"
                           "(4, 'abstract4', 'title4','pdf4')")

        add_authorValues = ("INSERT INTO author "
                            "(nameAuthor, affiliationsAuthor, emailAuthor) "
                            "VALUES ('Mike Jones', 'None', 'mike@test.com'),"
                            "('Duke Mickey', 'RCA', 'duke@test.com'),"
                            "('Alex Doe', 'NAACP', 'alex@test.com'),"
                            "('Nick Smith', 'None', 'nick@test.com'),"
                            "('Poe Dameron', 'RBL', 'poe@rbl.com'),"
                            "('D. Vader', 'EMPR', 'vader@sith.com'),"
                            "('Luke Copyright', 'None', 'luke@censorship.com'),"
                            "('Boy Wonder', 'Heroes', 'special@hero.com'),"
                            "('Duperman', 'Knockoffs', 'dupe@notreal.com'),"
                            "('Mattman', 'Knockoffs', 'matt@notreal.com')")

        add_authorListValues = ("INSERT INTO authorlist "
                                "(paperid, email, significance) "
                                "VALUES (3, 'mike@test.com', 0),"
                                "(0, 'duke@test.com', 2),"
                                "(5, 'alex@test.com', 4),"
                                "(11, 'nick@test.com', 6),"
                                "(2, 'poe@rbl.com', 8),"
                                "(7, 'vader@sith.com', 10),"
                                "(1, 'luke@censorship.com', 12),"
                                "(9, 'special@hero.com', 1),"
                                "(10, 'dupe@notreal.com', 3),"
                                "(4, 'matt@notreal.com', 5)")

        add_PCMemberValues = ("INSERT INTO pcmember "
                              "(namePCM, emailPCM) "
                              "VALUES ('PCM3', 'email3@email3.com'),"
                              "('PCM0', 'email0@email0.com'),"
                              "('PCM5', 'email5@email5.com'),"
                              "('PCM11', 'email11@email11.com'),"
                              "('PCM2', 'email2@email2.com'),"
                              "('PCM7', 'email7@email7.com'),"
                              "('PCM1', 'email1@email1.com'),"
                              "('PCM9', 'email9@email9.com'),"
                              "('PCM10', 'email10@email10.com'),"
                              "('PCM4', 'email4@email4.com')")

        add_reviewValues = ("INSERT INTO review "
                            "(reportid, dateReview, recommendationReview, commentReview, paperid, email) "
                            "VALUES (3, current_date() , 'recommendationreview3', 'commentreview3', 3, 'email3@email3.com'),"
                            "(0, current_date(), 'recommendationreview0', 'commentreview0', 0, 'email0@email0.com'),"
                            "(5, current_date(), 'recommendationreview5', 'commentreview5', 5, 'email5@email5.com'),"
                            "(11, current_date(), 'recommendationreview11', 'commentreview11', 11, 'email11@email11.com'),"
                            "(2, current_date(), 'recommendationreview2', 'commentreview2', 2, 'email2@email2.com'),"
                            "(7, current_date(), 'recommendationreview7', 'commentreview7', 7, 'email7@email7.com'),"
                            "(1, current_date(), 'recommendationreview1', 'commentreview1', 1, 'email1@email1.com'),"
                            "(9, current_date(), 'recommendationreview9', 'commentreview9', 9, 'email9@email9.com'),"
                            "(10, current_date(), 'recommendationreview10', 'commentreview10', 10, 'email10@email10.com'),"
                            "(4, current_date(), 'recommendationreview4', 'commentreview4', 4, 'email4@email4.com')")

        cursor.execute(add_paperValues)
        cursor.execute(add_authorValues)
        cursor.execute(add_authorListValues)
        cursor.execute(add_PCMemberValues)
        cursor.execute(add_reviewValues)
        cnx.commit()
