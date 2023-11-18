
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__) 
  
# Connect to the database 
conn = psycopg2.connect(database="car_hire", user="postgres", 
                        password="", host="localhost", port="5432") 
cur = conn.cursor() 

@app.route('/api/vechile', methods = ['GET', 'POST']) 
def vechiles(**kwargs):
    data = None 
    if(request.method == 'GET'): 
        cur.execute('''SELECT * FROM vehicle''') 
        data = cur.fetchall()
        vechiles_datas = []
        if data:
            for record in data:
                vechiles_datas.append(_get_vals(record)) 
        return jsonify(vechiles_datas)
    
    if (request.method == 'POST'):
        data = request.json
        name = data.get('name')
        licence_no = data.get('licence_no')
        type = data.get('type')
        category = data.get('category')
        cur.execute( 
        '''INSERT INTO vehicle
        (name, licence_no, type, category) VALUES (%s, %s, %s, %s)''', 
        (name, licence_no, type, category))
        # commit the changes 
        conn.commit()
        return jsonify([
                        '201 created',
                        {'name': name, 'licence_no': licence_no, 'type': type,
                         'category': category}
                        ]) 
  
        
def _get_vals(record) -> dict:
    """ act as object to data transferer """
    data_dict = {}
    try:  
        data_dict =  dict(name=record[1], license_no=record[2], type=record[3],
                          category=record[4])
        return data_dict      
    except Exception as e:
        return data_dict
if __name__ == '__main__': 
    app.run(debug=False, port=5001) 