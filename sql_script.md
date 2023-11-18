-- Create the vehicle table
CREATE TABLE vehicle (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    licence_no VARCHAR(20),
    type VARCHAR(50),
    category VARCHAR(50)
);

-- Create the customer table
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    gender VARCHAR(10),
    ssn VARCHAR(20) UNIQUE
);

-- Create the booking table
CREATE TABLE booking (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE
   
);

-- Create the invoice table
CREATE TABLE invoice (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    amount NUMERIC(10, 2)
);

ALTER TABLE booking
ADD COLUMN customer_id INTEGER REFERENCES customer(id),
ADD COLUMN vehicle_id INTEGER REFERENCES vehicle(id),
ADD COLUMN invoice_id INTEGER REFERENCES invoice(id);

ALTER TABLE invoice
ADD COLUMN customer_id INTEGER REFERENCES customer(id),
ADD COLUMN booking_id INTEGER REFERENCES booking(id),
ADD COLUMN vehicle_id INTEGER REFERENCES vehicle(id);