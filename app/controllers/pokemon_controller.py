from flask import Blueprint, request, jsonify
from services.pokemon import buscar_pokemon

pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/pokemon', methods=['GET'])
def buscar():
    nombre = request.args.get('nombre')
    tipo = request.args.get('tipo')

    if not nombre and not tipo:
        return jsonify({"error": "Debes enviar un nombre o tipo"}), 400

    resultado = buscar_pokemon(nombre, tipo)
    return jsonify(resultado)
