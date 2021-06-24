"""
  Interfaz gráfica 

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-07-2021          Versión inicial del programa
     
"""
###############################
# VERSION 0 : Interfaz gráfica
###############################

# from tkinter import Button, Canvas, Entry, Label, Menu, Message, PhotoImage, StringVar, Text, Tk, Variable,messagebox
# from tkinter.constants import BOTTOM, CENTER, LEFT, RAISED, RIGHT, TOP


# def oprimirBoton():
#     messagebox.showinfo("Ventana de Información", "oprimió un boton")    

# #Crear la ventana Principal
# ventanaPrincipal = Tk()
# ventanaPrincipal.title("Triángulos")
# ventanaPrincipal.geometry("800x500")

# Crear imagen ( formato pgm y gif)
# imagen = PhotoImage(file="gato.gif")

# Crear un label con imagen
# etiquetaImagen = Label(ventanaPrincipal,image=imagen)
# etiquetaImagen.pack()


# Crear un label con texto
# etiqueta = Label(ventanaPrincipal,text="Este es un Label")
# etiqueta.config(fg="blue", bg="green", font=("Verdana",24)) 
# etiqueta.pack()

# Crear una caja de texto
# texto = Entry(ventanaPrincipal,width=5)
# texto.pack()


# Guardar el valor de una variable en una caja de texto
# valor = 1
# valor = str(valor)
# textoEntry = StringVar()
# textoEntry.set(valor)
# textExample = Entry(ventanaPrincipal,textvariable=textoEntry)
# textExample.pack()


# Message

# messagebox.showinfo("Ventana de Información", "Esta es una información")
# messagebox.showwarning("Ventana de Advertencia", "Esta es una advertencia")
# messagebox.showerror("Ventana de Error", "Este es un Error")
# messagebox.askquestion("Ventana de Pregunta", "¿Esta seguro?")
# messagebox.askokcancel("Ventana de Ok o  Cancelar", "¿Desea continuar?")
# messagebox.askyesno("Ventana de yes o no ", "¿Si o no?")
# messagebox.askretrycancel("Ventana de reintentar o canceler", "¿Reintentar?")  

# Posicionar: Metodo place
# texto = Entry(ventanaPrincipal,width=5)
# texto.place(x=100,y=40)

# Posicionar: Metodo grid
# etiqueta = Label(ventanaPrincipal,text="Este es un Label")
# etiqueta.grid(row=0,column=0)

# texto = Entry(ventanaPrincipal,width=5)
# texto.grid(row=0,column=1)

# etiquetaDos = Label(ventanaPrincipal,text="Este es un Label 2")
# etiquetaDos.grid(row=0,column=2)


# Posicionar: Metodo pack()
# etiqueta = Label(ventanaPrincipal,text="Este es un Label ")
# etiqueta.pack()

# etiquetaUno = Label(ventanaPrincipal,text="Este es un Label 1")
# etiquetaUno.pack(side=LEFT)

# etiquetaDos = Label(ventanaPrincipal,text="Este es un Label 2")
# etiquetaDos.pack(side=RIGHT)

# etiquetaTres = Label(ventanaPrincipal,text="Este es un Label 3")
# etiquetaTres.pack(side=BOTTOM)

# Crear el menu principal
# menuBarra = Menu(ventanaPrincipal)
# menuBarra.add_command(label="Salir")

# # Mostrar el menu
# ventanaPrincipal.config(menu=menuBarra)

# Mostrar la ventana
# ventanaPrincipal.mainloop()