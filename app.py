from flask import Flask, render_template
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        return conn
    except Error as e:
        print(e)

    return conn

database = r"C:\\myproject\calc.db"
conn = create_connection(database)
class Calculator:

    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE Calculator
        :return:
        """

        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_table_calc(conn_1 ):

        command1 = "CREATE TABLE IF NOT EXISTS  Calculator (ID_NUMBER INTEGER,ID INTEGER , number INTEGER, operation TEXT NOT NULL);"
        cur = conn_1.cursor()
        cur.execute(command1)
        conn_1.commit()


    def insert_task(conn, task):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """
        sql_insert_calc = ''' INSERT INTO Calculator(id_number,id,number, operation) VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql_insert_calc, task)
        conn.commit()
        print(cur.lastrowid)
        return cur.lastrowid

    def select_task_by_priority(conn):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM Calculator ORDER BY id_number DESC limit 1 ")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def select_all_tasks(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM Calculator")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def delete_task(conn, id_number) :
        """
        Delete a task by id_number
        :param conn:  Connection to the SQLite database
        :param id_number: id_number of the task
        :return:
        """
        cur = conn.cursor()
        cur.execute("DELETE FROM Calculator WHERE id_number = ?; ",(id_number,))
        #cur.execute(sql_delete_id, (task,))
        conn.commit()


    def delete_all_tasks(conn):
        """
        Delete all rows in the tasks table
        :param conn: Connection to the SQLite database
        :return:
        """
        sql_delete_all = 'DELETE FROM Calculator'
        cur = conn.cursor()
        cur.execute(sql_delete_all)
        conn.commit()

Calculator.create_table_calc(conn)
anything = Calculator()

app = Flask(__name__)

@app.route('/') #homepage
def hello_world():
     return 'Hello, World!'

values = []
Calculator.delete_all_tasks(conn)
@app.route('/calc/<int:id>/push/<number>') #choose the numbers by pushing them
def adding_values(number, id):
    database = r"C:\\myproject\calc.db"
    conn = create_connection(database)
    id_number = len(values)+1
    l = int(number)
    task_1=(id_number, id, number,'push')
    values.append(l)
    Calculator.insert_task(conn,task_1)
    Calculator.select_all_tasks(conn)
    return str(number)

@app.route('/calc/<int:id>/<op>') 
def home(op, id):
    database = r"C:\\myproject\calc.db"
    conn = create_connection(database)

    if op == "peek": #call this operator to return top of the stack
        last_element = len(values)
        if last_element == 0:
            return "<h1> list is empty </h1>"
        else:
            Calculator.select_task_by_priority(conn)
            return str(values[last_element-1])

    elif op == "pop": #returns and deletes top of the stack
        last_element = len(values)
        if last_element == 0:
            return "<h1> list is empty </h1>"
        else:
            id_number=last_element
            Calculator.delete_task(conn, id_number)
            Calculator.select_all_tasks(conn)
            return "<h1> last digit removed </h1>"

    elif op == "add": #adding
        last_element = len(values)
        if last_element <= 1:
            return "<h1> list is empty or have 1 element </h1>"
        else:
            id_number=last_element
            result = values[last_element-1] + values[last_element-2]
            values[last_element-1] = result
            number=result
            task_1 = (id_number, id, number, 'add')
            Calculator.delete_task(conn, id_number)
            Calculator.insert_task(conn, task_1)
            Calculator.select_all_tasks(conn)
            return str(result)

    elif op == "sub":  #substracting
        last_element = len(values)
        if last_element <= 1:
            return "<h1> list is empty or have 1 element </h1>"
        else:
            id_number = last_element
            result = values[last_element-1] - values[last_element-2]
            values[last_element-1] = result
            number=result
            task_1 = (id_number, id, number, 'sub')
            Calculator.delete_task(conn, id_number)
            Calculator.insert_task(conn, task_1)
            Calculator.select_all_tasks(conn)
            return str(result)

    elif op == "mult": #multiplying
        last_element = len(values)
        if last_element <= 1:
            return "<h1> list is empty or have 1 element </h1>"
        else:
            id_number = last_element
            result = values[last_element-1] * values[last_element-2]
            values[last_element-1] = result
            number=result
            task_1 = (id_number, id, number, 'mult')
            Calculator.delete_task(conn, id_number)
            Calculator.insert_task(conn, task_1)
            return str(result)

    elif op == "divi": #deviding
        last_element = len(values)
        if last_element <= 1:
            return "<h1> list is empty or have 1 element </h1>"
        else:
            id_number = last_element
            operation = 'divi'
            if values[last_element-2] == 0:    #error message
                return "<h1> stack underflow, devided by 0 </h1>"
            else:
                result = values[last_element-1] / values[last_element-2]
                values[last_element-1] = result
                number=result
                task_1 = (id_number, id, number, 'divi')
                Calculator.delete_task(conn, id_number)
                Calculator.insert_task(conn, task_1)
                Calculator.update_task(conn, id_number, result, operation)
                return str(result)

if __name__ == '__main__': #debugger on
    app.run(debug = True)
