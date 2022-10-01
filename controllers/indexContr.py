from flask import Response, request, jsonify
from math import sin

def indexContr():
    data = [(x, sin(x / 10.)) for x in range(0, 101)]
    return  jsonify({'data': data})