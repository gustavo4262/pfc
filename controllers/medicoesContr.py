from flask import Response, request
from ..services.medicoesSe import pegaMedicaoSe, postaMedicaoSe
from ..utils.validate import  validateStringEssential

def medicaoContr():
    try:
        if request.method == 'GET':
            args = request.args
            paciente = args.get("paciente")
            tipoDados = args.get("tipoDados")
            
            validateStringEssential(paciente)
            validateStringEssential(tipoDados)

            dados = pegaMedicaoSe(paciente, tipoDados)

            return dados, 200
        
        elif request.method == 'POST':
            content = request.get_json()
            paciente = content["paciente"]
            tipoDados = content["tipoDados"]
            valor = content["valor"]
            
            
            validateStringEssential(paciente)
            validateStringEssential(tipoDados)
            validateStringEssential(valor)    

            postaMedicaoSe(paciente, tipoDados, valor)
            return Response(status=201)

    except Exception as e:
        print(e)
        if (e.args[0] == "Bad Request"):
            return Response(status=400)
        if (e.args[0] == "Not Found"):
            return Response(status=404)
        return Response(status=500)
    
