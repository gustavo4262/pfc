from flask import Blueprint
from ..controllers.medicoesContr import medicaoContr
from ..controllers.usuariosContr import criaUsuarioContr, adicionaPacienteAMedicoContr
from ..controlers.indexContr import indexContr

bp = Blueprint('mainBp', __name__)

bp.route('/', methods=['GET'])(indexContr)

bp.route("/medicao",  methods=['GET', 'POST'])(medicaoContr)

bp.route("/usuario", methods=["POST"])(criaUsuarioContr)

bp.route("/pacienteMedico", methods=["POST"])(adicionaPacienteAMedicoContr)






