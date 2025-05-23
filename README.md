# CleanStock_project

 Contenido completo de README.md
markdown
Copiar
Editar
# 🧾 Cleanstock - Aplicación Web de Inventarios

**Cleanstock** es una aplicación web desarrollada con **Flask (Python)** para el backend y **HTML/CSS/JavaScript** en el frontend. Utiliza **Supabase** como base de datos en la nube, permitiendo gestionar inventarios y usuarios de manera intuitiva y moderna.

---

## 🚀 Funcionalidades

- ✅ Login seguro con sesión y validación
- ✅ Administración de usuarios (crear, editar, eliminar)
- ✅ Visualización de:
  - Stock
  - Lista de conteo
  - Cargue de base de datos
  - Elementos fuera de base
- ✅ Diseño responsivo con panel lateral y modales interactivos
- ✅ Integración con Supabase vía REST API

---

## 🛠 Requisitos

- Python 3.10 o superior  
- Git  
- (Opcional) Visual Studio Code

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/cleanstock.git
cd cleanstock
2. Crea y activa un entorno virtual
bash
Copiar
Editar
python -m venv venv
En Windows:

bash
Copiar
Editar
venv\Scripts\activate
En Mac/Linux:

bash
Copiar
Editar
source venv/bin/activate
3. Instala las dependencias
bash
Copiar
Editar
pip install -r requirements.txt
🔐 Configuración de Supabase
En el archivo app.py, asegúrate de tener configurado:

python
Copiar
Editar
SUPABASE_URL = 'https://<tu-proyecto>.supabase.co'
SUPABASE_KEY = 'tu_clave_publica'
Opcionalmente puedes usar variables de entorno con un archivo .env.

▶️ Ejecutar la aplicación
Una vez instalado todo, ejecuta:

bash
Copiar
Editar
python app.py
Abre tu navegador en:

cpp
Copiar
Editar
http://127.0.0.1:5000/
🧱 Estructura del proyecto
cpp
Copiar
Editar
📦 cleanstock/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── inicio.html
│   ├── login.html
│   ├── administracion_usuarios.html
│   └── ...
├── static/
│   ├── logo.png
│   ├── *.css
│   └── inicio.png
🔑 Acceso por defecto
Usuario: admin

Contraseña: 1234

(Puedes gestionarlo desde la tabla user_admin_plataform en Supabase).

📦 Despliegue (opcional)
Plataformas sugeridas:

Render

Railway

Fly.io

👨‍💻 Autor
Desarrollado por: [Tu nombre aquí]
Repositorio oficial: GitHub

📄 Licencia
Este proyecto está bajo la licencia MIT (o la que prefieras).

yaml
Copiar
Editar

---

## ✅ Próximo paso:
- Guarda este texto como `README.md` en la raíz de tu proyecto.
- Actualiza el nombre del autor, tu usuario de GitHub y la URL si vas a subirlo.

¿Te gustaría que también te cree un `.gitignore` listo para proyectos Flask y Python?