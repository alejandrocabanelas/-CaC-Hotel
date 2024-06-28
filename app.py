# Importación de librerías y framework
from flask import Flask, redirect, request, render_template
from flask_mysqldb import MySQL

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reservas'

# Inicialización de MySQL
mysql = MySQL(app)

# Rutas de acceso principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/ingreso.html')
def ingreso():
    return render_template('ingreso.html')

@app.route('/registro.html')
def registro():
    return render_template('registro.html')

@app.route('/reservas.html')
def reservas():
    return render_template('reservas.html')

@app.route('/store', methods=['POST'])
def storage():
    # Recibimos los valores del formulario y los pasamos a variables locales:
    _fecha_llegada = request.form['fecha-llegada']
    _fecha_salida = request.form['fecha-salida']
    _habitacion = request.form['tipo-habitacion']
    _huespedes = request.form['cantidad-huespedes']
    _nombre = request.form['nombre']
    _correo = request.form['email']
    _telefono = request.form['telefono']
    
    datos = (_fecha_llegada, _fecha_salida, _habitacion, _huespedes, _nombre, _correo, _telefono)
    
    # Armamos la sentencia SQL que va a almacenar estos datos en la DB:
    sql = "INSERT INTO tablareservas (ID, FECHA_LLEGADA, FECHA_SALIDA, HABITACION, HUESPEDES, NOMBRE, CORREO, TELEFONO) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);"
    
    conn = mysql.connection  # Nos conectamos a la base de datos 
    cursor = conn.cursor()   # En cursor vamos a realizar las operaciones
    cursor.execute(sql, datos)  # Ejecutamos la sentencia SQL en el cursor
    conn.commit()  # Hacemos el commit
    cursor.close()  # Cerramos el cursor

    # Redirigimos a la ruta principal
    return redirect('/misReservas.html')

@app.route('/servicios.html')
def servicios():
    return render_template('servicios.html')

@app.route('/modificar.html')
def modificar():
    return render_template('modificar.html')

@app.route('/misReservas.html')
def misReservas():
    # Esto anda pero no imprime en el html
    sql = "SELECT * FROM `tablareservas`;"
    conn = mysql.connection  # Nos conectamos a la base de datos 
    cursor = conn.cursor()   # En cursor vamos a realizar las operaciones
    cursor.execute(sql)  # Ejecutamos la sentencia SQL en el cursor
    db_reservas = cursor.fetchall()  # Traer info de base de datos
    for reservas in db_reservas:
        print(reservas)
    cursor.close()  # Cerramos el cursor

    return render_template('misReservas.html', reservas=db_reservas)

if __name__ == '__main__':
    app.run(debug=True)
