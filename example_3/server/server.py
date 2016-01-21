# coding: utf-8

import datetime

from pymongo.mongo_client import MongoClient

from flask import Flask, request, render_template


app = Flask(__name__)

def create_doc(collection, value, date):
    collection.insert_one({'value': value, 'date': date})

@app.route('/', methods=['POST', 'GET'])
def index():
    mongo_client = MongoClient('localhost', 27017)

    db_corridor = mongo_client.corridor
    collection_corridor_light = db_corridor.light

    if (request.method == 'POST' and 
            'light' in request.form and 
            'date' in request.form):
        try:
            doc_corridor_light_latest = list(
                collection_corridor_light.find().sort('date', -1).limit(1)
            )[0]
        except IndexError:
            create_doc(
                    collection_corridor_light, 
                    request.form['light'],
                    datetime.datetime.strptime(request.form['date'], '%Y.%m.%d %H:%M:%S'))
        else:
            if doc_corridor_light_latest['value'] != request.form['light']:
                create_doc(
                    collection_corridor_light, 
                    request.form['light'],
                    datetime.datetime.strptime(request.form['date'], '%Y.%m.%d %H:%M:%S'))
        
        return u'true'
    return render_template('index.html', corridor_lights=collection_corridor_light.find().sort('date', -1))

if __name__ == '__main__':
    app.debug = True
    app.run()