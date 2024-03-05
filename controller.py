import sqlite3 as sql

def createDB():
    conn = sql.connect('comercios.db')
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect('comercios.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE comercios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            email TEXT,
            direccion TEXT,
           rubro TEXT,
           telefono1 VARCHAR(20),
           telefono2 VARCHAR(20),
           comentarios TEXT
            )"""
    )
    conn.commit()
    conn.close()    

if __name__ == '__main__':
    #createDB()
    createTable()