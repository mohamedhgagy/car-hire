from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__) 
  
# Connect to the database 
conn = psycopg2.connect(database="car_hire", user="postgres", 
                        password="", host="localhost", port="5432") 
cur = conn.cursor() 

@app.route('/api/customer', methods = ['GET', 'POST']) 
def customer(**kwargs):
    data = None 
    if(request.method == 'GET'): 
        cur.execute('''SELECT * FROM customer''') 
        data = cur.fetchall()
        customer_data = []
        if data:
            for record in data:
                customer_data.append(_get_vals(record)) 
        return jsonify(customer_data), 200
    
    if (request.method == 'POST'):
        data = request.json
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        ssn = data.get('ssn')
        cur.execute( 
        '''INSERT INTO customer
        (name, age, gender, ssn) VALUES (%s, %s, %s, %s)''', 
        (name, age, gender, ssn))
        # commit the changes 
        conn.commit()
        return jsonify(
                        {'name': name, 'age': age, 'gender': gender,
                         'ssn': ssn}
                        ), 201 
 
@app.route('/api/customer/<int:customer_id>', methods = ['GET']) 
def get_customer(customer_id):
    cur.execute("SELECT * FROM customer WHERE id = %s", (customer_id,)) 
    data = cur.fetchall()
    if data:
        return jsonify(_get_vals(data[0])), 200
    return jsonify([f'No customer with id {customer_id}']), 400
 
@app.route('/api/customer/<int:customer_id>', methods = ['DELETE']) 
def delete_customer(customer_id):
    cur.execute("DELETE FROM customer WHERE id = %s", (customer_id,))
    conn.commit()
    return jsonify({'message': 'Customer deleted successfully'}), 200

@app.route('/api/customer/<int:customer_id>', methods = ['PUT']) 
def update_customer(customer_id):
    data = request.json
    cur.execute(
            "UPDATE customer SET name = %s, age = %s, ssn = %s, gender = %s WHERE id = %s",
            (data['name'], data['age'], data['ssn'], data['gender'], customer_id)
        )
    conn.commit()
    return jsonify({'message': 'Customer updated successfully'}), 200
        
def _get_vals(record) -> dict:
    """ act as object to data transferer """
    data_dict = {}
    try:  
        data_dict =  dict(id= record[0], name=record[1], age=record[2], gender=record[3],
                          ssn=record[4])
        return data_dict      
    except Exception as e:
        return data_dict
if __name__ == '__main__': 
    app.run(debug=False, port=5002) 