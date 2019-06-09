from tkinter import *
from tkinter import messagebox
import sqlite3

"""----------------------------------Funciones-----------------------------------------"""

def conexionBBDD(): #creando la base de datos
    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE DATOSUSUARIO
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50), APELLIDO VARCHAR(10),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR (100))
        ''')

    messagebox.showinfo("BBDD", "Base creada")

def salirDelPrograma(): #funcion para salir del programa

	valor = messagebox.askquestion("Salir", "¿Realmente quiere salir del programa?")

	if valor =="yes":
		root.destroy() #cierra el programa

def limpiarCuadros():

	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	textoComentario.delete(1.0, END) #borra desde el primer carcter hasta el final 

def crear():
	miConexion=sqlite3.connect("Usuarios")

	miCursor = miConexion.cursor()

	miCursor.execute("INSERT INTO DATOSUSUARIO VALUES(NULL, '" + miNombre.get() + 
		"','" + miPass.get() + 
		"','" + miApellido.get() + 
		"','" + miDireccion.get() + 
		"','" + textoComentario.get("1.0", END) + "')")

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito.")

def leer():
	miConexion=sqlite3.connect("Usuarios")

	miCursor = miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIO WHERE ID=" + miId.get())

	elUsuario = miCursor.fetchall()

	for usuario in elUsuario:

		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor = miConexion.cursor()

	miCursor.execute("UPDATE DATOSUSUARIO SET NOMBRE_USUARIO= '" + miNombre.get() + 
		"', PASSWORD = '" + miPass.get() + 
		"', APELLIDO = '" + miApellido.get() + 
		"', DIRECCION = '" + miDireccion.get() + 
		"', COMENTARIOS = '" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())


	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con éxito.")

def borrar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor = miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSUSUARIO WHERE ID=" + miId.get())

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro eliminado con éxito")

def aCercaDe():

	messagebox.showinfo("A cerca de", "Versión de práctica CRUD By Gabriela Vilaró")

"""-------------------------Creación del menú del CRUD-------------------------"""
root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0) #armando el menú
                            #saca las lineas
bbddMenu.add_command(label="Conectar", command = conexionBBDD) #acá conecto con la base de datos
bbddMenu.add_command(label="Salir", command = salirDelPrograma)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command = limpiarCuadros)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command = crear)
crudMenu.add_command(label="Leer", command = leer)
crudMenu.add_command(label="Actualizar", command = actualizar)
crudMenu.add_command(label="Borrar", command = borrar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="A cerca de", command = aCercaDe)

barraMenu.add_cascade(label="Base de datos", menu=bbddMenu)#acomodo los elementos en el menú
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

"""----------------------------------Creación de los cuadros del crud-------------------------------"""

miFrame =Frame(root)
miFrame.pack()

miId = StringVar() #tipo entry
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

cuadroID=Entry(miFrame, textvariable = miId)
cuadroID.grid(row=0, column = 1, padx=10, pady=10) #Se ubica en la fila 0, columna 1

cuadroNombre=Entry(miFrame, textvariable = miNombre)
cuadroNombre.grid(row=1, column = 1, padx=10, pady=10) #Se ubica en la fila 1, columna 1
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable = miPass)
cuadroPass.grid(row=2, column = 1, padx=10, pady=10) #Se ubica en la fila 2, columna 1
cuadroPass.config(show="°")

cuadroApellido=Entry(miFrame, textvariable = miApellido)
cuadroApellido.grid(row=3, column = 1, padx=10, pady=10) #Se ubica en la fila 3, columna 1

cuadroDireccion=Entry(miFrame, textvariable = miDireccion)
cuadroDireccion.grid(row=4, column = 1, padx=10, pady=10) #Se ubica en la fila 4, columna 1

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column = 1, padx=10, pady=10) #Se ubica en la fila 5, columna 1

scrollVert=Scrollbar(miFrame, command=textoComentario.yview) #deslizador
scrollVert.grid(row=5, column=2, sticky="nsew") #fila 5

textoComentario.config(yscrollcommand=scrollVert.set)

"""-----------------------------Creación de las etiquetas de los cuadros---------------------------- """

idLabel = Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)#columna 0 para que este al costado del cuadro, fila 0

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

"""---------------------------------Creación de los botones del crud----------------------------------------"""

miFrame2=Frame(root)

miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command = crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command = leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command = actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=borrar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()