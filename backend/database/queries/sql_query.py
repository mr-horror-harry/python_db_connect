CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS student_data(
    regno serial,
    name varchar(20),
    dept varchar(10),
    gender char(1),
    mobile char(10)
)
"""
INSERT_DATA = """INSERT INTO student_data(name, dept, gender, mobile) VALUES(%s, %s, %s, %s)"""