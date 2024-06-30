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

# Rutas de acceso secundarios
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/ingreso')
def ingreso():
    return render_template('ingreso.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

# Guardar datos en la base de datos
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
    
    return redirect('/misReservas')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/modificar')
def modificar():
    return render_template('modificar.html')

# Traemos toda la info a la pagina
@app.route('/misReservas')
def misReservas():
    sql = "SELECT * FROM `tablareservas`;"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    db_reservas = cursor.fetchall()  # Traer info de base de datos
    for reserva in db_reservas:
        print(reserva)
    cursor.close()

    return render_template('misReservas.html', db_reservas=db_reservas)

# Funcion para eliminar una linea de la base de datos
@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `reservas`.`tablareservas` WHERE ID=%s", (id,))
    conn.commit()
    cursor.close()
    return redirect('/misReservas')

# Funcion para guardar la modificacion de los datos
@app.route('/update', methods=['POST'])
def update():
    # Recibimos los valores del formulario y los pasamos a variables locales:
    _fecha_llegada = request.form['fecha-llegada']
    _fecha_salida = request.form['fecha-salida']
    _habitacion = request.form['tipo-habitacion']
    _huespedes = request.form['cantidad-huespedes']
    _nombre = request.form['nombre']
    _correo = request.form['email']
    _telefono = request.form['telefono']
    _id = request.form['id_codigo']

    conn = mysql.connection
    cursor = conn.cursor()

    # Actualizacion del registro de la base de datos
    sql = "UPDATE reservas.tablareservas SET FECHA_LLEGADA=%s, FECHA_SALIDA=%s, HABITACION=%s, HUESPEDES=%s, NOMBRE=%s, CORREO=%s, TELEFONO=%s WHERE ID=%s"
    datos = (_fecha_llegada, _fecha_salida, _habitacion, _huespedes, _nombre, _correo, _telefono, _id)
    cursor.execute(sql, datos)

    conn.commit()
    cursor.close()

    return redirect('/misReservas')

# Funcion para modificar los datos
@app.route('/reprogramar/<int:id>')
def reprogramar(id):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `reservas`.`tablareservas` WHERE id=%s", (id,))
    reservas = cursor.fetchall()
    cursor.close()
    print(reservas)
    return render_template('reprogramar.html', reservas=reservas)

if __name__ == '__main__':
    app.run(debug=True)
