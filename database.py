import sqlite3
import os

def init_db():
    # En internet usamos la carpeta temporal '/tmp', en tu Mac usa la carpeta normal
    if os.environ.get('RENDER'):
        db_path = '/tmp/database.db'
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'database.db')
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("¡Base de datos creada con éxito!")
