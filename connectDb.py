## import packages
import pandas as pd
import sqlite3

## connect to db
def get_db_connection():
    conn = sqlite3.connect('/Users/sairakhwaja/Documents/GitHub/hha-504-flask-with-db/patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

## save to pd df
df = pd.DataFrame(patientListSql)
df

## rename columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'city', 'pcp', 'insurancecoverage', 'gender']
df