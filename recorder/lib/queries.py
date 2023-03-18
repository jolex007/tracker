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
