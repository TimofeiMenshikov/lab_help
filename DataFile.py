from ConstantFile import Constant_store
from VariableFile import Variable_store
from PrintFile import space_print
from inspect import currentframe, getframeinfo
import numpy as np
from typing import Union

class Data_store(Constant_store, Variable_store):
    
    def __init__(self, CONSTANTS_FILENAME: str, VARIABLES_FILENAME: str) -> None:
        
        self._good_init = True
        
        Constant_store.__init__(self, CONSTANTS_FILENAME)
        
        if not self._good_init:  # self._good_init - одна переменная для всех классов, поэтому в начале инита она переставляется в True => надо проверять на True/False, после каждого инита, что логично
            print(getframeinfo(currentframe()))
            return 
             
        Variable_store.__init__(self, VARIABLES_FILENAME)
        
        if not self._good_init:
            print(getframeinfo(currentframe()))
            return
        
        self._data: Dict[str, Union[int, np.matrix]] = {**self._constants, **self._variables}
            
        if (not Data_store.check(self)):
            print(getframeinfo(currentframe()))
            self._good_init = False


    def check(self) -> bool:
        
        if not (self._good_init):
            print("Data_store: BAD INIT")
            return False
        
        if not (Constant_store.check(self)):
            return False
        
        if not (Variable_store.check(self)):
            return False
        
        if len(self._data) != (len(self._constants) + len(self._variables)):
            print("len(self._data) != len(self._constants) + len(self._variables)")
            return False
        
        return True
        
        
    def get_info(self, print_depth: int = 0) -> bool:
        
        space_print(print_depth, "Data_store")
        space_print(print_depth, "this is union of variables data and constant data")
        space_print(print_depth, "parents")
        space_print(print_depth, '{')
        Constant_store.get_info(self, print_depth + 1)
        Variable_store.get_info(self, print_depth + 1)
        space_print(print_depth, '}')
        
        if (not self.check()):
            print(getframeinfo(currentframe()))
            
            return False
        
        return True
        
        
    def add_new_variable(self, expression: str, variable_name: str, write_to_file: bool = False) -> bool: # добавляет пременную  variable_name = expression, не понятно как отлавливать ошибки 
        
        if not (self.check()):
            print(getframeinfo(currentframe()))
            return False
        
        
        if variable_name in self._data.keys():
            print("name is already have used")
            return False
        
        value: Union[float, np.matrix] = eval(expression,  {},  {**self._constants, **self._variables}) # второй аргумент - глобальные переменные, третий аргумент - локальные переменные

        if type(value) == np.matrix:       # если тип - матрица, то записываем в переменные, иначе записываем в константы
            self._variables[variable_name] = value
            
            print(f"variable {variable_name} has added sucessfully")
                
        else:                              
            self._constants[variable_name] = value
            
            if (write_to_file):
                with open(self._CONSTANTS_FILENAME, "a") as constants_file:
                    constants_file.write(f"\n{variable_name} = {value}")
                
            print(f"constant {variable_name} has added sucessfully")
        
        self._data[variable_name] = value
        
        return True
    
    def __del__(self):
        Variable_store.__del__()
        Constant_store.__del__()
        
        


   
        
        
            