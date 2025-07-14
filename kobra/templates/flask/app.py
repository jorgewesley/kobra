from flask import Flask, render_template
from config import Config
{{ db_import }}
{{ auth_import }}

app = Flask(__name__)
app.config.from_object(Config)

{{ db_init }}

@app.route('/')
def home():
    return render_template('index.html', project_name="{{ project_name }}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)