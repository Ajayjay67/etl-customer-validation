import pandas as pd
import sqlite3

df = pd.read_csv('../data/customer_target.csv')
conn = sqlite3.connect('../data/customer.db')
df.to_sql('customers', conn, if_exists='replace', index=False)
print("Data loaded into SQLite database.")