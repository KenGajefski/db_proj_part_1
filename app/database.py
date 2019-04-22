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
        " `reportid` INTEGER,"
        # TODO: Python and MySQL Connector DO NOT play nice with DATE values. This is being changed for
        # the purpose of trying to get the program to work.
        " `dateReview` DATE,"
        " `recommendationReview` VARCHAR(255),"
        " `commentReview` VARCHAR(255),"
        " `paperid` INTEGER NOT NULL UNIQUE,"
        " `email1` VARCHAR(255) NOT NULL UNIQUE,"
        " `email2` VARCHAR(255) UNIQUE,"
        " `email3` VARCHAR(255) UNIQUE,"
        " `email4` VARCHAR(255) UNIQUE,"
        " `email5` VARCHAR(255) UNIQUE,"
        " FOREIGN KEY (`paperid`) REFERENCES `paper` (`paperid`),"
        " FOREIGN KEY (`email1`) REFERENCES `pcmember` (`emailPCM`),"
        " FOREIGN KEY (`email2`) REFERENCES `pcmember` (`emailPCM`),"
        " FOREIGN KEY (`email3`) REFERENCES `pcmember` (`emailPCM`),"
        " FOREIGN KEY (`email4`) REFERENCES `pcmember` (`emailPCM`),"
        " FOREIGN KEY (`email5`) REFERENCES `pcmember` (`emailPCM`)"
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
                            "VALUES ('Fotouhi', 'None', 'fotouhi@test.com'),"
                            "('Fotouhi', 'RCA', 'fotouhi@tes.com'),"
                            "('Fotouhi', 'NAACP', 'fotouhi@t.com'),"
                            "('Nick Smith', 'None', 'lu@test.com'),"
                            "('Poe Dameron', 'RBL', 'poe@rbl.com'),"
                            "('D. Vader', 'EMPR', 'vader@sith.com'),"
                            "('Luke Copyright', 'None', 'luke@censorship.com'),"
                            "('Boy Wonder', 'Heroes', 'special@hero.com'),"
                            "('Duperman', 'Knockoffs', 'dupe@notreal.com'),"
                            "('Mattman', 'Knockoffs', 'matt@notreal.com')")

        add_authorListValues = ("INSERT INTO authorlist "
                                "(paperid, email, significance) "
                                "VALUES (3, 'fotouhi@test.com', 0),"
                                "(0, 'fotouhi@tes.com', 2),"
                                "(5, 'fotouhi@t.com', 4),"
                                "(3, 'lu@test.com', 6),"
                                "(2, 'poe@rbl.com', 8),"
                                "(7, 'vader@sith.com', 10),"
                                "(1, 'luke@censorship.com', 12),"
                                "(9, 'special@hero.com', 1),"
                                "(10, 'dupe@notreal.com', 3),"
                                "(4, 'matt@notreal.com', 5)")

        add_PCMemberValues = ("INSERT INTO pcmember "
                              "(namePCM, emailPCM) "
                              "VALUES ('PCM3', 'email3@email3.com'),"
                              "('PCM6', 'email0@email0.com'),"
                              "('PCM5', 'email5@email5.com'),"
                              "('PCM11', 'email11@email11.com'),"
                              "('PCM2', 'email2@email2.com'),"
                              "('PCM7', 'email7@email7.com'),"
                              "('PCM1', 'email1@email1.com'),"
                              "('PCM9', 'email9@email9.com'),"
                              "('PCM10', 'email10@email10.com'),"
                              "('PCM4', 'email4@email4.com')")

        add_reviewValues = ("INSERT INTO review "
                            "(reportid, dateReview, recommendationReview, commentReview, paperid, "
                            "email1, email2, email3, email4, email5) "
                            "VALUES (3, current_date() , 'N', 'commentreview3', 3, 'matt@test.com', 'john@test.com', NULL, NULL, NULL),"
                            "(0, current_date(), 'Y', 'commentreview0', 0, 'email0@email0.com', NULL, NULL, NULL, NULL),"
                            "(5, current_date(), 'Y', 'commentreview5', 5, 'email5@email5.com', NULL, NULL, NULL, NULL),"
                            "(11, current_date(), 'Y', 'commentreview11', 11, 'email11@email11.com', NULL, NULL, NULL, NULL),"
                            "(2, current_date(), 'N', 'commentreview2', 2, 'email2@email2.com', NULL, NULL, NULL, NULL),"
                            "(7, current_date(), 'N', 'commentreview7', 7, 'email7@email7.com', NULL, NULL, NULL, NULL),"
                            "(1, current_date(), 'N', 'commentreview1', 1, 'email1@email1.com', NULL, NULL, NULL, NULL),"
                            "(9, current_date(), 'Y', 'commentreview9', 9, 'email9@email9.com', NULL, NULL, NULL, NULL),"
                            "(10, current_date(), 'Y', 'commentreview10', 10, 'email10@email10.com', NULL, NULL, NULL, NULL),"
                            "(4, current_date(), 'N', 'commentreview4', 4, 'email4@email4.com', NULL, NULL, NULL, NULL)")

        cursor.execute(add_paperValues)
        cursor.execute(add_authorValues)
        cursor.execute(add_authorListValues)
        cursor.execute(add_PCMemberValues)
        cursor.execute(add_reviewValues)
        cnx.commit()
