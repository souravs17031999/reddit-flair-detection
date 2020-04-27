from flask import Flask, render_template, request, jsonify
from flair_predict import detect_flair
import io
import os
import werkzeug
from werkzeug.utils import secure_filename
import flask

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# defining default route
@app.route('/',methods = ['GET'])
def hello_world():
	'''
	Routing for Home page
	Methods permitted  : GET
	'''
	return render_template('index.html')

@app.route('/reddit', methods = ['GET','POST'])
def flair_detection():
	'''
	Routing Reddit flair detection APP
	Methods permitted  : GET, POST
	'''
	if request.method == 'GET':
	    return render_template('index_reddit.html')

	if request.method == 'POST':
		X = request.form['xname']
		if not X or X == '':
			return render_template('error_reddit.html', message='EMPTY_URL_ERROR : please enter something !')

		prediction_list = detect_flair(X)
		# first is title fetched, then created time, last one is flair detected
		return render_template('result_reddit.html', prediction_list=prediction_list)

@app.route('/automated_testing', methods = ['GET','POST'])
def API():
	'''
	Routing API Testing endpoint
	Methods permitted  : GET, POST
	'''
	if request.method == 'GET':
	    return render_template('error_api.html')

	if request.method == 'POST':
		file = request.files['upload_file']
		if file:
			filename = secure_filename(file.filename)
			Target = os.path.join(APP_ROOT, filename)
			file.save(Target)
			with open(Target) as f:
				links = f.readlines()

			preds = {}
			for link in links:
				if link == '':
					preds[link] = 'None'
				preds[link] = detect_flair(link, api=True)[0]
				
			return jsonify(preds)
		else:
			return jsonify({error : "File not retrived properly !"})

@app.errorhandler(500)
def page_not_found(e):
	'''
	Routing automatic error handling
	'''
    # note that we set the 500 status explicitly
    return render_template('error_reddit.html', message='INVALID_INPUT_URL : PLEASE ENTER VALID REDDIT URL !'), 500
