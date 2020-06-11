from flask import Flask, request, jsonify

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="products"
)

app = Flask(__name__)

#settings

#form = AppointmentForm(request.form)

# Rutas

@app.route('/readproduct', methods=['GET'])
def readproduct():
    sql = "SELECT * FROM product"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return jsonify(data = result)

@app.route('/readproductid/<id>', methods=['GET'])
def readproductid(id):
    sql = f"SELECT * FROM product WHERE id= {id}"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return jsonify(data = result)

# Mamejo de peticiones Add Appointment


@app.route('/addproduct', methods=['POST'])
def addproduct():
    if request.method == 'POST':    
        code = request.json['code']
        name = request.json['name']
        description = request.json['description']
        image = request.json['image']
        stock = request.json['stock']
        price = request.json['price']
        
        if (code == "" or name == "" or description == "" or image == "" or stock == "" or price == ""):
            return jsonify(response = "bad format")
        else:
            cur = mydb.cursor()
            sql = f"INSERT INTO product (code, name, description, image, stock, price) VALUES('{code}','{name}','{description}','{image}','{stock}','{price}')"       
            cur.execute(sql)
            mydb.commit()
            return jsonify(response = "data created success")    
    else:
        return jsonify(response = "bad call")


@app.route('/updateproduct/<id>', methods=['POST'])
def updateproduct(id):
    if request.method == 'POST':
        code = request.json['code']
        name = request.json['name']
        description = request.json['description']
        image = request.json['image']
        stock = request.json['stock']
        price = request.json['price']

        if (code == "" or name == "" or description == "" or image == "" or stock == "" or price == ""):
            return jsonify(response = "bad format")
        else:
            sql = f"UPDATE product SET code ='{code}', name ='{name}', description ='{description}', image ='{image}', stock ='{stock}', price ='{price}' WHERE id = {id}"
            cur = mydb.cursor()
            cur.execute(sql)
            mydb.commit()
            return jsonify(response = "data updated success")
    else:
        return jsonify(response = "bad call")
        


@app.route('/deleteproduct/<id>', methods=['DELETE'])
def deleteproduct(id):
    sql = f"DELETE FROM product WHERE id = {id}"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return jsonify(response = "data deleted success")

    
# Ejecutar la app en el server / en modo debug

if __name__ == "__main__":
    app.run(host="localhost", port=5000 ,debug=True)
