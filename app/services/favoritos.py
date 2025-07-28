import json
import os

ARCHIVO_FAVORITOS = "favoritos.json"

def _cargar_favoritos():
    if not os.path.exists(ARCHIVO_FAVORITOS):
        return {}
    with open(ARCHIVO_FAVORITOS, "r") as f:
        return json.load(f)

def _guardar_favoritos(data):
    with open(ARCHIVO_FAVORITOS, "w") as f:
        json.dump(data, f, indent=4)

def agregar_favorito(usuario, nombre_pokemon):
    data = _cargar_favoritos()
    if usuario not in data:
        data[usuario] = []

    nuevo_id = len(data[usuario]) + 1
    data[usuario].append({"id": nuevo_id, "nombre": nombre_pokemon})
    _guardar_favoritos(data)
    return {"id": nuevo_id, "nombre": nombre_pokemon}

def listar_favoritos(usuario):
    data = _cargar_favoritos()
    return data.get(usuario, [])

def buscar_favorito(usuario, fav_id):
    data = _cargar_favoritos()
    if usuario in data:
        for fav in data[usuario]:
            if fav["id"] == fav_id:
                return fav
    return None

def eliminar_favorito(usuario, fav_id):
    data = _cargar_favoritos()
    if usuario in data:
        nuevos = [f for f in data[usuario] if f["id"] != fav_id]
        if len(nuevos) != len(data[usuario]):
            data[usuario] = nuevos
            _guardar_favoritos(data)
            return True
    return False
