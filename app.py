# Importe de librerias y framework
from flask import Flask, request, render_template
from flask_mysqldb import MySQL
mysql = MySQL()

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_BD'] = 'reservas'

mysql.init_app(app)

# Configuración de la base de datos
db = MySQL(app)

# Rutas
@app.route('/')
def misReservas():
    return render_template('./src/pages/misReservas.html')

if __name__ == '__main__':
    app.run(debug=True)