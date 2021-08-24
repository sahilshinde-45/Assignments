import pandas as pd

employee_data = pd.read_csv("Employees.csv", index_col=False, delimiter='[,,|,;]')
employee_data.head()
