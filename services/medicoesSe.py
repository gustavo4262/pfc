from repositories.medicoesRepo import pegaMedicaoRepo, postaMedicaoRepo
from flask import jsonify

def postaMedicaoSe(paciente, tipoDados, valor):

    postaMedicaoRepo(paciente, tipoDados, valor)


def pegaMedicaoSe(paciente, tipoDados):
    
    res = pegaMedicaoRepo(paciente, tipoDados)

    data = []
    for line in res:
        data.append({ "tipoDados": tipoDados,  "datatime": line[3], "valor": line[4]})

    return jsonify({'data': data})

