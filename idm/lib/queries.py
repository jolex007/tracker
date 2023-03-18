from .database import DBConnection

def add_employee_db(first_name, second_name, login, email, manager_login):
    query = '''
    INSERT INTO employees (first_name, second_name, login, email, manager_login)
    VALUES({}, {}, {}, {}, {})
    '''.format(first_name, second_name, login, email, manager_login)

    try:
        DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    return {"status": "OK"}


def change_employee_db(login, params):
    # TODO:
    return {"status": "OK"}


def delete_employee_db(login, params):
    query = '''
    DELETE FROM employees
    WHERE login='{}'
    '''.format(login)

    try:
        DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    return {"status": "OK"}


def get_employees_db(login_regexp):
    query = '''
    SELECT
        login,
        first_name,
        second_name,
        email,
        manager_login
    FROM employees
    WHERE login ~ '{}'
    '''.format(login_regexp)

    try:
        result = DBConnection.execute_query(query)
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
    
    employees_found = []
    
    for row in result:
        login = row[0]
        first_name = row[1]
        second_name = row[2]
        email = row[3]
        manager_login = row[4]

        employees_found.append({
            'login': login,
            'first_name': first_name,
            'second_name': second_name,
            'email': email,
            'manager_login': manager_login
        })
    
    return {
        "status": "OK",
        "found": employees_found
    }
