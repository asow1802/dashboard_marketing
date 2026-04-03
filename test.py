import pandas as pd
data = pd.read_csv("financial_loan.csv", sep=",")
data.head()

data.sum().isnull()
