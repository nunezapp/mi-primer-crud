from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# LEER (Read) - Muestra todas las tareas
@app.route('/')
def index():
    conn = get_db_connection()
    tareas = conn.execute('SELECT * FROM tareas').fetchall()
    conn.close()
    return render_template('index.html', tareas=tareas)

# CREAR (Create) - Añade una nueva tarea
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO tareas (titulo, descripcion) VALUES (?, ?)', (titulo, descripcion))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

# ELIMINAR (Delete) - Borra una tarea por su ID
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tareas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
# ACTUALIZAR (Update) - Editar una tarea existente
@app.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    tarea = conn.execute('SELECT * FROM tareas WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']

        conn.execute('UPDATE tareas SET titulo = ?, descripcion = ? WHERE id = ?', (titulo, descripcion, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('update.html', tarea=tarea)

if __name__ == '__main__':
    app.run(debug=True)
