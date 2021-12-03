#! /usr/bin/env python
from flask import *
from recherche import *
app = Flask(__name__,template_folder='template')

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')
@app.route('/')
@app.route('/indexEN/')
def indexEN():
	return render_template('indexEN.html')
@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  print(r(n))
  return render_template("resultat.html", nom=n)
if __name__ == "__main__":
    app.run()
