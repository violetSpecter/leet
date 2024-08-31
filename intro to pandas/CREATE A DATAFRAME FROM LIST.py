
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # this is how we create a dataframe in pandas out of a list
    # providing the column names
    sd = pd.DataFrame(student_data, columns = ['student_id', 'age'])
    
    # answer
    return sd