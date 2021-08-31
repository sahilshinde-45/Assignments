import mysql
import mysql.connector as msql

from mysql.connector import Error

from main import employee_data

try:
    conn = mysql.connector.connect(host='localhost', database='employee', user='root', password='Neosoft$22',
                                   auth_plugin='mysql_native_password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS employee_data;')
        print('Creating table....')

        cursor.execute(
            "CREATE TABLE employee_data(EMPLOYEE_ID varchar(10), FIRST_NAME varchar(50),LAST_NAME varchar(50),EMAIL varchar(50),PHONE_NUMBER varchar(20),JOB_ID varchar(25), SALARY varchar(20),DEPARTMENT_ID varchar(10))")
        print("Table is created.")

        for i, row in employee_data.iterrows():
            # here %S means string values
            sql = ('INSERT INTO employee.employee_data'
                   '(EMPLOYEE_ID,FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, JOB_ID, SALARY, DEPARTMENT_ID)'
                   'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)')
            cursor.execute(sql, tuple(row))
            print("Record inserted successfully")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
