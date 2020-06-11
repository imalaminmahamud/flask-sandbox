from flask import Flask
app = Flask('123')

@app.route('/')
def index():
	return f'Index Page'

@app.route('/hello')
def hello():
	return 'hello, world' 
