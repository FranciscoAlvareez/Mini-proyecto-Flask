import requests
from datetime import datetime

POKEMONS_POR_SIGNO = {
    "aries": "charmander",
    "tauro": "bulbasaur",
    "geminis": "squirtle",
    "cancer": "pikachu",
    "leo": "eevee",
    "virgo": "jigglypuff",
    "libra": "meowth",
    "escorpio": "psyduck",
    "sagitario": "snorlax",
    "capricornio": "magikarp",
    "acuario": "mew",
    "piscis": "togepi"
}

def obtener_pokemon_horoscopo(fecha):
    signo = calcular_signo(fecha)
    pokemon_nombre = POKEMONS_POR_SIGNO.get(signo, "pikachu")
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_nombre}").json()
    return {
        "signo": signo,
        "nombre": data["name"],
        "imagen": data["sprites"]["front_default"],
        "tipo": [t["type"]["name"] for t in data["types"]]
    }

def calcular_signo(fecha):
    f = datetime.strptime(fecha, "%Y-%m-%d")
    mes, dia = f.month, f.day
    # Tabla de signos
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19): return "aries"
    if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20): return "tauro"
    if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20): return "geminis"
    if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22): return "cancer"
    if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22): return "leo"
    if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22): return "virgo"
    if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22): return "libra"
    if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21): return "escorpio"
    if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21): return "sagitario"
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19): return "capricornio"
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18): return "acuario"
    return "piscis"
