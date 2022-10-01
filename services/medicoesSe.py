from repositories.medicoesRepo import pegaListaPacientesMedicoRepo, pegaMedicaoRepo, postaMedicaoRepo
from flask import jsonify

def postaMedicaoSe(paciente, tipoDados, valor, horario):

    postaMedicaoRepo(paciente, tipoDados, valor, horario)


def pegaMedicaoSe(paciente, tipoDados):
    
    res = pegaMedicaoRepo(paciente, tipoDados)

    data = []
    for line in res:
        data.append({ "tipoDados": tipoDados,  "datatime": line[3], "valor": line[4]})

    return jsonify({'data': data})

def pegaListaPacientesMedicoSe(medico):

    res = pegaListaPacientesMedicoRepo(medico)

    data = []
    for line in res:
        data.append({ 'paciente': line[0]})

    return jsonify({'data': data})
