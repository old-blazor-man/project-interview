#Author: Hector N. Chapa Jr.
#Date: 3-2-2020
#Purpose: This python scripts is the API of my application
#Which it allows the front end to communicate with this server back end.
#And Queries the database...

#MODULE IMPORT NECESSARY FOR APPLICATION..
#1.) Flask WebServer/API
#2.) Psycopg2 communicate with postresql database query purposes...
#3.) Convert the return database information into jsonify that web communication
#4.) To tell psycop2 to return dictinories instead of tuples...
#5.) JSON module converst string into object json..
import flask, psycopg2, json
from flask import request, jsonify
from psycopg2.extras import RealDictCursor


#INIATE MY APP FLASK..
app = flask.Flask(__name__, static_url_path='', 
            static_folder='public')


#Start of the Application..
@app.route("/", methods=['GET'])
def home():
    return app.send_static_file('index.html')

#Create all the routes for customer API
# I am desigining Version 1 API

# MODULE: get ALL customers from database
@app.route('/api/v1/customers', methods=['GET'])
def get_all_customers():
    #Logic To connect to database 
    #Open Cursor to perform database operation
    conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
    cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
    cursor.execute("SELECT * FROM info.customers")
    customers = cursor.fetchall() #get all records

    #Close db and cursor
    cursor.close()
    conn.close()
    #Return JSON...
    return jsonify(customers)

# MODULE: get ALL customers from database
@app.route('/api/v1/update/customer', methods=['POST'])
def update_customer():
    if request.method == "POST":
        #Logic To connect to database 
        #Open Cursor to perform database operation
        conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        email = request.form['email']
        address = request.form['address']
        dob = request.form['dob']
        customerid = request.form['customerid']
        cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
        cursor.execute("""UPDATE info.customers SET first_name = %s, 
        middle_name = %s,last_name = %s, dob = %s, address = %s, email = %s
        WHERE customerid = %s""", (fname, mname, lname, dob, address, email, customerid,))

        #Commit to the change...
        conn.commit()
        
        #Close db and cursor
        cursor.close()
        conn.close()
        #Return JSON...
        return jsonify({"success": True})

# MODULE: GET ONLY CUSTOMERS THAT HAVE ORDERS...
@app.route('/api/v1/customers/orders', methods=['GET'])
def customers_orders():
    #Logic To connect to database 
    #Open Cursor to perform database operation
    conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
    cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
    sql = """select
        json_build_object(
                'customerid', cus.customerid,
                'first_name', cus.first_name,
            	'middle_name', cus.middle_name,
                'last_name', cus.last_name,
                'email', cus.email,
                'address', cus.address,
                'dob', cus.dob,
            	'date_registered', cus.date_registered,
                'orderview', 0,
                'orders', json_agg(json_build_object(
                        'orderid', o.orderid,
                        'order_name', o.order_name,
                        'order_total', o.order_total,
                    	'order_date', o.order_date
                ))
    ) as user
from info.customers cus
inner join info.orders o on o.customerid = cus.customerid
GROUP BY 
  cus.customerid"""
    cursor.execute(sql)
    customers = cursor.fetchall() #get all records

    #Close db and cursor
    cursor.close()
    conn.close()
    #Return JSON...
    return jsonify(customers)

# MODULE: ADD NEW CUSTOMER INTO DB..
@app.route('/api/v1/add/customer', methods=['POST'])
def add_customer():
    #Logic To connect to database 
    #Open Cursor to perform database operation
    conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
    cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
    
    #IF METHOD IS POST THEN INSERT DATA...
    if request.method == 'POST':
        cursor.execute("""INSERT INTO 
        info.customers(first_name, middle_name, 
        last_name, dob, address, email, date_registered) VALUES 
        (%s, %s,%s, %s, %s, %s, %s)""", (request.form['fname'], 
        request.form['mname'], request.form['lname'], request.form['dob'], 
        request.form['address'], request.form['email'], "NOW()",))

    #Commit to the changes 
    conn.commit()
    
    #Close db and cursor
    cursor.close()
    conn.close()
    #Return JSON...
    return jsonify({"success": True})




#MODULE: GET TOTAL CUSTOMERS
@app.route('/api/v1/total/customers', methods=['GET'])
def get_total_Customers():
    #Logic To connect to database 
    #Open Cursor to perform database operation
    conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
    cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
    cursor.execute("SELECT count(*) as total FROM info.customers")
    customers = cursor.fetchall() #get all records

    #Close db and cursor
    cursor.close()
    conn.close()
    #Return JSON...
    #In this case get only the first row since there is only one row to return
    return jsonify(customers[0])



#MODULE: GET TOTAL ORDERS
@app.route('/api/v1/total/orders', methods=['GET'])
def get_total_orders():
    #Logic To connect to database 
    #Open Cursor to perform database operation
    conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
    cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
    cursor.execute("SELECT count(*) as total FROM info.orders")
    customers = cursor.fetchall() #get all records

    #Close db and cursor
    cursor.close()
    conn.close()
    #Return JSON...
    #In this case get only the first row since there is only one row to return
    return jsonify(customers[0])

#MODULE: GET TOTAL ORDERS BY CURRENT YEAR
@app.route('/api/v1/total/orders/Year', methods=['GET'])
def get_total_OrdewrsByYear():
    #Logic To connect to database 
    #Open Cursor to perform database operation
    conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
    cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
    cursor.execute("SELECT count(*) as total FROM info.orders where date_part('year', order_date) = date_part('year', CURRENT_DATE)")
    customers = cursor.fetchall() #get all records

    #Close db and cursor
    cursor.close()
    conn.close()
    #Return JSON...
    #In this case get only the first row since there is only one row to return
    return jsonify(customers[0])

# MODULE: ADD NEW CUSTOMER INTO DB..
@app.route('/api/v1/add/orders', methods=['POST'])
def add_orders():
    if request.method == 'POST':
        jsload = json.loads(request.form['orders'])
        conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
        cursor = conn.cursor(cursor_factory=RealDictCursor) #Here is where explicit tell the cursor how to handle return of the databse..
        cursor.executemany("""INSERT INTO info.orders(customerid, order_total, order_name, order_date) 
        VALUES (%(customerid)s,%(ordertotal)s, %(ordername)s, %(orderdate)s)""", jsload);
        
        #Commit to the changes 
        conn.commit()
        #Close db and cursor
        cursor.close()
        conn.close()
        return jsonify({"success": True})

# MODULE: DEL ORDER ID FROM THE DB..
@app.route('/api/v1/delete/order', methods=['POST'])
def del_orders():
    if request.method == 'POST':
        orderid = request.form['orderid']
        print(orderid)
        conn = psycopg2.connect("dbname=store user=postgres password=J1sth3b3st")
        cursor = conn.cursor() #Here is where explicit tell the cursor how to handle return of the databse..
        cursor.execute("""DELETE FROM info.orders WHERE orderid = %s""", (orderid,))
        #Commit to the changes 
        conn.commit()
        #Close db and cursor
        cursor.close()
        conn.close()
        return jsonify({"success": True})


app.run()
