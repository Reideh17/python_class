"""
#   Interfaz gráfica y Conexión a Base de Datos

#   Autor :  Formador
# |
#   Creación/ Actualización  Observaciones
#      Junio-07-2021          Versión inicial del programa
#      Junio-20-2021          Ajustes varios
     

###############################
# VERSION 0 : Interfaz gráfica
###############################

# from tkinter import Tk

# # Crear la ventana Principal
# ventanaPrincipal = Tk()

# # Mostrar la ventana
# ventanaPrincipal.mainloop()


########################################################
# # VERSION 1 : Interfaz gráfica y conectividad con BD
# ######################################################

# import sqlite3
# from   tkinter import *
# from   tkinter import Button, Entry, Frame, Label, Scrollbar,Tk,messagebox,Menu, ttk
# from   tkinter.constants import BOTH, BOTTOM, LEFT, RIGHT, TOP, X, YES

# def crearCamposInsertar(marcoOperaciones)->Entry:
#     """
#       Parámetros: Un objeto tipo frame para incluir widgets de entrada y etiquetas.
#       Retorno   :    Identificadores de variables para obtener los valores de lados de los triángulos.
#     """

#     labelLadoUno      = Label(marcoOperaciones,text="Lado Uno :",font=('arial', 8,"bold"),bg="salmon")
#     ladoUnoTriangulo  = Entry(marcoOperaciones,width=5)
#     labelLadoUno.place(x = 65, y = 2)
#     ladoUnoTriangulo.place(x = 130, y = 2)

#     labelLadoDos      = Label(marcoOperaciones,text="Lado Dos :",font=('arial', 8,"bold"),bg="salmon")
#     ladoDosTriangulo  = Entry(marcoOperaciones,width=5)
#     labelLadoDos.place(x = 170, y = 2)
#     ladoDosTriangulo.place(x = 235, y = 2)

#     labelLadoTres      = Label(marcoOperaciones,text="Lado Tres",font=('arial', 8,"bold"),bg="salmon")
#     ladoTresTriangulo  = Entry(marcoOperaciones,width=5)
#     labelLadoTres.place(x = 275, y = 2)
#     ladoTresTriangulo.place(x = 340, y = 2)

#     return  ladoUnoTriangulo,ladoDosTriangulo,ladoTresTriangulo

# def crearBotones(marcoOperaciones)->Button:
#     """
#       Parámetros: Un objeto tipo frame para incluir Botones de operaciones.
#       Retorno   : Identificadores de variables tipo Button, para ejecutar operaciones.
#     """

#     botonInsertar   = Button(marcoOperaciones,text="Crear Δ ",bg = "white",font=('arial', 8,"bold"),command=insertarTriangulo)    
#     botonInsertar.place(x = 480, y = 2)

#     botonBorrar     = Button(marcoOperaciones,text="Borrar Δ ",bg = "white",font=('arial', 8,"bold"),command=borrarTriangulo)
#     botonBorrar.place(x = 540, y = 2)
    
#     botonConsultar  = Button(marcoOperaciones,text="Consultar Δ ",bg = "white",font=('arial', 8,"bold"), command=consultarTriangulo)
#     botonConsultar.place(x = 600, y = 2)

#     return botonInsertar,botonBorrar,botonConsultar

# def conectarBD():
#     """
#       Parámetros : No recibe parámetros.
#       Retorno    : Identificadores de variables tipo conexión y cursor(para ejecutar sentencias SQL).
#     """
#     conexion = sqlite3.connect('C:\database\geometria.db')
#     cursor   = conexion.cursor()
#     return conexion,cursor


# def insertarTriangulo():
#     """
#       Parámetros: No recibe parámetros.
#       Cuerpo    : Ejecuta la sentencia insert de sql.
#       Retorno   : None.
#     """
#     datos    = ladoUnoTriangulo.get(),ladoDosTriangulo.get(),ladoTresTriangulo.get()
#     try:
#           cursor.execute("INSERT INTO triangulo VALUES (NULL,?,?,?)",(datos))
#           conexion.commit()
#           messagebox.showinfo('Base de Datos','Triángulo insertado exitosamente')
#     except: 
#           messagebox.showwarning('ADVERTENCIA','Fallo en la inserción del triángulo')


# def consultarTriangulo():
#     """
#       Parámetros: No recibe parámetros
#       Cuerpo    : Ejecuta la sentencia select de sql
#       Retorno   : None
#     """

#     registros = tablaConsulta.get_children()
#     for elemento in registros:
#         tablaConsulta.delete(elemento)
#     sql = "SELECT * from triangulo"
#     try:
#         cursor.execute(sql)
#         for row in cursor:

#             tablaConsulta.insert("",'end',values=(row[0],row[1],row[2],row[3]))
#     except:
#         messagebox.showwarning('ADVERTENCIA','Su consulta no arrojó resultados')


# def mostrarConsulta()->ttk.Treeview:
#     """
#       Parámetros: No recibe parámetros
#       Retorno   : Un identifador de variable tipo Treeview, para visualizar en el el resultado
#                   de una consulta SQL
#     """

#     scrollbarY = Scrollbar(marcoPrincipal, orient=VERTICAL)
    
#     tablaConsulta = ttk.Treeview(marcoPrincipal, columns=("primeraColumna", "segundaColumna", "terceraColumna","cuartaColumna"), yscrollcommand=scrollbarY.set)
#     tablaConsulta.heading('primeraColumna', text="Id Δ")
#     tablaConsulta.heading('segundaColumna', text="1er Lado Δ")
#     tablaConsulta.heading('terceraColumna', text="2do Lado Δ")
#     tablaConsulta.heading('cuartaColumna',  text="3er Lado Δ")
#     tablaConsulta.column('#0',stretch=NO, minwidth=0, width=0)
#     tablaConsulta.column('#1', width=100, anchor=CENTER)
#     tablaConsulta.column('#2', width=100, anchor=CENTER)
#     tablaConsulta.column('#3', width=100, anchor=CENTER)
#     tablaConsulta.column('#4', width=100, anchor=CENTER)
    
#     scrollbarY.config(command=tablaConsulta.yview)
#     scrollbarY.pack(side=RIGHT, fill=Y)

#     estilo = ttk.Style()
#     estilo.theme_use('clam')
#     estilo.configure('Treeview.Heading', background="dark turquoise",font=('arial', 8,"bold"))

#     tablaConsulta.pack(side=LEFT, expand = YES,fill = BOTH)

#     return tablaConsulta

# def borrarTriangulo():
#     """
#       Parámetros: No recibe parámetros.
#       Cuerpo    : Ejecuta la sentencia delete de sql.
#       Retorno   : None.
#     """


#     if messagebox.askyesno(message="Los datos se perderán definitivamente. ¿Desea Continuar",title="Advertencia"):
#        sql = "DELETE FROM triangulo"
#        try: 
#         cursor.execute(sql)
#         conexion.commit()
#         messagebox.showinfo('Base de Datos','Los triángulos fueron borrados con éxito')

#        except:
#             messagebox.showwarning('ADVERTENCIA','Fallo borrando triángulos')
#     else:
#         pass

# def salirAplicacion():
#     """
#       Parámetros: No recibe parámetros.
#       Retorno   : None.
#     """
#     if messagebox.askyesno(message="¿Desea Salir de la Aplicación?",title="Advertencia"):
#         conexion.close()
#         ventanaPrincipal.destroy()


# #============================= FIN FUNCIONES ========================================


# # Crear la ventana Principal
# ventanaPrincipal = Tk()
# ventanaPrincipal.title("Triángulos")
# ventanaPrincipal.geometry("800x300")

# # Crear el marco Principal
# marcoPrincipal = Frame(ventanaPrincipal, width=800, height=50, bd=5, bg='pale turquoise',relief='sunken',cursor='spider')
# marcoPrincipal.pack( expand = YES, fill = BOTH)

# # Crear el marco de abajo: con el texto Python - Conexión a Base de Datos
# marcoAbajo = Frame(ventanaPrincipal, width=800, height=50, bd=5, bg='dark turquoise',relief='flat',cursor='heart')
# marcoAbajo.pack(side=TOP)

# tituloAbajo = Label(marcoAbajo, width=800, font=('arial', 12,"bold"), bg='dark turquoise',text = "Python - Conexión a Base de Datos")
# tituloAbajo.pack(side=TOP)

# # Crear el marco de operaciones : crear, consultar y borrar un triángulo
# marcoOperaciones = Frame(marcoPrincipal, width=800, height=30, bd=5, bg='salmon',relief='flat',cursor='heart')
# marcoOperaciones.pack(fill = X,side=BOTTOM)

# # Crear campos de captura para los lados del triángulo
# ladoUnoTriangulo,ladoDosTriangulo,ladoTresTriangulo = crearCamposInsertar(marcoOperaciones)

# # Crear los botones de crear, consultar y borrar un triángulo
# crearBotones(marcoOperaciones)

# # Conectarse a la base de datos
# conexion,cursor = conectarBD()

# # Crear la estructura para mostrar la consulta 
# tablaConsulta = mostrarConsulta()

# # Crear el menu principal
# menuBarra = Menu(ventanaPrincipal)
# menuBarra.add_command(label="Salir", command=salirAplicacion)

# # Mostrar el menu
# ventanaPrincipal.config(menu=menuBarra)

# # Mostrar la ventana
# ventanaPrincipal.mainloop()


