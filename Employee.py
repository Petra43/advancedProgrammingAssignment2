# Ryan Parker whole file
class Employee(object):

    my_empid = ''
    my_gender = ''
    my_age = 0
    my_sales = 0
    my_bmi = ''
    my_salary = 0
    my_birthday = ''

    def __init__(self, empid, gender, age, sales, bmi, salary, birthday):
        self.my_empid = empid
        self.my_gender = gender
        self.my_age = age
        self.my_sales = sales
        self.my_bmi = bmi
        self.my_salary = salary
        self.my_birthday = birthday
