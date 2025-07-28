from flask import Flask, jsonify
import logging
from controllers.pokemon_controller import pokemon_bp
from controllers.horoscopo_controller import horoscopo_bp
from controllers.favoritos_controller import favoritos_bp

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(pokemon_bp)
app.register_blueprint(horoscopo_bp)
app.register_blueprint(favoritos_bp)

# Configurar Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Error handler global
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Error: {str(e)}")
    code = getattr(e, "code", 500)
    return jsonify({"error": str(e)}), code

@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido al Horóscopo Pokémon"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
