import pandas as pd

employee_data = pd.read_csv("Employees.csv", index_col=False, delimiter = ',' or '|' or ';' , engine='python')

employee_data.head()
