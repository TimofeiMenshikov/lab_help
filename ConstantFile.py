#файл с классами, связанными с хранением констант

from PrintFile import space_print
from typing import Dict, Union
from inspect import currentframe, getframeinfo

class Const_dict(dict): # стандартный словарь, из которого выпилены некоторые функции, которые могут изменить его (однако всё еще уязвим)

    def pop(self):
        print(f"not allowed to use {__name__} function to {self.__class__} element")
        
    def push(self):
        print(f"not allowed to use {__name__} function to {self.__class__} element")
        
    def clear(self):
        print(f"not allowed to use {__name__} function to {self.__class__} element")
        
    def popitem(self):
        print(f"not allowed to use {__name__} function to {self.__class__} element")
        

        
        
class Constant_store:   # объект данного класса содержит объект класса Const_dict, привязывая его к текстовому файлу , содержащему константы
        
    def __init__ (self, CONSTANTS_FILENAME: str) -> None:
        
        self._good_init = True
        
        self._CONSTANTS_FILENAME = CONSTANTS_FILENAME
        
        with open(CONSTANTS_FILENAME, "r") as CONSTANTS_FILE:
        
            constant_data = CONSTANTS_FILE.readlines()
            
            print(type(CONSTANTS_FILE))
            
            print(constant_data)
            
            self._constants: Dict[str, int] = Const_dict()
            
            self.__dict_size = len(constant_data)
            
            for equation_number in range(self.__dict_size):
                
                constant_name, constant_value = self.__get_constant_equation(constant_data[equation_number])
                
                self._constants[constant_name] = constant_value
                        
        if not (Constant_store.check(self)):
            self._good_init = False


    #def __readlines(self, CONSTANTS_FILE):
    

    def __get_constant_equation(self, equation_string: str) -> tuple:     # парсинг строки вида "x = 5", посредством убирания пробелов и символа =. Метод привязан к __init__ и не требует проверки объекта, потому что он ещё не создан.
        
        constant_name, constant_value_string = equation_string.split('=')
        
        constant_name = constant_name.replace(' ', '')
        
        constant_value = float(constant_value_string)
        
        return (constant_name, constant_value)            
                
                
    def check(self) -> bool:
        
        if not (self._good_init):
            print("Constant_store: BAD INIT")
            return False
        
        if (__class__ == "Constant_store"):
            if (self.__dict_size != len(self._constants)):
                print("Constant_store: Dict size and number of equatations are not equal, probably there are repetitive constant names")
                return False
        
        return True    
        
        
    def get_info(self, print_depth: int = 0) -> bool:
                      
        space_print(print_depth, "Constant_store")
        space_print(print_depth, f"This is a dict, that stores constants from {self._CONSTANTS_FILENAME}. Do not remove, add or change dict elements!!!")
        
        for key, value in self._constants.items():
            space_print(print_depth, f"{key} = {value}")
        
        if not (self.check()):
            print(getframeinfo(currentframe()))
            return False
        
        return True
    
    
        
    def get_constant(self, name: str) -> Union[float, None]:
        
        if (not self.check()):
            print(getframeinfo(currentframe()))
            return None
        
        try:
            return self._constants[name]
        
        except KeyError:
            print(f"function {self.get_constant.__name__}, unable to find constant with that name") # почему то, если писать просто __name__ и вызывать из другого файла, то выдает название файла, в котором находится функция
            
            return None
        
        
            