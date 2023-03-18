from flask import Flask, jsonify, request
from lib.queries import *
from lib.database import DBConnector

app = Flask(__name__)


@app.route("/employee", methods=['POST'])
def add_employee():
    content = request.json
    status = add_employee_db(content['first_name'], content['second_name'], content['login'], content['email'], content['manager_login'])
    return jsonify(status)


# TODO: Add change employee request
# @app.route("/employee/<login>", methods=['PUT'])
# def change_employee(login):
#     content = request.json
#     status = change_employee_db(login, content)
#     return jsonify({'status': 'OK'})


@app.route("/employee/<login>", methods=['DELETE'])
def remove_employee(login):
    status = delete_employee_db(login)
    return jsonify(status)


@app.route("/employee", methods=['GET'])
def get_employees_info():
    content = request.json
    result = get_employees_db(content["login"])
    return jsonify(result)


@app.route("/health", methods=['GET'])
def health():
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    DBConnector.set_settings()
    app.run(host='0.0.0.0', port=8000)
