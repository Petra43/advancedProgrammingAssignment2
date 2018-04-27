from cmd import Cmd
from Model_Handler import *
import tkinter as tk
from tkinter import filedialog


class My_CMD(Cmd):

    def __init__(self, model_Handler):
        Cmd.__init__(self)
        self.My_Model_Handler = model_Handler
        self.My_Model_Handler.Create_DDB()
        self.prompt = ">>> "
        self.intro = "Welcome to BCPR301_Ass1 Interpreter \nIf help with options is needed type 'help'"

    def do_ImportFile(self, file_type):
       """
        Syntax: ImPortFile(file_type)
        Adds all new employees from file to Model_Handler.All_My_Employees
        param: file_type : a string representing what type of file it is. Options: txt, xml, csv
        returns: None
       """

        # Alex
       if file_type not in ["txt", "csv", "xml"]:
            print("Please specify a file type")
       else:
           root = tk.Tk()
           root.withdraw()
           file_path = filedialog.askopenfilename()
           my_Reader = Reader()

           # Ryan parker
           if file_type == "txt":
               self.My_Model_Handler.load_txt()
           # Alex
           if file_type == "xml":
               self.My_Model_Handler.all_My_Employees.update(my_Reader.XML_Reader(file_path, self.My_Model_Handler.error_File, self.My_Model_Handler.all_My_Employees))

           if file_type == "csv":
               pass

    # Ryan Parker
    def do_load(self, line):
        """
        Syntax: loads from database
        Retrives data from the database
        Prints 'data retrived' if successful or errors if not
        returns: none
        """
        self.My_Model_Handler.Get_All_Employees_Database()

    # Ryan Parker
    def do_SaveNewEmployees(self, line):
        """
        Syntax: SaveNewEmployees
        Saves all newly Added Employees to database
        Prints 'Database updated' if successful or errors if not
        returns: none
        """
        self.My_Model_Handler.Save_New_Employees_Database()
        print("Database updated")

    # Ryan Parker
    def do_saveTXT(self, line):
        """
        Syntax: SaveNewEmployees
        Saves all newly Added Employees to a txt file
        Prints 'saved to file sucessfuly' or errors
        returns: none
        """

        self.My_Model_Handler.save_to_txt()

    def do_InputEmployee(self, line):
        """
        syntax: InputEmployee()
        Asks user for inputs for a new Employee
        Adds new single employee to all_My_Employees
        returns: none
        """
        self.My_Model_Handler.add_employee()
    # Alex
    def do_Graph(self, typeGraph):
        """
        syntax: Graph(self, typeGraph, value1, value2)
        Displays a graph with the two values given or the error as to why it can not be displayed
        param: typeGraph : A string with the type of graph wanted eg: Bar, Pie, Line
        returns: none
        """
        # Alex
        if(typeGraph == "bar"):
            data = input("What data do you want displayed? (age, salary, sales)")
            self.My_Model_Handler.CreateBar(data, self.My_Model_Handler.all_My_Employees)
        # Ryan Parker
        elif typeGraph == "pie":
            data = input("What data do you want displayed? (gender, bmi)")
            self.My_Model_Handler.create_pie(data)
        else:
            print("please input a valid graph type: bar, pie")

        # If typeGraph == scatter
        # createScatterGraph

        # If typeGraph == pie
        # createPieGraph

        # If values cannot be represented in graph print why they cannot

    def do_ShowEmployees(self, line):
        """
        syntax: do_ShowEmployees()
        Prints a list of all the EMPID's that are present in all_my_employees
        returns: none
        """
        for key in self.My_Model_Handler.all_My_Employees:
            print(key)

    def do_quit(self, line):
        """
        Quit from MyCMD
        return: True
        """
        want_save = input("Do you wish to save new Employees to Database? Y/N")
        while(want_save not in ["y", "Y", "n", "N"]):
            want_save = input("Do you wish to save new Employees to Database? Y/N")
        if(want_save in ["y","Y"]):
            self.My_Model_Handler.Save_New_Employees_Database();
            print("Database Updated")
        print("Quitting ......")
        return True
