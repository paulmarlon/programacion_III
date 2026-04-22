from flask import Flask, request, jsonify
from database import init_db, insertar_asistente

app = Flask(__name__)
init_db()
@app.route('/asistentes', methods=['GET'])
def listar_asistentes():
    """Retorna todos los registros de la base de datos."""
    try:
        from database import obtener_todos
        registros = obtener_todos()
        # Convertimos la lista de tuplas a una lista de diccionarios para el JSON
        lista = []
        for r in registros:
            lista.append({"id": r[0], "nombre": r[1], "email": r[2]})
        return jsonify(lista), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/asistencia', methods=['POST'])
def registrar():
    data = request.get_json()
    if not data or 'nombre' not in data or 'email' not in data:
        return jsonify({"error": "Faltan nombre o email"}), 400

    nombre = data['nombre'].strip()
    email = data['email'].strip()

    try:
        asistente_id = insertar_asistente(nombre, email)
        return jsonify({"mensaje": "Asistente registrado", "id": asistente_id}), 201
    except ValueError as e:
        # Aquí capturamos el "Email ya registrado"
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/')
def index():
    return "API de registro de asistencia funcionando. Usa POST /asistencia"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)