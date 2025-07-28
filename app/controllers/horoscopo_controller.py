from flask import Blueprint, request, jsonify
from services.horoscopo import obtener_pokemon_horoscopo
from datetime import datetime

horoscopo_bp = Blueprint('horoscopo', __name__)

@horoscopo_bp.route('/horoscopo', methods=['POST'])
def horoscopo():
    datos = request.get_json()
    nombre = datos.get("nombre")
    fecha = datos.get("fecha_nacimiento")

    if not nombre or not fecha:
        return jsonify({"error": "Faltan datos (nombre o fecha_nacimiento)"}), 400

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Fecha inválida, usa formato YYYY-MM-DD"}), 400

    pokemon = obtener_pokemon_horoscopo(fecha)
    return jsonify({
        "usuario": nombre,
        "pokemon": pokemon
    })
