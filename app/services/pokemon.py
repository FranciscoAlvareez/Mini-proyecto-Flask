import requests

def buscar_pokemon(nombre=None, tipo=None):
    resultados = []

    # Si se busca por nombre
    if nombre:
        resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}")
        if resp.status_code == 200:
            data = resp.json()
            resultados.append(_formatear_datos(data))

    # Si se busca por tipo
    elif tipo:
        resp = requests.get(f"https://pokeapi.co/api/v2/type/{tipo.lower()}")
        if resp.status_code == 200:
            data = resp.json()
            # Traemos solo los primeros 10
            for pokemon in data["pokemon"][:10]:
                poke_name = pokemon["pokemon"]["name"]
                p_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name}").json()
                resultados.append(_formatear_datos(p_data))

    return resultados

def _formatear_datos(data):
    return {
        "nombre": data["name"],
        "imagen": data["sprites"]["front_default"],
        "tipo": [t["type"]["name"] for t in data["types"]],
        "altura": data["height"],
        "peso": data["weight"],
        "habilidades": [h["ability"]["name"] for h in data["abilities"]]
    }
