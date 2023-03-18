from flask import Flask, jsonify, request
from lib.queries import *
from lib.database import DBConnector

app = Flask(__name__)


# Список отчетов
@app.route("/records", methods=['GET'])
def get_records():
    content = request.json
    
    return jsonify(status)

# Получить конкретный отчет
@app.route("/records/<record_id>", methods=['POST'])
def get_record(record_id):
    content = request.json

    return jsonify(status)

# Создание отчета
@app.route("/records", methods=['POST'])
def add_record(record_id):
    content = request.json

    return jsonify(status)

# Удаление отчета
@app.route("/records/<record_id>", methods=['DELETE'])
def get_record(record_id):
    content = request.json

    return jsonify(status)

if __name__ == '__main__':
    DBConnector.set_settings()
    app.run(host='0.0.0.0', port=8000)
