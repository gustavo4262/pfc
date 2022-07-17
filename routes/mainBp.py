from flask import Blueprint
from ..controllers.medicoesContr import medicaoContr
from ..controllers.usuariosContr import criaUsuarioContr, adicionaPacienteAMedicoContr

bp = Blueprint('mainBp', __name__)

bp.route("/medicao",  methods=['GET', 'POST'])(medicaoContr)

bp.route("/usuario", methods=["POST"])(criaUsuarioContr)

bp.route("/pacienteMedico", methods=["POST"])(adicionaPacienteAMedicoContr)






