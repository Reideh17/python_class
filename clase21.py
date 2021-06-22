from tkinter import Button, Entry, Label,Tk,messagebox,Menu



def crearCampos():
    
    labelNumeroTriangulo = Label(ventanaPrincipal,text="No Triángulo",bg = "cyan")
    labelNumeroTriangulo.grid(padx=30,pady=30, column=4,row=0)

    idTriangulo        = Entry(ventanaPrincipal,width=20)
    idTriangulo.grid(column=5,row=0)

    labelLadoUno         = Label(ventanaPrincipal,text="Lado Uno",bg = "cyan")
    labelLadoUno.grid(padx=30, column=2,row=1)
    ladoUnoTriangulo   = Entry(ventanaPrincipal,width=15)
    ladoUnoTriangulo.grid(column=3,row=1)

    labelLadoDos         = Label(ventanaPrincipal,text="Lado Dos",bg = "cyan")
    labelLadoDos.grid(padx=30, column=4,row=1)
    ladoDosTriangulo   = Entry(ventanaPrincipal,width=15)
    ladoDosTriangulo.grid(column=5,row=1)

    labelLadoTres        = Label(ventanaPrincipal,text="Lado Tres",bg = "cyan")
    labelLadoTres.grid(padx=30,column=6,row=1)
    ladoTresTriangulo  = Entry(ventanaPrincipal,width=15)
    ladoTresTriangu
