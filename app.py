from flask import Flask
from routes.task import tasks_blueprint

app = Flask(__name__)
app.register_blueprint(tasks_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=False)
