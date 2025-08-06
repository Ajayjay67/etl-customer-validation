import pandas as pd

df = pd.read_csv('../data/customer_source.csv')
df['JoinDate'] = pd.to_datetime(df['JoinDate']).dt.strftime('%Y-%m-%d')
df.to_csv('../data/customer_target.csv', index=False)
print("Transformation complete. Data saved to customer_target.csv.")