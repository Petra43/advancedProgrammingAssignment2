import unittest
from Cleaner import Cleaner
from Validator import Validator
import Reader

class CleanerTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        # be executed after each test case
        pass #print('down')

    # Ryan starts here
    def test_cleaner_empid(self):
        clean = Cleaner()
        test_data = 'A102'
        expected_result = 'A102'

        actual_result = clean.clean_empid(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_empid_2(self):
        clean = Cleaner()
        test_data = 'a102'
        expected_result = 'A102'

        actual_result = clean.clean_empid(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender(self):
        clean = Cleaner()
        test_data = 'male'
        expected_result = 'M'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender_2(self):
        clean = Cleaner()
        test_data = 'm'
        expected_result = 'M'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender_3(self):
        clean = Cleaner()
        test_data = 'female'
        expected_result = 'F'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender_4(self):
        clean = Cleaner()
        test_data = 'f'
        expected_result = 'F'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi(self):
        clean = Cleaner()
        test_data = 'normal'
        expected_result = 'Normal'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi_2(self):
        clean = Cleaner()
        test_data = 'UNDERWEIGHT'
        expected_result = 'Underweight'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi_3(self):
        clean = Cleaner()
        test_data = 'overweight'
        expected_result = 'Overweight'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi_4(self):
        clean = Cleaner()
        test_data = 'OBEsity'
        expected_result = 'Obesity'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)
    # Ryan Stops here
    # Alex starts
    def test_cleaner_age_valid_Int(self):
        clean = Cleaner()
        test_data = 99
        expected_result = 99
        actual_result = clean.Clean_Age(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_age_invalid(self):
        clean = Cleaner()
        test_data = "nine"
        expected_result = None
        actual_result = clean.Clean_Age(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_valid_1(self):
        clean = Cleaner()
        test_data = "25/11/1991"
        expected_result = "25-11-1991"
        actual_result = clean.Clean_Birthday(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_valid_2(self):
        clean = Cleaner()
        test_data = "25-11-1991"
        expected_result = "25-11-1991"
        actual_result = clean.Clean_Birthday(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_Invalid_1(self):
        clean = Cleaner()
        test_data = "2323231"
        expected_result = None
        actual_result = clean.Clean_Birthday(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_Invalid_2_response1(self):
        clean = Cleaner()
        test_data = "Hello"
        expected_result = None
        actual_result = clean.Clean_Birthday(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_Invalid_3_response1(self):
        clean = Cleaner()
        test_data = "23-11-99"
        expected_result = None
        actual_result = clean.Clean_Birthday(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_Invalid_3_response2(self):
        clean = Cleaner()
        test_data = "23-11-99"
        expected_result = "The year needs to be in the full format eg: 2009"
        actual_result = clean.Clean_Birthday(test_data)[1]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_cleaner_birthday_Invalid_3_response1(self):
        clean = Cleaner()
        test_data = "hello-break-me"
        expected_result = None
        actual_result = clean.Clean_Birthday(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))
    # Alex Stops

class ValidatorTests(unittest.TestCase):

    # Ryan Starts
    def test_validator_empid_true(self):
        val = Validator()
        employee_place_holder = ''
        test_data = 'A201'
        actual_result = val.val_empid(employee_place_holder, test_data)

        self.assertTrue(actual_result)

    def test_validator_empid_false(self):
        val = Validator()
        employee_place_holder = ''
        test_data = 'AA01'
        actual_result, error_message = val.val_empid(employee_place_holder, test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_empid_false_2(self):
        val = Validator()
        employee_place_holder = ''
        test_data = '3201'
        actual_result, error_message = val.val_empid(employee_place_holder, test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_gender_true(self):
        val = Validator()
        test_data = 'M'
        actual_result, error_message = val.val_gender(test_data)

        self.assertTrue(actual_result, error_message)

    def test_validator_gender_true_2(self):
        val = Validator()
        test_data = 'F'
        actual_result, error_message = val.val_gender(test_data)

        self.assertTrue(actual_result, error_message)

    def test_validator_gender_false(self):
        val = Validator()
        test_data = 'other'
        actual_result, error_message = val.val_gender(test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_bmi_true(self):
        val = Validator()
        data = 'Normal', 'Underweight', 'Obesity', 'Overweight'
        for x in data:
            actual_result, error_message = val.val_bmi(x)
            self.assertTrue(actual_result, error_message)

    def test_validator_bmi_false(self):
        val = Validator()
        data = 'other'
        for x in data:
            actual_result, error_message = val.val_bmi(x)
            self.assertFalse(actual_result, error_message)
    # Ryan Stops
    # Alex Starts
    def test_validator_age_valid_1(self):
        val = Validator()
        test_data = 23
        expected_result = True
        actual_result = val.Validate_Age(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_age_invalid_upper_limit(self):
        val = Validator()
        test_data = 100
        expected_result = False
        actual_result = val.Validate_Age(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_age_invalid_lower_limit(self):
        val = Validator()
        test_data = -1
        expected_result = False
        actual_result = val.Validate_Age(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_age_invalid_string(self):
        val = Validator()
        test_data = "Blah"
        expected_result = False
        actual_result = val.Validate_Age(test_data)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_birthday_valid(self):
        val = Validator()
        test_data_1 = "25-11-1991"
        test_data_2 = 26
        expected_result = True
        actual_result = val.Validate_Birthday(test_data_1, test_data_2)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_birthday_invalid_wrong_age(self):
        val = Validator()
        test_data_1 = "25-11-1991"
        test_data_2 = 27
        expected_result = False
        actual_result = val.Validate_Birthday(test_data_1, test_data_2)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_birthday_invalid_wrong_age_error_message(self):
        val = Validator()
        test_data_1 = "25-11-1991"
        test_data_2 = 27
        expected_result = "The age given and birthday do not line up"
        actual_result = val.Validate_Birthday(test_data_1, test_data_2)[1]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_birthday_invalid_not_date(self):
        val = Validator()
        test_data_1 = "11-25-1991"
        test_data_2 = 27
        expected_result = False
        actual_result = val.Validate_Birthday(test_data_1, test_data_2)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_birthday_invalid_not_date_error_message(self):
        val = Validator()
        test_data_1 = "11-25-1991"
        test_data_2 = 27
        expected_result = "Birthday is not a valid date"
        actual_result = val.Validate_Birthday(test_data_1, test_data_2)[1]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

    def test_validator_birthday_invalid_string_age(self):
        val = Validator()
        test_data_1 = "11-25-1991"
        test_data_2 = "Yahhh"
        expected_result = False
        actual_result = val.Validate_Birthday(test_data_1, test_data_2)[0]
        self.assertEqual(actual_result, expected_result, "actaul_result should equal" + str(expected_result))

if __name__ == '__main__':
    unittest.main()