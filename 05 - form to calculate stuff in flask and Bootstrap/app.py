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
	#appeler et définir les variables
	result = request.form #chargement des réponses dans une variable type dictionnaire
	nbr_annee = int(result['nbr_annee']) #appel de variable dans result et transformation en entier
	nbr_fois_par_jour = int(result['nbr_fois_par_jour_input']) #idem
	heuresPassees = int(result['heures']) #idem
	minutesPassees = int(result['minutes']) #idem
	secondesPassees = int(result['secondes']) #idem
	verbe = result['verbe']
	
	# #####################################
	#restitution du temps passé : calculs par étape
	#Calcul du nombre total de secondes
	nombreTotalSeconde = 365*nbr_annee*nbr_fois_par_jour*(heuresPassees*3600+minutesPassees*60+secondesPassees)	
	#Calcul du nombre de mois en décimal 
	nombreMoisCalc = nombreTotalSeconde/(3600*24*30)
	#Extraction du nombre entier de mois
	nombreMoisCalcEntier = int(nombreMoisCalc)
	#calcul du nombre de secondes restantes 
	secondesrestantes1 = nombreTotalSeconde - nombreMoisCalcEntier*3600*24*30
	#Calcul du nombre de jours en décimal
	nombreJoursCalc = secondesrestantes1/(3600*24)
	#extraction du nombre entier de jours
	nombreJoursCalcEntier = int(nombreJoursCalc)
	#calcul du nombre restant de secondes : si le temps total est inférieur à un jour, alors secondesrestantesH vaut nombreTotalSeconde
	secondesrestantes2 = secondesrestantes1 - nombreJoursCalcEntier*3600*24
	#calcul du nombre d'heures restantes
	nombreHeuresCalc = secondesrestantes2/3600
	#Extraction du nombre entier d'heures
	nombreHeuresCalcEntier = int(nombreHeuresCalc)
	#calcul du nombre restant de secondes
	secondesrestantes3 = secondesrestantes2 - nombreHeuresCalcEntier*3600
	#calcul du nombre de minutes
	nombreMinutesCalc = secondesrestantes3/60
	#Extraction du nombre entier de minutes
	nombreMinutesCalcEntier = int(nombreMinutesCalc)
	#calcul de ce qu'il reste de secondes
	nombreSecondesrestantesFinal =  secondesrestantes3 - nombreMinutesCalcEntier*60
	
	# #####################################
	#construction de la phrase à publier selon les résultat : message différents selon la durée calculée
	txt1 = "En tout ça représente " 
	txt2 = str(nombreMoisCalcEntier) + " mois "
	txt3 = str(nombreJoursCalcEntier) + " jours "
	txt4 = str(nombreHeuresCalcEntier) + " heures "
	txt5 = str(nombreMinutesCalcEntier) + " minutes et  "
	txt6 = str(nombreSecondesrestantesFinal) + " secondes "
	txt7 = "à  " + verbe + " sans jamais s'arrêter"
	
	# #####################################
	#définition d'un ensemble de réponse qui s'affichent conditionnellement selon la durée totale. tldr, si il y a 0 mois, on affiche pas les mois...
	try:
		if nbr_fois_par_jour*(heuresPassees*3600+minutesPassees*60+secondesPassees) > 86400: #controle sur le fait qu'une journée = 24h
			reponseComplete = "Une journée c'est 24 heures max!!!"
		elif heuresPassees == minutesPassees == secondesPassees == 0 : #controle sur le temps alloué à l'activité : si 0 pas de calcul
			reponseComplete = "Autant de fois que l'on veut un temps nul reste nul!"
		elif nombreMoisCalcEntier != 0 : #si pas de mois, on affiche pas les mois
			reponseComplete = txt1+ txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + " ce qui est assez long il faut avouer!!!"
		elif nombreMoisCalcEntier == 0 & nombreJoursCalcEntier != 0 :
			reponseComplete = txt1 + txt3 + txt4 + txt5 + txt6 + txt7 + " à ne faire que ça sans débander!"
		elif nombreMoisCalcEntier == nombreJoursCalcEntier == nombreHeuresCalcEntier == 0 :
			reponseComplete = txt1 + txt5 + txt6 + txt7 + "."
		elif nombreMoisCalcEntier == nombreJoursCalcEntier == 0 :
			reponseComplete = txt1 + txt4 + txt5 + txt6 + txt7 + "."
		else  :
			reponseComplete = txt1 + txt5 + txt6 + txt7 + " ce qui au final n'est pas si long que ça."
	except:
			return "Mais qu'est-ce que vous faites?"
	# #####################################
	# return render_template("resultat.html", reponseComplete=reponseComplete, result=result) = ligne pour controler le résultat
	return render_template("resultat.html", reponseComplete=reponseComplete)
	
if __name__ == "__main__":
    app.run(debug=True)
