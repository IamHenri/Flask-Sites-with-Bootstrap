# inspiration : https://pixees.fr/informatiquelycee/n_site/nsi_prem_flask.html
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apropos/")
def apropos():
    return render_template("apropos.html")

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)
	
	
if __name__ == "__main__":
    app.run(debug=True)
