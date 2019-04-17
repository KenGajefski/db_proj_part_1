# CSC 4710 - Database Project Part 1

This is the first part of the project for CSC 4710. This part includes a front-end interface with buttons for interacting with the database.

### Prerequisites

Required Software and Libraries

```
-Python 3.7.2
-Flask
-WTForms
-Flask-MySQL
-Flask-WTF
--MySQL Connector
```

This program also assumes that MySQL is setup with the required user account for the project part as well as running on port 3036 of the local machine.

Installing
--------------------------------------------

### Using PyCharm

Create a new Python project from this repo. You will then need to use pip to install all the necessary libraries.

#### It is highly recommended to install the PyCharm Professional edition and use your .edu email for registration so you have access to Flask configurations. The Community edition may not work correctly if setting up the Flask configuration from scratch  ####

```
This is to be done from the python console in PyCharm or follow the alternative method below
---------------------------------------------------------------------------------------------
pip install Flask
pip install WTForms
pip install Flask-WTF
pip install mysql-connector-python
```

An alternative to using the console is to go file > settings > Project:<projName> > Project interpreter
  From here you can click the '+' on the right side of the pane and search for the library
  Click 'Install Package' when you have the correct one selected

#### Make sure your configuration script path is pointing to 'project.py' when you run the program and set for flask. This can be done by selecting the 'edit configurations' option in the top right next to the 'run' button. ####

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE from JetBrains
* [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) - Connecting the Flask app with MySQL
* [WTForms](https://wtforms.readthedocs.io/en/stable/) - Web Form library for use with Flask

## Authors

* **Kenneth Gajefski**
* **Nicholas LaFramboise**

See also the list of [contributors](https://github.com/KenGajefski/db_proj_part_1/graphs/contributors) who participated in this project.
