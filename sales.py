# ==========================================
# SALES DATA ANALYTICS PROJECT
# ERROR FREE VERSION
# ==========================================

# ---------- IMPORT LIBRARIES ----------

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# ---------- LOAD CSV FILE ----------

df = pd.read_csv(
    "Sample - Superstore.csv",
    encoding='latin1'
)

print("CSV FILE LOADED SUCCESSFULLY")

# ---------- SHOW FIRST 5 ROWS ----------

print("\nFIRST 5 ROWS")

print(df.head())

# ---------- COLUMN NAMES ----------

print("\nCOLUMN NAMES")

print(df.columns)

# ---------- NULL VALUES ----------

print("\nNULL VALUES")

print(df.isnull().sum())

# ---------- TOTAL SALES ----------

print("\nTOTAL SALES")

print(df['Sales'].sum())

# ---------- TOTAL PROFIT ----------

print("\nTOTAL PROFIT")

print(df['Profit'].sum())

# ---------- REGION WISE SALES ----------

print("\nREGION WISE SALES")

region_sales = df.groupby('Region')['Sales'].sum()

print(region_sales)

# ---------- MYSQL CONNECTION ----------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sindhu@17",
    database="sales"
)

print("\nMYSQL CONNECTED SUCCESSFULLY")

cursor = conn.cursor()

# ---------- READ MYSQL TABLE ----------

cursor.execute("SELECT * FROM `sample - superstore`")

result = cursor.fetchall()

print("\nMYSQL DATA")

for row in result[:5]:
    print(row)

# ---------- SEABORN GRAPH ----------

sns.barplot(
    x='Category',
    y='Sales',
    data=df
)

plt.xticks(rotation=45)

plt.title("Category Wise Sales")

plt.show()

# ---------- REQUESTS API ----------

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print("\nAPI DATA")

print(data[:2])

# ---------- CLOSE MYSQL CONNECTION ----------

cursor.close()

conn.close()

print("\nPROJECT COMPLETED SUCCESSFULLY")