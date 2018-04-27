from Model_Handler import *

class Controller():
    def __init__(self, model_Handler):
        self.Model_Handler = model_Handler
    def Go(self):
        current_CMD = My_CMD(self.Model_Handler)
        current_CMD.cmdloop()