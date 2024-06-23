import openpyxl
import numpy as np
from typing import Dict, Union
from PrintFile import space_print
from inspect import currentframe, getframeinfo



class Variable_store():  # содержит словарь из элементов - списков, объект класса привязан к excel файлу, из которого берутся данные.
    
    def __init__(self, VARIABLES_FILENAME: str) -> None:
        
        self._good_init = True
        
        self.workbook = openpyxl.load_workbook(VARIABLES_FILENAME)
        
        self.sheet = self.workbook.active
        
        self.__VARIABLES_FILENAME = VARIABLES_FILENAME
        
        self._variables: Dict[str, np.matrix] = {}
        
        variable_data_raw = tuple(self.sheet.columns)
        
        self.__dict_size = len(variable_data_raw)
                
        for i in range(self.__dict_size):
            one_variable_column_data = np.zeros(len(variable_data_raw[i]) - 1)  #временный массив, содержащий столбец из чисел для каждой переменной
                 
            for j in range(1, len(variable_data_raw[i])):
                
                one_variable_column_data[j - 1] = variable_data_raw[i][j].value
                
            self._variables[variable_data_raw[i][0].value] = np.matrix(one_variable_column_data)
            
                       
        if not (Variable_store.check(self)):
            self._good_init = False
            
            
    def check(self) -> bool:
        
        if not (self._good_init):
            print("Variable_store: BAD INIT")
            return False
        
        if (__class__ == "Variable_store"):
            if (self.__dict_size != len(self._variables)):
                print("Variable_store: Dict size and number of equatations are not equal, probably there are repetitive constant names")
                return False
        
        return True    
    
                
    
    def get_info(self, print_depth: int = 0) -> bool:
        
        space_print(print_depth, "Variable_store") # необходимо понять, почему при вызове __class__ подставляется Data_store
        space_print(print_depth, f"This is a dict, that stores variables from {self.__VARIABLES_FILENAME}")
        
        for key, value in self._variables.items():
            space_print(print_depth, f"{key} = {value}")
            
        if (not self.check()):
            print(getframeinfo(currentframe()))
            
            return False
        
        return True
    
    def __del__(self):
        
        workbook.remove(sheet)
            
    def get_variable_by_number(self, name, number) -> Union[float, None]: #достает из вектора - переменной по номеру определённое значение.
        
        if (not self.check()):
            print(getframeinfo(currentframe()))
            return None
        
        try:
            return (self._variables[name])[0, number] # 0 строка, столбец под номером number
               
        except KeyError:
            print(f"function {self.get_variable_by_number.__name__}, unable to find variable with that name")
            return None