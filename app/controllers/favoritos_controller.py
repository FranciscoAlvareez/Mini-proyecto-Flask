from flask import Blueprint, request, jsonify
from services.favoritos import agregar_favorito, listar_favoritos, buscar_favorito, eliminar_favorito

favoritos_bp = Blueprint('favoritos', __name__)

@favoritos_bp.route('/favoritos', methods=['POST'])
def agregar():
    datos = request.get_json()
    usuario = datos.get("usuario")
    nombre_pokemon = datos.get("nombre_pokemon")
    if not usuario or not nombre_pokemon:
        return jsonify({"error": "Faltan datos (usuario o nombre_pokemon)"}), 400
    fav = agregar_favorito(usuario, nombre_pokemon)
    return jsonify(fav)

@favoritos_bp.route('/favoritos', methods=['GET'])
def listar():
    usuario = request.args.get("usuario")
    if not usuario:
        return jsonify({"error": "Falta el usuario"}), 400
    return jsonify(listar_favoritos(usuario))

@favoritos_bp.route('/favoritos/<int:fav_id>', methods=['GET'])
def buscar_fav(fav_id):
    usuario = request.args.get("usuario")
    if not usuario:
        return jsonify({"error": "Falta el usuario"}), 400
    fav = buscar_favorito(usuario, fav_id)
    return jsonify(fav or {})

@favoritos_bp.route('/favoritos', methods=['DELETE'])
def eliminar():
    datos = request.get_json()
    usuario = datos.get("usuario")
    fav_id = datos.get("id")
    if not usuario or not fav_id:
        return jsonify({"error": "Faltan datos (usuario o id)"}), 400
    ok = eliminar_favorito(usuario, fav_id)
    return jsonify({"eliminado": ok})
