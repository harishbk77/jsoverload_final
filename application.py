from flask import Flask, request, url_for, redirect, render_template
import pymysql
from bokeh.plotting import figure, output_file, show

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
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('cy.html', result=res, content_type='application/json')
	
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

		# prepare some data
        x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
        y0 = [i**2 for i in x]
        y1 = [10**i for i in x]
        y2 = [10**(i**2) for i in x]

		# create a new plot
        p = figure(
        tools="pan,box_zoom,reset,save",
        y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
        x_axis_label='sections', y_axis_label='particles'
        )

        # output to static HTML file
        output_file("log_lines.html")

        # add some renderers
        p.line(x, x, legend="y=x")
        p.circle(x, x, legend="y=x", fill_color="white", size=8)
        p.line(x, y0, legend="y=x^2", line_width=3)
        p.line(x, y1, legend="y=10^x", line_color="red")
        p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
        p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

        # show the results
        show(p)
        return emps
	
    res = db_query()
    return render_template('harish.html', result=res, content_type='application/json')