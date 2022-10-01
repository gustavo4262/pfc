from repositories.usuarioRepo import criaUsuarioRepo, adicionaPacienteAMedicoRepo, fazLoginRepo
from flask import jsonify

def fazLoginSe(nome, senha):

    result = fazLoginRepo(nome, senha)

    if result == "paciente":
        return jsonify({"isMedic": False})
    else:
        return jsonify({"isMedic": True})



def criaUsuarioSe(nome, senha, isMedico):
    try:
        criaUsuarioRepo(nome, senha, isMedico=="1")
    except Exception as e:
        if 'violates' in e.args[0] and 'constraint' in e.args[0]:
            raise Exception("Conflict")
        else:
            raise e

def adicionaPacienteAMedicoSe(paciente, medico):
    
    adicionaPacienteAMedicoRepo(paciente, medico)

