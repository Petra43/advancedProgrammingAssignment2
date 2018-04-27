import sqlite3
# Ryan Parker whole file
class EmployeeDB:

    def connect(self):
        try:
            con = sqlite3.connect('employees.db')
            return con
        except:
            print('connection to database failed')

    def create_table(self):
        con = self.connect()
        try:
            c = con.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS employees (
            empid TEXT PRIMARY KEY UNIQUE,
            gender CHAR(1),
            age INT,
            sales INT,
            bmi TEXT,
            salary INT,
            birthday TEXT);"""
            c.execute(sql)
            con.commit()

        except:
            print('table aready exists')
        con.close()

    def save_employee(self, empid, gender, age, sales, bmi, salary, birthday):
        con = self.connect()
        try:
            c = con.cursor()
            insert = "INSERT INTO employees(empid, gender, age, sales, bmi, salary, birthday) "
            values = "VALUES('" + empid + "', '" + gender + "', " + age + ", " + sales + ", '" + bmi + "', " + salary + ", '" + birthday + "');"
            sql = insert + values
            c.execute(sql)
            con.commit()
            con.close()
        except:
            print('failed to add employee (conflictiong empid)')
