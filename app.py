from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import os
import requests
from functools import wraps
from dotenv import load_dotenv 

# Carga las variables del archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback-key")  # 👈 Usa la variable desde .env

# Configuración Supabase desde variables de entorno
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SUPABASE_HEADERS = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json'
}

# Decorador para verificar rol

def requiere_rol(rol_requerido):
    def decorador(f):
        @wraps(f)
        def funcion_decorada(*args, **kwargs):
            if 'rol' not in session or session['rol'] != rol_requerido:
                flash('⚠️ No tienes permisos para acceder a esta página.')
                return redirect(url_for('inicio'))
            return f(*args, **kwargs)
        return funcion_decorada
    return decorador

@app.route('/api/user_admin_plataform')
def obtener_usuarios():
    response = requests.get(
        f'{SUPABASE_URL}/rest/v1/user_admin_plataform',
        headers=SUPABASE_HEADERS
    )
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'No se pudo obtener usuarios'}), response.status_code

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Consulta a Supabase para validar usuario y contraseña
        params = {
            'username': f'eq.{username}',
            'password': f'eq.{password}'
        }
        response = requests.get(
            f'{SUPABASE_URL}/rest/v1/user_admin_plataform',
            headers=SUPABASE_HEADERS,
            params=params
        )

        if response.status_code == 200 and response.json():
            user_data = response.json()[0]
            session['user'] = user_data['username']
            session['rol'] = user_data['rol']
            return redirect(url_for('inicio'))
        else:
            return render_template('login.html', error='Credenciales incorrectas')

    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def inicio():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('inicio.html')

@app.route('/stock')
def stock():
    filtro = request.args.get('filtro', '')

    if filtro:
        filtro_like = f"%{filtro}%"
        query_params = {
            "or": f"(referencia.ilike.{filtro_like},marca.ilike.{filtro_like},nombre_bodega.ilike.{filtro_like})",
            "order": "nombre_bodega.asc,referencia.asc"
        }
    else:
        query_params = {
            "order": "nombre_bodega.asc,referencia.asc"
        }

    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/vista_stock",
        headers=SUPABASE_HEADERS,
        params=query_params
    )

    if response.status_code == 200:
        datos_stock = response.json()
        return render_template('stock.html', datos_stock=datos_stock)
    else:
        flash("❌ Error al cargar datos de stock.")
        return render_template('stock.html', datos_stock=[])
    
from flask import Response
import csv
from io import StringIO

@app.route('/descargar_csv')
def descargar_csv():
    filtro = request.args.get('filtro', '')

    if filtro:
        filtro_like = f"%{filtro}%"
        query_params = {
            "or": f"(referencia.ilike.{filtro_like},marca.ilike.{filtro_like},nombre_bodega.ilike.{filtro_like})",
            "order": "nombre_bodega.asc,referencia.asc"
        }
    else:
        query_params = {
            "order": "nombre_bodega.asc,referencia.asc"
        }

    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/vista_stock",
        headers=SUPABASE_HEADERS,
        params=query_params
    )

    if response.status_code != 200:
        return "Error al obtener los datos", 400

    datos = response.json()

    # Crear archivo CSV en memoria
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Referencia", "Descripción", "Marca", "Bodega", "Cantidad", "Precio", "Unidad"])

    for item in datos:
        writer.writerow([
            item.get("referencia", ""),
            item.get("descripcion", ""),
            item.get("marca", ""),
            item.get("nombre_bodega", ""),
            item.get("cantidad_stock", ""),
            item.get("precio", ""),
            item.get("umb", "")
        ])

    return Response(
        csv_buffer.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=stock_filtrado.csv"}
    )

@app.route('/lista_conteo')
def lista_conteo():
    return render_template('lista_conteo.html')

@app.route('/fuera_base')
def fuera_base():
    return render_template('fuera_base.html')

@app.route('/cargue_db')
def cargue_db():
    return render_template('cargue_db.html')

@app.route('/administracion_usuarios', methods=['GET'])
@requiere_rol('admin')
def administracion_usuarios():
    response = requests.get(
        f'{SUPABASE_URL}/rest/v1/user_admin_plataform?select=id,username,password,email,rol',
        headers=SUPABASE_HEADERS
    )
    if response.status_code == 200:
        usuarios = response.json()
        return render_template('administracion_usuarios.html', usuarios=usuarios)
    else:
        return render_template('administracion_usuarios.html', error="No se pudieron cargar los usuarios")

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = {
        "username": request.form['username'],
        "email": request.form['email'],
        "password": request.form['password'],
        "rol": request.form['rol']
    }
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/user_admin_plataform",
        headers=SUPABASE_HEADERS,
        json=data
    )
    if response.status_code == 201:
        flash('✅ Usuario creado con éxito.')
    else:
        flash('❌ Error al crear usuario.')
    return redirect(url_for('administracion_usuarios'))

@app.route('/eliminar_usuario/<int:user_id>', methods=['POST'])
@requiere_rol('admin')
def eliminar_usuario(user_id):
    response = requests.delete(
        f"{SUPABASE_URL}/rest/v1/user_admin_plataform?id=eq.{user_id}",
        headers=SUPABASE_HEADERS
    )
    if response.status_code == 204:
        flash('🗑️ Usuario eliminado correctamente.')
    else:
        flash('❌ Error al eliminar usuario.')
    return redirect(url_for('administracion_usuarios'))

@app.route('/editar_usuario', methods=['POST'])
@requiere_rol('admin')
def editar_usuario():
    user_id = request.form['id']
    data = {
        "username": request.form['username'],
        "email": request.form['email'],
        "rol": request.form['rol']
    }
    response = requests.patch(
        f"{SUPABASE_URL}/rest/v1/user_admin_plataform?id=eq.{user_id}",
        headers=SUPABASE_HEADERS,
        json=data
    )
    if response.status_code == 204:
        flash('✏️ Usuario editado exitosamente.')
    else:
        flash('❌ Error al editar usuario.')
    return redirect(url_for('administracion_usuarios'))

if __name__ == "__main__":
    app.run(debug=True)