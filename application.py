from flask import Flask, request, url_for, redirect, render_template, jsonify
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
    def countriesData(self):
        self.cur.execute("SELECT * FROM country_lookup ORDER BY value DESC")
        result = self.cur.fetchall()
        # print(result[0])
        return result
    #     # rows = self.cur.fetchall()
    #     # country_data = []
    #     # for row in rows:
    #     #     tempDict = {}
    #     #     tempDict["country"] = row[0]
    #     #     tempDict["respondentCount"] = int(row[1])
    #     #     # tempDict[row[0]] = int(row[1])
    #     #     country_data.append(tempDict)
    #     # return country_data

		
@app.route('/')
def index():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('index.html', result=res, content_type='application/json')
	
@app.route('/cy')
def cy():
    def db_query():
        db = Database()
        data = db.countriesData()
        return data
    res = db_query()
    return render_template('cy.html', result=res, content_type='application/json')

@app.route('/cyjson')
def cyjsonData():
    def db_query():
        db = Database()
        data = db.countriesData()
        return data
    res = db_query()
    return jsonify(res)
# @app.route('/cyjson')
# def cyjsonData():
#     def countriesData(self):
#         self.cur.execute("SELECT Country_code, Value FROM country_lookup ORDER BY Value DESC")
#         result = self.cur.fetchall()
#         # print(result[0])
#         return result
#         for row in result:
#             country_data = []
#             tempDict = {}
#             tempDict["id"] = row[0]
#             tempDict["value"] = int(row[1])
#             # tempDict[row[0]] = int(row[1])
#             country_data.append(tempDict)
#         return jsonify(country_data)
	
@app.route('/franklin')
def franklin():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('franklin.html', result=res, content_type='application/json')

@app.route('/mauricio')
def mauricio():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('mauricio.html', result=res, content_type='application/json')
	
@app.route('/harish')
def harish():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('harish.html', result=res, content_type='application/json')