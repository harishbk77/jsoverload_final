from flask import Flask
import pymysql
app = Flask(__name__)

from flask import Flask, render_template
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        host = "gtbootcamp.mysql.database.azure.com"
        user = "harish@gtbootcamp"
        password = "JsOverload!23"
        db = "jsoverload"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def list_employees(self):
        self.cur.execute("select Respondent, MainBranch, Hobbyist from survey_results_public LIMIT 50")
        result = self.cur.fetchall()
        print(result[0])
        return result
@app.route('/')
def employees():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('employees.html', result=res, content_type='application/json')