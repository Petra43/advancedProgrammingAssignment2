import xml.etree.ElementTree as ET
from Employee import Employee # Ryan: changed the star to employee dont know if it will break your code or not
from Validator import Validator
from Cleaner import Cleaner

class Reader():

    # Alex
    def XML_Reader(self, file_Location, error_File_Location, all_employees): # Add validate
        MyCleaner = Cleaner()
        my_Employees = {}
        tree = ET.parse(file_Location)
        root = tree.getroot()
        for user in root.findall('user'):
            # Need to Validate all given data
            empid = user.get('EMPID')
            gender = user.find('gender').text
            age = user.find('age').text
            sales = user.find('sales').text
            bmi = user.find('BMI').text
            salary = user.find('salary').text
            birthday = user.find('birthday').text
            #For each item in new Employee need to check that they have a value after being vlaidated
            new_Employee = Employee(MyCleaner.clean_empid(empid), MyCleaner.clean_gender(gender),
                                    MyCleaner.Clean_Age(age)[0], int(sales),
                                    MyCleaner.clean_bmi(bmi), int(salary.replace(',', '')),
                                    MyCleaner.Clean_Birthday(birthday)[0])
            my_Employees[new_Employee.my_empid] = new_Employee


            # clean_Data = True
            #
            # for item in [empid, gender, age, sales, bmi, salary, birthday]:
            #     if item[0] == False:
            #         clean_Data = False
            #
            # if(clean_Data):
            #     new_Employee = Employee(MyCleaner.clean_empid(empid), MyCleaner.clean_gender(gender), MyCleaner.Clean_Age(age), MyValidator.Validate_Sales(sales), MyCleaner.clean_bmi(bmi), MyValidator.Validate_Salary(salary), MyCleaner.Clean_Birthday(birthday))
            #     my_Employees[new_Employee.EMPID] = new_Employee
            # else:
            #     #write to errorlogFile
            #     pass

        return my_Employees

    # Alex
    def read_Config(self, file_Location):
        tree = ET.parse(file_Location)
        root = tree.getroot()
        config_user = root.findall('user')[0].text
        config_error_file = root.findall('errorFile')[0].text
        for database in root.findall('database'):
            config_ddb_location = database.find('location').text
            config_ddb_username = database.find('username').text
            config_ddb_password = database.find('password').text
        return config_user,config_error_file, config_ddb_location, config_ddb_username, config_ddb_password

    # Ryan Parker
    def read_file_txt(self,all_my_employees):

        with open("test_data_txt.txt", "r") as file:
            data = file.readlines()
            clean = Cleaner()
            val = Validator()
            for line in data:
                valid = True
                emp = line.split(",")

                empid = clean.clean_empid(emp[0])
                if val.val_empid(all_my_employees, empid)[0] == False:
                    valid = False
                    print("empid")

                gender = clean.clean_gender(emp[1])
                if val.val_gender(gender)[0] == False:
                    valid = False
                    print("gender")

                age = clean.Clean_Age(emp[2])
                if val.Validate_Age(age[0])[0] == False:
                    valid = False
                    print("age")

                sales = emp[3]

                bmi = clean.clean_bmi(emp[4])
                if val.val_bmi(bmi)[0] == False:
                    valid = False
                    print("bmi")

                salary = emp[5]

                # there is an issue with the validation of the test data's birthdays
                birthday = clean.Clean_Birthday(emp[6])
                # if val.Validate_Birthday(birthday, age[0]+ 1 )[0]:
                #     pass
                # else:
                #     valid = False
                #     print("birthday")

                if valid != False:
                    employee = Employee(empid, gender, age[0], sales, bmi, salary, birthday[0])
                    all_my_employees[empid] = employee
                else:
                    print("Failed to add employee")
        return all_my_employees

    # Ryan Parker
    def write_file_txt(self, employees):

        file = open("employees.txt", "w")
        try:
            for emp in employees.values():
                empid = emp.my_empid
                gender = emp.my_gender
                age = str(emp.my_age)
                sales = str(emp.my_sales)
                bmi = emp.my_bmi
                salary = str(emp.my_salary)
                birthday = str(emp.my_birthday)
                new_file = empid + "," + gender + "," + age + "," + sales + "," + bmi + "," + salary + "," + birthday + "/n"
                file.write(new_file)
            print("saved to file sucessfuly")
        except:
            print("failed to save file")
        file.close()

