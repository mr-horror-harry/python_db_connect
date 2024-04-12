import psycopg2

def connect_db():
    try:
        print("Connecting to DB...")
        connection = psycopg2.connect(
            dbname="student_data",
            user="new_user",
            password="password",
            host="192.168.17.8",
            port="5432"
        )
        return connection
    except Exception as err:
        print(f"DB not connected!\n{err}")