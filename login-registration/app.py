from flask import Flask, session


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return app


def create_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def login():
        if not session.get('logged_in'):



def run_the_application(app):
    app.run(
        debug=True,
        use_reloader=True,
        host="0.0.0.0"
    )


if __name__ == "__main__":
    app = create_app()
    run_the_application(app)

