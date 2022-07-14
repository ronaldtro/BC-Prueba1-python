import sqlite3


def main():
    
    #crearAlumnos() - Ya creados!
    verTabla()

    buscarAlumno('Camilo')  
    buscarAlumno('Ronald') 
    buscarAlumno('Roberto')     
    

def crearAlumnos():
    for i in range(1,9):
        nombres = ['Ronald','Camilo','Maria', 'Esteban', 'Nicol', 'Mafe', 'Luis', 'Miguel', 'Sandra', 'Salome'] 
        apellidos = ['Diaz', 'De la cruz', 'Guerra', 'Torres', 'Perez', 'zapateiro', 'Neftali', 'Gemelo', 'Contreras']
        crearAlumno(i, nombres[i], apellidos[i])

def buscarAlumno(nombre):
    conn = sqlite3.connect('prueba20.db')

    cursor = conn.cursor()

    rows = cursor.execute(f'SELECT * FROM Alumnos WHERE nombre="{nombre}" ')
    #rows = cursor.execute('INSERT INTO usuario(id, nombre, contrasena) VALUES(3, "Fabian", 1234)')

    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        #return False
        print(f"Alumn@ {nombre} no existe!")
        return

    #return True
    print(f"Alumn@ {data}")    

def verTabla():
    conn = sqlite3.connect('prueba20.db')

    cursor = conn.cursor()

    rows = cursor.execute('SELECT * FROM Alumnos')
    #rows = cursor.execute('INSERT INTO usuario(id, nombre, contrasena) VALUES(3, "Fabian", 1234)')

    #data = rows.fetchall()
    print('***** TABLA Alumnos ***')
    for elem in rows:
        print(elem)

    cursor.close()
    conn.close()
    print('***********************')

def crearAlumno(id, nombre, apellido):
    conn = sqlite3.connect('prueba20.db')

    cursor = conn.cursor()

    query = f'INSERT INTO Alumnos(id, nombre, apellido) VALUES({id}, "{nombre}", "{apellido}")'
    rows = cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
