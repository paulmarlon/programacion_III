import os
from flask import Flask, request, jsonify, render_template
from database import DatabaseConnection
from models import ProductoRepository

app = Flask(__name__)

# Instancia global de la conexión
db_conn = DatabaseConnection()

@app.route('/')
def index():
    """Sirve la página web con el formulario Vue.js."""
    return render_template('index.html')

@app.route('/api/productos', methods=['GET'])
@app.route('/api/productos', methods=['GET'])
def buscar_productos():
    """
    Endpoint de búsqueda de productos vía query string (GET).
    """
    try:
        # 1. Obtener parámetros de filtrado
        nombre = request.args.get('nombre')
        marca = request.args.get('marca')
        precio_min = request.args.get('precio_min')
        precio_max = request.args.get('precio_max')
        unidades_min = request.args.get('unidades_min')

        # 2. Obtener parámetros de ORDENAMIENTO (Nuevos)
        # Usamos los valores por defecto que pide el requerimiento
        sort_by = request.args.get('sort_by', 'nombre')
        order = request.args.get('order', 'asc')

        # Validación de tipos (mantenemos tu lógica original)
        if precio_min:
            try: precio_min = float(precio_min)
            except ValueError: return jsonify({'error': 'precio_min inválido'}), 400

        if precio_max:
            try: precio_max = float(precio_max)
            except ValueError: return jsonify({'error': 'precio_max inválido'}), 400

        if unidades_min:
            try:
                unidades_min = int(unidades_min)
                if unidades_min < 0: raise ValueError
            except ValueError: return jsonify({'error': 'unidades_min inválido'}), 400

        # 3. Conexión y ejecución
        db_conn.connect()
        repo = ProductoRepository(db_conn)

        # Pasamos sort_by y order al repositorio
        productos = repo.buscar(
            nombre=nombre if nombre else None,
            marca=marca if marca else None,
            precio_min=precio_min,
            precio_max=precio_max,
            unidades_min=unidades_min,
            sort_by=sort_by,  # <--- Requerimiento cumplido
            order=order       # <--- Requerimiento cumplido
        )

        db_conn.close()

        # 4. Respuesta
        resultados = [p.to_dict() for p in productos]
        return jsonify({
            'cantidad': len(resultados),
            'productos': resultados
        })

    except Exception as e:
        if db_conn:
            db_conn.close()
        return jsonify({'error': f'Error interno: {str(e)}'}), 500
@app.route('/api/productos', methods=['POST'])
def guardar_producto():
    try:
        datos = request.get_json()
        
        # Validación básica
        if not datos.get('nombre') or not datos.get('marca'):
            return jsonify({'error': 'Nombre y marca son obligatorios'}), 400

        db_conn.connect()
        # Necesitaremos un método 'guardar' en tu ProductoRepository
        repo = ProductoRepository(db_conn)
        nuevo_id = repo.guardar(datos) 
        db_conn.close()

        return jsonify({'mensaje': 'Producto guardado', 'id': nuevo_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True, port=5000)