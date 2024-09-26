from flask import Flask, render_template, request, jsonify
import random
import time
import os

app = Flask(__name__)

# Definición de palabras y colores
colores = {'rojo': 'red', 'verde': 'green', 'azul': 'blue', 'amarillo': 'yellow'}
palabras = list(colores.keys())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stroop-test', methods=['POST'])
def stroop_test():
    # Obtiene los parámetros del test (número de pruebas)
    n_pruebas = int(request.form.get('n_pruebas', 10))
    resultados = []
    
    for _ in range(n_pruebas):
        palabra = random.choice(palabras)
        color_real = random.choice(list(colores.values()))
        
        # Simulación de resultado (aquí podrías integrar la lógica para registrar la respuesta real)
        start_time = time.time()  # Simula el inicio de la prueba
        respuesta_usuario = random.choice(['r', 'g', 'b', 'y'])  # Simulación de respuesta aleatoria
        end_time = time.time()
        
        tiempo_reaccion = end_time - start_time
        respuesta_correcta = (
            (respuesta_usuario == 'r' and color_real == 'red') or
            (respuesta_usuario == 'g' and color_real == 'green') or
            (respuesta_usuario == 'b' and color_real == 'blue') or
            (respuesta_usuario == 'y' and color_real == 'yellow')
        )
        
        resultados.append({
            'palabra': palabra,
            'color_real': color_real,
            'respuesta': respuesta_usuario,
            'correcto': respuesta_correcta,
            'tiempo_reaccion': tiempo_reaccion
        })
    
    return jsonify(resultados)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Obtiene el puerto de la variable de entorno
    app.run(host='0.0.0.0', port=port)        # Escucha en todas las IPs


  





