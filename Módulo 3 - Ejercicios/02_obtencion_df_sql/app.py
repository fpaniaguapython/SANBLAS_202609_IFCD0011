import sqlite3

import pandas as pd

conn = sqlite3.connect('./bbdd_peliculas.db')

df = pd.read_sql('SELECT * FROM peliculas WHERE anyo_estreno>1990', conn)

conn.close()

print(df.head())