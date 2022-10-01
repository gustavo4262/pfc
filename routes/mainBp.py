from flask import Blueprint
from controllers.medicoesContr import medicaoContr, pegaListaPacientesMedico
from controllers.usuariosContr import fazLoginContr, criaUsuarioContr, adicionaPacienteAMedicoContr
from controllers.indexContr import indexContr

bp = Blueprint('mainBp', __name__)

bp.route('/', methods=['GET'])(indexContr)

bp.route('/lista-pacientes', methods=['GET'])(pegaListaPacientesMedico)

bp.route("/medicao",  methods=['GET', 'POST'])(medicaoContr)

bp.route("/faz-login", methods=["POST"])(fazLoginContr)

bp.route("/cria-login", methods=["POST"])(criaUsuarioContr)

bp.route("/paciente-medico", methods=["POST"])(adicionaPacienteAMedicoContr)






