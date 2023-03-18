from flask import Flask, jsonify, request
from lib.queries import *
from lib.database import DBConnector

app = Flask(__name__)


# Список тикетов
@app.route("/issues", methods=['GET'])
def get_issues():
    content = request.json
    status = get_issues_db(content["title_regexp"])
    return jsonify(status)

# Отдельный тикет
@app.route("/issues/<issue_id>", methods=['GET'])
def get_issue(issue_id):
    status = get_issue_db(issue_id)
    return jsonify(status)

# Создать тикет
@app.route("/issues", methods=['POST'])
def add_issue():
    content = request.json
    status = add_issue_db(content['title'], content['description'], content['sprint_id'], content['owner_login'], content['employee_login'], content['change_time'])
    return jsonify(status)

# Изменить тикет
@app.route("/issues/<issue_id>", methods=['PATCH'])
def change_issue(issue_id):
    content = request.json
    # TODO:
    return jsonify(status)

# Удалить тикет
@app.route("/issues/<issue_id>", methods=['DELETE'])
def remove_issue(issue_id):
    status = remove_issue_db(issue_id)
    return jsonify(status)


# Посмотреть спринты
@app.route("/sprints", methods=['GET'])
def get_sprints():
    content = request.json
    status = get_sprints_db(content['name_filter'])
    return jsonify(status)

# Создать спринт
@app.route("/sprints", methods=['POST'])
def add_sprint():
    content = request.json
    status = add_sprint_db(content['name'], content['start_time'], content['finish_time'])
    return jsonify(status)

# Удалить спринт
@app.route("/sprints/<sprint_id>", methods=["DELETE"])
def remove_sprint(sprint_id):
    content = request.json
    status = remove_sprint_db(sprint_id)
    return jsonify(status)


@app.route("/health", methods=['GET'])
def health():
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    DBConnector.set_settings()
    app.run(host='0.0.0.0', port=8000)
