# This will hold all database functionality
import mysql
from mysql.connector import errorcode

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
        "CREATE TABLE `PCMember` ("
        " `memberid` INTEGER AUTO_INCREMENT,"
        " `namePCM` VARCHAR(255),"
        " `emailPCM` VARCHAR(255),"
        " PRIMARY KEY (`emailPCM`),"
        " KEY (`memberid`)"
        ") ENGINE=InnoDB")

    TABLES['review'] = (
        "CREATE TABLE 'review' ("
        " `reportid` INTEGER,"
        " `dateReview` DATE,"
        " `recommendationReview` VARCHAR(255),"
        " `commentReview` VARCHAR(255),"
        " `paperid` INTEGER NOT NULL UNIQUE,"
        " `email` VARCHAR(255) NOT NULL UNIQUE,"
        " FOREIGN KEY (`paperid`) REFERENCES `paper` (`paperid`),"
        " FOREIGN KEY (`email`) REFERENCES `PCMember` (`emailPCM`)"
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

    def init_values(self):
        add_paperValues = ("INSERT INTO paper "
                           "(paperid, abstractPaper, titlePaper, pdfPaper) "
                           "VALUES (3, 'absract3', 'title3','pdf3'),"
                           "(0, 'abstract0', 'title0','pdf0'),"
                           "(5, 'abstract5', 'title5', 'pdf5')")

        add_authorValues = ("INSERT INTO author "
                            "(nameAuthor, affiliationsAuthor, emailAuthor) "
                            "VALUES (%s,%s,%s),"
                            "()")

        add_authorListValues = ("INSERT INTO authorlist "
                                "(paperid, email, significance) "
                                "VALUES (%s,%s,%s)")

        add_PCMemberValues = ("INSERT INTO pcmember "
                              "(memberid, namePCM, emailPCM) "
                              "VALUES (%s,%s,%s)")

        add_reviewValues = ("INSERT INTO review "
                            "(reportid, dateReview, recommendationReview, commentReview, paperid, email) "
                            "VALUES (%s,%s,%s,%s,%s,%s)")

