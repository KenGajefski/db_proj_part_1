# This will hold all database functionality
import mysql
from mysql.connector import errorcode

class DBCreation():
    dbName = 'sampledb'

    TABLES = {}
    TABLES['author'] = (
        "CREATE TABLE `author` ("
        " `namesAuthor` VARCHAR(255),"
        " `affiliationsAuthor` VARCHAR(255),"
        " `emailsAuthor` VARCHAR(255),"
        " PRIMARY KEY (`namesAuthor`)"
        ") ENGINE=InnoDB")

    TABLES['authorList'] = (
        "CREATE TABLE `authorList` ("
        " `listID` INTEGER,"
        " `authorName` VARCHAR(255),"
        " PRIMARY KEY (`listID`),"
        " FOREIGN KEY (`namesAuthor`) REFERENCES `author` (`namesAuthor`)"
        ") ENGINE=InnoDB")

    TABLES['PCMember'] = (
        "CREATE TABLE `PCMember` ("
        " `namePCM` VARCHAR(255),"
        " `emailPCM` VARCHAR(255),"
        " PRIMARY KEY (namePCM)"
        ") ENGINE=InnoDB")

    TABLES['review'] = (
        "CREATE TABLE 'review' ("
        " `reportID` INTEGER,"
        " `dateReview` DATE,"
        " `recommendationReview` VARCHAR(255),"
        " `commentReview` VARCHAR(255),"
        " `namePCM` VARCHAR(255),"
        " PRIMARY KEY (reportID),"
        " FOREIGN KEY (namePCM) REFERENCES `PCMember` (`namePCM`)"
        ") ENGINE=InnoDB")

    TABLES['paper'] = (
        "CREATE TABLE `paper` ("
        " `paperID` INTEGER,"
        " `abstractPaper` VARCHAR(255),"
        " `titlePaper` VARCHAR(255),"
        " `pdfPaper` VARCHAR(255),"
        " `listID` INTEGER,"
        " `reportID` INTEGER,"
        " PRIMARY KEY (`paperID`),"
        " FOREIGN KEY (`listID`) REFERENCES `authorList` (`listID`),"
        " FOREIGN KEY (`reportID`) REFERENCES `review` (`reportID`)"
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
