from DataFile import Data_store
            
            
if __name__ == "__main__":
    
    CONSTANTS_FILENAME = "constants.txt"
    
    VARIABLES_FILENAME = "variable_data.xlsx"
    
    
    
    data_store = Data_store(CONSTANTS_FILENAME, VARIABLES_FILENAME)

    data_store.add_new_variable("x - y", "value3", write_to_file = True)
        
    data_store.get_info()    
    
    
    
                

            
        
