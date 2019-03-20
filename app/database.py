# This will hold all database functionality
import mysql
from mysql.connector import errorcode

class DBCreation():
    dbName = 'sampledb'

    TABLES = {}
    TABLES['authors'] = (
        "CREATE TABLE `authors` ("
        " `idAuthors` INTEGER,"
        " `namesAuthors` VARCHAR(255),"
        " `affiliationsAuthors` VARCHAR(255),"
        " `emailsAuthors` VARCHAR(255),"
        " PRIMARY KEY (`idAuthors`)"
        ") ENGINE=InnoDB")

    TABLES['reports'] = (
        "CREATE TABLE `reports` ("
        " `idReports` INTEGER,"
        " `dateReports` DATE,"
        " `descriptionReports` VARCHAR(255),"
        " `finalReports` INTEGER,"
        " PRIMARY KEY (`idReports`)"
        ") ENGINE=InnoDB")

    TABLES['papers'] = (
        "CREATE TABLE `papers` ("
        " `idPapers` INTEGER,"
        " `idAuthors` INTEGER,"
        " `idReports` INTEGER,"
        " `authorPapers` VARCHAR(255),"
        " `abstractPapers` VARCHAR(255),"
        " `titlePapers` VARCHAR(255),"
        " `pdfPapers` VARCHAR(255),"
        " PRIMARY KEY (`idPapers`),"
        " FOREIGN KEY (`idAuthors`) REFERENCES `authors` (`idAuthors`),"
        " FOREIGN KEY (`idReports`) REFERENCES `reports` (`idReports`)"
        ") ENGINE=InnoDB")

    def create_database(self):
        try:
            DBCreation.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DBCreation.dbName))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        try:
            DBCreation.cursor.execute("USE {}".format(DBCreation.dbName))
        except mysql.connector.Error as err:
            print("Database {} does not exist.".format(DBCreation.dbName))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                DBCreation.create_database(DBCreation.cursor)
                print("Database {} created successfully.".format(DBCreation.dbName))
                DBCreation.cnx.database = DBCreation.dbName
            else:
                print(err)
                exit(1)

    def create_table(self):
        for table_name in DBCreation.TABLES:
            table_description = DBCreation.TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                DBCreation.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

