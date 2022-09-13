from repositories.usuarioRepo import criaUsuarioRepo, adicionaPacienteAMedicoRepo

def criaUsuarioSe(nome, senha, isMedico):
    try:
        criaUsuarioRepo(nome, senha, isMedico=="True")
    except Exception as e:
        if 'violates' in e.args[0] and 'constraint' in e.args[0]:
            raise Exception("Conflict")
        else:
            raise e

def adicionaPacienteAMedicoSe(paciente, medico):
    
    adicionaPacienteAMedicoRepo(paciente, medico)

