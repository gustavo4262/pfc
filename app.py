from flask import Flask
from flask_cors import CORS

from routes.mainBp import bp

app = Flask(__name__)
cors = CORS(app)

app.config["SSL_DISABLE"] = True
app.config["JSON_SORT_KEYS"] = False

app.register_blueprint(bp)
