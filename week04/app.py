from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## 달달한 맛
@app.route('/')
def homework():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.homework.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.homework.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


## 짭잡한 맛
@app.route('/my-shopping')
def my_homework():
    return render_template('my-shopping.html')


@app.route('/my_order', methods=['POST'])
def my_order():
    name_receive = request.form['order_name']
    count_receive = request.form['order_count']
    address_receive = request.form['order_address']
    phone_receive = request.form['order_phone']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.my_homework.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/my_order', methods=['GET'])
def my_orders():
    orders = list(db.my_homework.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'my_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)