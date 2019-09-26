# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import os



app = Flask(__name__)


my_Api = [
    {
        'vaga' : 'Pedeiro',
        'descricao_brev' : 'trabalhar muito fazer obras de arte e nao receber valor merecido',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Auxiliar',
        'descricao_brev' : 'quenm mais trabalha e menos recebe',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Gerente',
        'descricao_brev' : 'so de buenas mandando em tudo',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'almoxerife',
        'descricao_brev' : 'ficar de boa entregando equipamentos e ferramentas',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Encarregado de obra',
        'descricao_brev' :'puchar um saco do supervisor e engenheiro',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Gestor de producao',
        'descricao_brev' : 'ficar de boa vendo os outros trabalhar o dia todo',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Moto boy',
        'descricao_brev' : 'da uns role',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Motorista',
        'descricao_brev' :'dirigir onibus',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Soldaor',
        'descricao_brev' : 'solda nos 3 processos ',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Caldereiro',
        'descricao_brev' : 'cortar tubulacoes',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Ispetor de Qualidade',
        'descricao_brev' : 'verificar sevicos',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Operador de Guidaste',
        'descricao_brev' : 'levantar peso',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Proxtibuider',
        'descricao_brev' : 'pegar altas negas',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Garcon',
        'descricao_brev' : 'servir clientes',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Cobrador',
        'descricao_brev' : 'Trabalhar com dinheiro que nao e seu',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },
    {
        'vaga' : 'Operador de Caixa',
        'descricao_brev' : 'Trabalhar pra casete',
        'descricao_com' : 'Trabalhar de domingo a domingo ate Morrer'
    },




]

@app.route('/',methods = ['GET'])
def get_Api():
    return jsonify(my_Api)






@app.route('/<string:arg>',methods = ['GET'])
def get_Api_search(arg):

    search = [i for i in my_Api if i['descricao_com'] == 'Trabalhar de domingo a domingo ate Morrer' ]
    x = [i for i in my_Api if i['descricao_com'] == 'Trabalhar de domingo a domingo ate Morrer' ]

    if arg == 'Trabalhar de domingo a domingo ate Morrer':
        return jsonify(search)
    elif arg == 'Trabalhar de domingo a domingo ate Morrer':
        return jsonify(x)
    else :
        return jsonify([{'Error' : "Not Faund !!!"}])













if __name__== '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
