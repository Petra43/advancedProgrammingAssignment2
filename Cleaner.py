class Cleaner():

    # Ryan Parker
    def clean_empid(self, data):
        result = data.upper()
        return result
    # Ryan Parker
    def clean_gender(self, data):
        result = data.upper()
        if (result == "MALE"):
            result = "M"
        if (result == "FEMALE"):
            result = "F"
        return result

    #Alex
    def Clean_Age(self, input):
        error = ""
        new_Age = None
        try:
            new_Age = int(input)
        except ValueError:
            error = "That was not a number for age in numeric form"
            new_Age = None
        return new_Age, error

    # Ryan Parker
    def clean_bmi(self, data):
        return data.capitalize()

    #Alex
    def Clean_Birthday(self, input):
        error = ""
        new_Birthday = ""
        try:
            #Splitting it up by divisions
            seperator = ""
            str_Day = ""
            str_Month = ""
            str_Year = ""
            section_String = 1
            for char in input:
                if char.isdigit():
                    if (section_String == 1):
                        str_Day = str_Day + char

                    if (section_String == 2):
                        str_Month = str_Month + char

                    if (section_String == 3):
                        str_Year = str_Year + char
                else:
                    seperator = char
                    section_String = section_String + 1
            if len(str_Year) != 4:
                error = "The year needs to be in the full format eg: 2009"
            else:
                new_Birthday = str_Day + "-" + str_Month  + "-" + str_Year
        except:
            error = "There are no nonnumerical seperators"
            new_Birthday = ""
        if(len(new_Birthday) == 3):
           error = "There are no numbers in birthday"
           new_Birthday = ""
        if (error != ""):
            new_Birthday = ""
        return new_Birthday, error
