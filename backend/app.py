from flask import Flask, request, jsonify, render_template, send_from_directory
from databases.DatabaseWrapper import DatabaseWrapper
from flask_cors import CORS
import traceback
import os

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:3000"}})  # Habilita CORS para todas las rutas

db_wrapper = DatabaseWrapper()

# Ruta para servir archivos estáticos generados por React
@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'frontend', 'build', 'static'), filename)

# Manejar solicitudes OPTIONS para la raíz
@app.route('/', methods=['OPTIONS', 'POST'])
def handle_options_and_post_root():
    if request.method == 'OPTIONS':
        # Agregar las cabeceras CORS requeridas para la raíz
        response_headers = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',  # Métodos permitidos
            'Access-Control-Allow-Headers': 'Content-Type',  # Cabeceras permitidas
        }
        return ('', 204, response_headers)
    elif request.method == 'POST':
        # Procesar la solicitud POST
        return landing_page()


# Ruta para manejar la solicitud POST
# Ruta para manejar la solicitud POST
@app.route('/', methods=['POST'])
def landing_page():
    # Obtenemos los datos del formulario
    data = request.get_json()
    correo = data.get('correo')
    telefono = data.get('telefono')

    # Validación para asegurarse de que el correo no sea nulo
    if correo is None or correo.strip() == "":
        return jsonify({"error": "El campo 'correo' es requerido"}), 400

    try:
        # Llama al procedimiento almacenado utilizando el DatabaseWrapper
        stored_procedure_name = 'InsertSubscriber'
        parameters = (correo, telefono)
        db_wrapper.call(stored_procedure_name, parameters)

        # Responde con éxito
        return jsonify({"message": "Datos guardados exitosamente en la base de datos"})

    except Exception as err:
        error_message = traceback.format_exc()
        print(error_message)
        return jsonify({"error": "Error al guardar los datos en la base de datos"}), 500


        
if __name__ == '__main__':
    app.run(debug=True)
