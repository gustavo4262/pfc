from flask import Response, request
from ..services.usuarioSe import criaUsuarioSe, adicionaPacienteAMedicoSe
from ..utils.validate import validateBooleanEssential, validateStringEssential

def criaUsuarioContr():
    try:
        content = request.get_json()
        nome = content["nome"]
        senha = content["senha"]
        isMedico = content["isMedico"]
            
        validateStringEssential(nome)
        validateStringEssential(senha)

        print(isMedico)
        validateBooleanEssential(isMedico)    
        print('ok')

        criaUsuarioSe(nome, senha, isMedico)
        return Response(status=201)


    except Exception as e:
        print(e.args)
        if (e.args[0] == "Bad Request"):
            return Response(status=400)
        if (e.args[0] == "Not Found"):
            return Response(status=404)
        if (e.args[0] == "Conflict"):
            return Response(status=409)
        return Response(status=500)

def adicionaPacienteAMedicoContr():
    try:
        content = request.get_json()
        paciente = content["paciente"]
        medico = content["medico"]
        
        validateStringEssential(paciente)
        validateStringEssential(medico)

        adicionaPacienteAMedicoSe(paciente, medico)

        return Response(status=201)

    except Exception as e:
        print(e)
        if (e.args[0] == "Bad Request"):
            return Response(status=400)
        if (e.args[0] == "Not Found"):
            return Response(status=404)
        return Response(status=500)
    
