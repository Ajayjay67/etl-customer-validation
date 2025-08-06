import pandas as pd
import sqlite3

df_csv = pd.read_csv('../data/customer_target.csv')
conn = sqlite3.connect('../data/customer.db')
df_db = pd.read_sql('SELECT * FROM customers', conn)

print("Validation Passed?", df_csv.equals(df_db))