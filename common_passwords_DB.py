import pandas as pd

table = pd.read_csv("common_passwords.csv", sep=",")

common_passwords = set(table['password'])


