from flask import Flask, request, jsonify

app = Flask(__name__)

# Переменная для хранения состояния вибрации
vibration_state = {"vibrate": False}

@app.route('/send_vibration', methods=['POST'])
def send_vibration():
    global vibration_state
    vibration_state["vibrate"] = True
    return '', 204

@app.route('/receive_vibration', methods=['GET'])
def check_vibration():
    global vibration_state
    response = jsonify(vibration_state)
    # Сбрасываем состояние вибрации после получения
    vibration_state["vibrate"] = False
    return response

if __name__ == '__main__':
    app.run(host='35.160.120.126', port=5000)
