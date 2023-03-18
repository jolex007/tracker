from .database import DBConnection

def add_sprint_db(name, start_time, finish_time):
    query = '''
    INSERT INTO sprints (name, start_time, finish_time)
    VALUES({}, {}, {})
    '''.format(name, start_time, finish_time)

    try:
        DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    return {"status": "OK"}

def remove_sprint_db(sprint_id):
    query = '''
    DELETE FROM sprints
    WHERE sprint_id='{}'
    '''.format(sprint_id)

    try:
        DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    return {"status": "OK"}

def get_sprints_db(name_regexp):
    query = '''
    SELECT
        sprint_id,
        name,
        start_datetime,
        finish_datetime
    FROM sprints
    WHERE name ~ '{}'
    '''.format(name_regexp)

    try:
        result = DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    found = []

    for row in result:
        sprint_id = row[0]
        name = row[1]
        start_datetime = row[2]
        finish_datetime = row[3]
    
        found.append({
            "sprint_id": sprint_id,
            "name": name,
            "start_datetime": start_datetime,
            "finish_datetime": finish_datetime
        })

    return {
        "status": "OK",
        "found": found
    }


def get_issues_db(title_regexp):
    query = '''
    SELECT
        issue_id,
        title
    FROM issues
    WHERE title ~ '{}'
    '''.format(title_regexp)

    try:
        result = DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    found = []
    
    for row in result:
        issue_id = row[0]
        title = row[1]

        found.append({
            'issue_id': issue_id,
            'title': title
        })
    
    return {
        "status": "OK",
        "found": found
    }

def get_issue_db(issue_id):
    query = '''
    SELECT
        issue_id,
        title,
        description,
        sprint_id,
        owner_login,
        employee_login,
        change_time,
        status
    FROM issues
    WHERE issue_id={}
    '''.format(issue_id)

    try:
        result = DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    if len(result) == 0:
        return {
            "status": "ERROR",
            "message": "Issue not found"
        }

    result = result[0]
    found = {
        "issue_id": result[0],
        "title": result[1],
        "description": result[2],
        "sprint_id": result[3],
        "owner_login": result[4],
        "employee_login": result[5],
        "change_time": result[6],
        "status": result[7]
    }

    return {
        "status": "OK",
        "found": found
    }

def add_issue_db(title, description, sprint_id, owner_login, employee_login, change_time):
    query = '''
    INSERT INTO issues (title, description, sprint_id, owner_login, employee_login, change_time, status)
    VALUES({}, {}, {}, {}, {}, {}, {})
    '''.format(title, description, sprint_id, owner_login, employee_login, change_time, "NEW")

    try:
        DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }

    return {"status": "OK"} # TODO: add issue_id into response

def remove_issue_db(issue_id):
    query = '''
    DELETE FROM issues
    WHERE issue_id='{}'
    '''.format(issue_id)

    try:
        DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    return {"status": "OK"}