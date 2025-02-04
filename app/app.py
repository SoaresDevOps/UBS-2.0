#importando as Bibliotecas
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import os
#Configurações basicas
app = Flask(__name__, static_folder='static', template_folder='static')
socketio = SocketIO(app, cors_allowed_origins="*") #permitindo a comunicacao de varios dispositivos


#pagina principal
@app.route('/')
def index():
    return render_template('index.html')

#pagina do resultado
@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

#comunicação por websocket
@socketio.on('send_sala')
def handle_send_sala(data):
    sala = data.get('sala', '')
    emit('receive_sala', {'sala': sala}, broadcast=True)

@socketio.on('send_senha')
def handle_send_senha(data):
    senha = data.get('senha', '')
    emit('receive_senha', {'senha': senha}, broadcast=True)

@socketio.on('send_doutor')
def handle_send_doutor(data):
    doutor = data.get('doutor', '')
    emit('receive_doutor', {'doutor': doutor}, broadcast=True)

@socketio.on('tocar_som')
def handle_tocar_som():
    emit('reproduzir_som', broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # Em produção, desative o debug
    socketio.run(app, debug=False, host='0.0.0.0', port=port)