from flask import Flask, request, jsonify, json, Response

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

@app.route('/products', methods=['GET'])
def products():
    sql = "SELECT * FROM product"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    listaProducts=[]

    for registro in result:
        productF ={
            "id": registro[0],
            "code": registro[1],
            "name": registro[2],
            "description": registro[3],
            "image": registro[4],
            "stock": registro[5],
            "price": registro[6]
        }
        listaProducts.append(productF)
    


    return jsonify(products = listaProducts)

# Mamejo de peticiones Add Appointment


@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':    
        code = request.json['code']
        name = request.json['name']
        description = request.json['description']
        image = request.json['image']
        stock = request.json['stock']
        price = request.json['price']
        
        
        if code == "" or name == "" or description == "" or image == "" or stock == "" or price == "":
            return jsonify(response = "bad format")
        else:
            cur = mydb.cursor()
            sql = f"INSERT INTO product (code, name, description, image, stock, price) VALUES('{code}','{name}','{description}','{image}','{stock}','{price}')"       
            cur.execute(sql)
            mydb.commit()
            return jsonify(response = "data created success")    
    else:
        return jsonify(response = "bad call")
        


@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    id = data['id']
    code = data['code']
    name = data['name']
    description = data['description']
    image = data['image']
    stock = data['stock']
    price = data['price']
    if (id == ""):
        return jsonify(response = "bad format")
    else:
        sql = f"UPDATE product SET code ='{code}', name ='{name}', description ='{description}', image ='{image}', stock ='{stock}', price ='{price}' WHERE id = {id}"
        cur = mydb.cursor()
        cur.execute(sql)
        mydb.commit()
        return jsonify(response = "data updated success")
        


@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    id = data['id']
    sql = f"DELETE FROM product WHERE id = {id}"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return jsonify(response = "data deleted success")
# Ejecutar la app en el server / en modo debug

if __name__ == "__main__":
    app.run(host="192.168.1.65", port=5000,debug=True)


