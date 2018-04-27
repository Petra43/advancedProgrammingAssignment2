from Controller import *
import sys
from Graph import *
# Alex whole file
try:
    b = Model_Handler(sys.argv[1])
    Controller(b).Go()
except:
    b = Model_Handler(None)
    Controller(b).Go()


# sam = Employee("EAt333", "M", 26, 2230, "normal", 4300, "25/11/1991" )
# jeff = Employee("EAt332", "M", 27, 2234, "normal", 1234, "25/11/1990" )
# bill = Employee("EAt331", "M", 28, 2890, "normal", 5600, "25/11/1989" )
# alex = Employee("EAt330", "M", 29, 1234, "normal", 2345, "25/11/1988" )
# ryan = Employee("EAt324", "M", 30, 560, "normal", 4567, "25/11/1987" )
# susan = Employee("EAt321", "M", 31, 2230, "normal", 1234, "25/11/1986" )
# kate = Employee("EAt320", "M", 32, 2230, "normal", 3245, "25/11/1985" )
# florence = Employee("EAt234", "M", 33, 2230, "normal", 9899, "25/11/1984" )
# jezus = Employee("EAt456", "M", 34, 2230, "normal", 4300, "25/11/1983" )
# wolo = Employee("EAt678", "M", 35, 2230, "normal", 4300, "25/11/1982" )
# bolo = Employee("EAt897", "M", 36, 2230, "normal", 4300, "25/11/1981" )
#
# All_My_Employees = {}
# All_My_Employees[sam.my_empid] = sam
# All_My_Employees[jeff.my_empid] = jeff
# All_My_Employees[bill.my_empid] = bill
# All_My_Employees[alex.my_empid] = alex
# All_My_Employees[ryan.my_empid] = ryan
# All_My_Employees[susan.my_empid] = susan
# All_My_Employees[kate.my_empid] = kate
# All_My_Employees[florence.my_empid] = florence
# All_My_Employees[jezus.my_empid] = jezus
# All_My_Employees[wolo.my_empid] = wolo
# All_My_Employees[bolo.my_empid] = bolo
#
# myGraph = Graph()
# myGraph.Create_Bar("age", All_My_Employees)


