
from flask import Flask
import psycopg2

app = Flask(__name__) 
  
# Connect to the database 
conn = psycopg2.connect(database="car_hire", user="postgres", 
                        password="", host="localhost", port="5432") 
  
cur = conn.cursor()
print(cur)
if __name__ == '__main__': 
    app.run(debug=True) 