import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("population.csv")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "age": "Integer",
    "total": "Integer",
    "male": "Integer",
    "female": "Integer"
}
df.to_sql(name='dashboard_population', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")

df= pd.read_csv("hospital.csv")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype= {
    "name": "CharField",
    "type": "CharField",
    "type_short": "CharField",
    "tel": "CharField",
    "zip" : "Integer",
    "add" : "CharField",
    "place" : "CharField"
}
df.to_sql(name='dashboard_hospital', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()
