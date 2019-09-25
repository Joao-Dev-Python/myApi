# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import os



app = Flask(__name__)


my_Api = [
    {
        'name' : 'Joao',
        'idade' : 25,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Ricardo',
        'idade' : 30,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Ana',
        'idade' : 25,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Paulo',
        'idade' : 26,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Daniel',
        'idade' : 13,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'GAbriela',
        'idade' : 17,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Karol',
        'idade' : 21,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Julio',
        'idade' : 33,
        'tipo' : 'pessoa'
    },
    {
        'name' : 'Vaca',
        'idade' : 5,
        'tipo' : 'animal'
    },
    {
        'name' : 'Ovelha',
        'idade' : 3,
        'tipo' : 'animal'
    },
    {
        'name' : 'Cadela',
        'idade' : 2,
        'tipo' : 'animal'
    },
    {
        'name' : 'Passáro',
        'idade' : 6,
        'tipo' : 'animal'
    },
    {
        'name' : 'Tartaruga',
        'idade' : 13,
        'tipo' : 'animal'
    },
    {
        'name' : 'Coala',
        'idade' : 1,
        'tipo' : 'animal'
    },
    {
        'name' : 'Girafa',
        'idade' : 4,
        'tipo' : 'animal'
    },
    {
        'name' : 'Macaco',
        'idade' : 7,
        'tipo' : 'animal'
    },




]

@app.route('/',methods = ['GET'])
def get_Api():
    return jsonify(my_Api)






@app.route('/<string:arg>',methods = ['GET'])
def get_Api_search(arg):

    search = [i for i in my_Api if i['tipo'] == 'pessoa' ]
    x = [i for i in my_Api if i['tipo'] == 'animal' ]

    if arg == 'pessoa':
        return jsonify(search)
    elif arg == 'animal':
        return jsonify(x)
    else :
        return jsonify([{'Error' : "Not Faund !!!"}])











port = int(os.environ.get('PORT', 5000))

if __name__== '__main__':

    app.run(host='127.0.0.1', port=port)
