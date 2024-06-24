# Importe de librerias y framework
from flask import Flask, request, jsonify, render_template
from flaskext.mysql import MySQL
mysql = MySQL()

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['MYSQL_DATABASE_URI'] = 'sqlite:///db.sqlite'  # Conexión a SQLite
app.config['MYSQL_TRACK_MODIFICATIONS'] = False

# Configuración de la base de datos
db = MySQL(app)

# Modelo de Usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

# Obtener todos los usuarios (GET)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'users': users_list})

# Crear un nuevo usuario (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

# Actualizar un usuario existente (PUT)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# Borrar un usuario (DELETE)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    db.create_all()  # Crear tablas en la base de datos si no existen
    app.run(debug=True)
