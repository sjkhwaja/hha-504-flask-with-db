## import packages
import sqlite3

## connect to sqlite
connect = sqlite3.connect('/Users/sairakhwaja/Documents/GitHub/hha-504-flask-with-db/patients.db')

## conncect to object db
db = connect.cursor()

## delete patient table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit() #commit changes


## create new table 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            city CHAR(25) NOT NULL,
            pcp CHAR(25) NOT NULL,
            insurancecoverage VARCHAR(1) NOT NULL,
            gender VARCHAR(1) NOT NULL
        ); """

db.execute(table)
connect.commit()

## insert fake patient data to new table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, pcp, insurancecoverage, gender) values('47382', 'Michael', 'Jordan', '01/01/1983', 'Chicago', 'Dr. Douglas Marks', 'Yes', 'M')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, pcp, insurancecoverage, gender) values('24756', 'RJ', 'Barrett', '02/02/1999', 'New York', 'Dr. Rachel Fin', 'Yes', 'M')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, pcp, insurancecoverage, gender) values('82967', 'Derrick', 'Rose', '03/03/1972', 'New York', 'Dr. Dylan Smith', 'Yes', 'M')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, pcp, insurancecoverage, gender) values('48978', 'JR', 'Smith', '04/04/1980', 'Los Angeles', 'Dr. Maya Finneran', 'Yes', 'M')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, pcp, insurancecoverage, gender) values('50629', 'Tyson', 'Chandler', '05/05/1977', 'San Diego', 'Dr. Michael Phillips', 'Yes', 'M')")

connect.commit()
connect.close()
