from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import bcrypt  # Para el hashing de contraseñas

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesaria para manejar sesiones

# Configuración de la conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',  # Usuario de MySQL
        password='1234',  # Contraseña de MySQL
        database='clientes'  # Nombre de la base de datos
    )

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre_completo = request.form['nombre_completo']  # Campo para nombre completo
    telefono = request.form['telefono']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    
    if not nombre_completo or not telefono or not contrasena:  # Validar campos obligatorios
        flash("Nombre Completo, Teléfono y Contraseña son obligatorios", "error")
        return redirect(url_for('index'))

    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insertar nuevo usuario
    cursor.execute('INSERT INTO usuarios (nombre_completo, telefono, correo, contrasena) VALUES (%s, %s, %s, %s)', 
                   (nombre_completo, telefono, correo, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash("Usuario registrado exitosamente", "success")
    return redirect(url_for('index'))

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    nombre_completo = request.form['nombre_completo']  # Campo para nombre completo
    contrasena = request.form['contrasena']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar credenciales
    cursor.execute('SELECT * FROM usuarios WHERE nombre_completo = %s', (nombre_completo,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if usuario and bcrypt.checkpw(contrasena.encode('utf-8'), usuario[4].encode('utf-8')):  # Verificar la contraseña
        session['nombre_completo'] = nombre_completo
        return redirect(url_for('bienvenida'))
    else:
        flash("Credenciales incorrectas", "error")
        return redirect(url_for('index'))

@app.route('/bienvenida')
def bienvenida():
    if 'nombre_completo' in session:
        return f"Bienvenido, {session['nombre_completo']}!"
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('nombre_completo', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    