import sqlite3

conn = sqlite3.connect("BaseAlumnos")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE ALUMNOS (
    ID INTEGER PRIMARY KEY,
    NOMBRE VARCHAR(20),
    APELLIDO VARCHAR(20))
''')

datosAlumnos = [
    (1, 'Pedro', 'Martinez'),
    (2, 'Maria', 'Perez'),
    (3, 'Luis', 'Ramos'),
    (4, 'José', 'Rodriguez'),
    (5, 'Carlos', 'Martinez'),
    (6, 'Miguel', 'Lopez'),
    (7, 'Jesus', 'Ramos'),
    (8, 'Ana', 'Fuentes')
]
cursor.executemany("INSERT INTO ALUMNOS VALUES (?,?,?)", datosAlumnos)

rows = cursor.execute("SELECT * FROM ALUMNOS WHERE NOMBRE='Maria'")
for row in rows:
    print(row)

conn.commit()
cursor.close()
conn.close()
