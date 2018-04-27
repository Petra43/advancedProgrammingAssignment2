import pygal  # First import pygal
import plotly

class Graph():
    # Alex
    def Create_Bar(self, type, all_my_employees):
        bar_chart = pygal.Bar()
        Employee_Values = [0] * len(all_my_employees)
        count = 0
        for key, value in all_my_employees.items():
            if type == "age":
                Employee_Values[count] = value.my_age[0]
            if type == "sales":
                Employee_Values[count] = value.my_sales
            if type == "salary":
                Employee_Values[count] = value.my_salary
            count = count + 1

        bar_chart.add(type, Employee_Values)
        bar_chart.render_to_file('bar_chart_' + type + '.svg')

    # Ryan Parker
    def create_pie(self, type ,all_my_employees):
        type = type.lower()
        if type == 'bmi':
            normal = 0
            under_weight = 0
            over_weight = 0
            obesity = 0
            for emp in all_my_employees.values():
                if emp.my_bmi == 'Normal':
                    normal += 1
                elif emp.my_bmi == 'Underweight':
                    under_weight += 1
                elif emp.my_bmi == 'Overweight':
                    over_weight += 1
                elif emp.my_bmi == 'Obesity':
                    obesity += 1
            fig = {
                'data': [{'labels': ['Normal', 'Underweight', 'Overweight', 'Obesity'],
                          'values': [normal, under_weight, over_weight, obesity],
                          'type': 'pie'}],
                'layout': {
                    'title': 'BMIs of employees percentage'}
            }

            plotly.offline.plot(fig)

        elif type == 'gender':
            male = 0
            female = 0
            for emp in all_my_employees.values():
                if emp.my_gender == 'M':
                    male += 1
                elif emp.my_gender == 'F':
                    female += 1
            fig = {
                'data': [{'labels': ['Male', 'Female'],
                          'values': [male, female],
                          'type': 'pie'}],
                'layout': {
                    'title': 'comparison of employees genders'}
            }

            plotly.offline.plot(fig)