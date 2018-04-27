from Reader import Reader
from Validator import Validator
from My_CMD import *
from employee_db import EmployeeDB
from Employee import Employee
from Cleaner import Cleaner
from Graph import Graph

class Model_Handler():
    all_My_Employees = {}
    my_validator = Validator()
    my_reader = Reader()
    my_database = EmployeeDB()
    clean = Cleaner()
    graphs = Graph()
    user = ""
    error_File = ""
    database_Location = ""
    database_userName = ""
    database_password = ""

    def  __init__(self, config_File_Location):
        if(config_File_Location != None):
            config_contents = self.my_reader.read_Config(config_File_Location);
            self.user = config_contents[0]
            self.error_File = config_contents[1]
            self.database_Location = config_contents[2]
            self.database_userName = config_contents[3]
            self.database_password = config_contents[4]

    # Ryan Parker
    def Get_All_Employees_Database(self):
        #Fill allMyEmployees with data from database
        con = self.my_database.connect()
        try:
            c = con.cursor()
            sql = "SELECT * FROM employees"
            c.execute(sql)
            for row in c:
                empid = row[0]
                gender = row[1]
                age = row[2]
                sales = row[3]
                bmi = row[4]
                salary = [5]
                birthday = [6]
                emp = Employee(empid, gender, age, sales, bmi, salary, birthday)
                self.all_My_Employees[empid] = emp
            print("data retrived")
        except:
            print('faild to retrive employees from database')
        con.close()

    # Ryan Parker
    def Create_DDB(self):
        self.my_database.create_table()

    # Ryan Parker
    def Save_New_Employees_Database(self):
        employees = self.all_My_Employees
        for emp in employees.values():
            empid = emp.my_empid
            gender = emp.my_gender
            age = str(emp.my_age)
            sales = str(emp.my_sales)
            bmi = emp.my_bmi
            salary = str(emp.my_salary)
            birthday = emp.my_birthday
            #print(empid + ', ' + gender + ', ' + age + ', ' +  sales + ', ' + bmi + ', '  + salary + ', ' + birthday )
            self.my_database.save_employee(empid, gender, age, sales, bmi, salary, birthday)

    # Ryan Parker
    def save_to_txt(self):
        self.my_reader.write_file_txt(self.all_My_Employees)

    # Ryan Parker
    def load_txt(self):
        self.my_reader.read_file_txt(self.all_My_Employees)

    #Validation Handlers
    # Alex
    def Validate_Age(self, given_Age):
        return self.my_validator.Validate_Age(given_Age)

    #Create Graphs
    # Alex
    def CreateBar(self, type, all_my_employees):
        self.graphs.Create_Bar(type, all_my_employees)

    # Ryan Parker
    def create_pie(self, type):
        self.graphs.create_pie(type, self.all_My_Employees)

    # Ryan Parker
    def add_employee(self):
        val = self.my_validator
        c = self.clean
        empid = ""
        gender = ""
        age = 0
        sales = 0
        bmi = ""
        salary = 0
        birthday = ""

        empid = c.clean_empid(input("employee id number e.g. A102: "))
        while val.val_empid(self.all_My_Employees, empid)[0] == False:
            print('invalid ID try again')
            empid = input("employee id number e.g. A102: ")

        gender = c.clean_gender(input("employee's gender M or F: "))
        while val.val_gender(gender) == False:
            print('invalid gender try again')
            gender = input("employee's gender M or F: ")

        result = val.Validate_Age(input("employee's age: "))
        while result[0] == False:
            print(result[1])
            age = input("employee's age: ")

        sales = input("number of sales employee has made (3 digit number): ")
        while val.Validate_Sales(sales) == False:
            print('invalid sales try again: ')
            sales = input("number of sales employee has made (3 digit number): ")

        bmi = c.clean_bmi(input("employee's bmi (Normal, Overweight, Obesity, or Underweight): "))
        while val.val_bmi(bmi) == False:
            print('invalid bmi try again: ')
            bmi = input("employee's bmi (Normal, Overweight, Obesity, or Underweight): ")

        salary = input("employee's salary(5 digit number): ")
        while val.Validate_Salary(salary) == False:
            print('invalid salary try again: ')
            salary = input("employee's salary(5 digit number): ")

        birthday = c.Clean_Birthday(input("employee's birthday DD-MM-YYYY: "))
        while val.Validate_Birthday(birthday, age) == False:
            print('invalid bithday try again: ')
            birthday = input("employee's birthday DD-MM-YYYY: ")

        emp = Employee(empid, gender, age, sales, bmi, salary, birthday)

        self.all_My_Employees[empid] = emp
