from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Inincia o Flask
app = Flask(__name__)

# Acessa O Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
db = SQLAlchemy(app)

# Faz as Migrações
migrate = Migrate(app, db)

# Base de Dados
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    tel = db.Column(db.String(20))
    email = db.Column(db.String(30))


# Rotas e Views
@app.route('/', methods=['POST', 'GET'])
def index():
    nome = request.form.get('nome')
    tel = request.form.get('telefone')
    email = request.form.get('email')

    if request.method != 'POST':
        return render_template('index.html')

    save_db = Contact(username=nome, tel=tel, email=email)
    db.session.add(save_db)
    db.session.commit()

    return render_template('index.html')


@app.route('/contacts')
def contacts():
    contacts_db = Contact.query.all()
    return render_template('contacts.html', contact=contacts_db)