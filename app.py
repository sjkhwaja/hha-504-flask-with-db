## Import packages
from flask import Flask, render_template
import sqlite3
import os

## Create new flask app
app = Flask(__name__)

## Connect user to first page
def get_db_connection():
        dir = os.getcwd() + '/patients.db'
        print('dir:', dir)
        conn = sqlite3.connect(dir) 
        conn.row_factory = sqlite3.Row 
        return conn

##
@app.route('/patients')
def patients():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('bootstrap.html', listPatients=patientListSql)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
