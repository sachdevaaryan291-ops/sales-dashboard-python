import pandas as pd
from sqlalchemy import create_engine


file_path = r"C:\Users\Amish\OneDrive\Desktop\Computed insight - Success of active sellers.csv"
df = pd.read_csv(file_path)


username = 'root'
password = 'root123'  # Change this if needed
host = 'localhost'
port = '3307'         # Use 3306 if 3307 is not default on your MySQL
database = 'sales_dashboard'


engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")


df.to_sql(name='sales_data', con=engine, if_exists='replace', index=False)

print("✅ Data uploaded successfully to MySQL!")
