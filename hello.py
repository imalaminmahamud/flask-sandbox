from flask import Flask, url_for, request
from markupsafe import escape


app = Flask('__name__')


@app.route('/')
def index():
	return f'Index Page'


@app.route('/hello')
def hello():
	return 'Hello, World' 


@app.route('/user/<username>')
def profile(username):
	return f'User - {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return f'Showing Post - {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return f'Subpath {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'do_the_login()'
	else:
		return 'show_the_login_form()'


with app.test_request_context():
	print(url_for('index'))
	print(url_for('login'))
	print(url_for('login', next='index/'))
	print(url_for('profile', username='John Doe', id=123))



