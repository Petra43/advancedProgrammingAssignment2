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
        prompt = "id number e.g. A102: "
        first_run = True
        while not val.val_empid(self.all_My_Employees, empid)[0]:
            empid = self.get_employee_data(val.val_empid(self.all_My_Employees, c.clean_empid(empid)), prompt, first_run)
            first_run = False

        gender = ""
        prompt = "gender M or F: "
        first_run = True
        while not val.val_gender(gender)[0]:
            gender = self.get_employee_data(val.val_gender(c.clean_gender(gender)), prompt, first_run)
            first_run = False


        age = ""
        prompt = "age: "
        first_run = True
        while not val.Validate_Age(age)[0]:
            age = self.get_employee_data(val.Validate_Age(age), prompt, first_run)
            first_run = False

        sales = ""
        prompt = "number of sales made (3 digit number): "
        first_run = True
        while not val.Validate_Sales(sales)[0]:
            data = self.get_employee_data(val.Validate_Sales(sales), prompt, first_run)
            first_run = False

        bmi = ""
        prompt = "bmi (Normal, Overweight, Obesity, or Underweight): "
        first_run = True
        while not val.val_bmi(bmi)[0]:
            bmi = self.get_employee_data(val.val_bmi(c.clean_bmi(bmi)), prompt, first_run)
            first_run = False

        salary = ""
        # this keeped displaying an erorr to the user and i don't understand how its validator works to fix it
        #prompt = "salary(5 digit number): "
        #first_run = True
        #while not val.Validate_Salary(salary) :
        #    salary = self.get_employee_data(val.Validate_Salary(salary), prompt, first_run)
        #   first_run = False

        birthday = ""
        prompt = "birthday DD-MM-YYYY: "
        first_run = True
        while not val.Validate_Birthday(birthday, age)[0]:
            birthday = self.get_employee_data(val.Validate_Birthday(birthday, age), prompt, first_run)
            first_run = False

        emp = Employee(empid, gender, age, sales, bmi, salary, birthday)
        self.all_My_Employees[empid] = emp

    def get_employee_data(self, valData, prompt, first_run):
        if first_run == False:
            print(valData[1])
        result = input("Employee's " + prompt)
        return result