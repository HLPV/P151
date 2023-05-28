from tkinter import *
root = Tk()
root.title("Sales Application")
root.geometry("400x400")
root.configure(background = "red")

mes = Label(root)
ventas = Label(root)

maximo_ventas = Label(root)
minimo_ventas = Label(root)


Mess=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
Ventas=(1000,2000,800,2500,5000,500,600.1000,2000,3500,7500,2500,3000)

def maximo():
    max_ventas=max(Ventas)
    print(max_ventas)
    max_ventas_indice=Ventas.index(max_ventas)
    print(max_ventas_indice)
    max_ventas_mes=Mess[max_ventas_indice]
    print("la ganancia maxima de "+str(max_ventas)+" se registro en el mes de "+(max_ventas_mes))
    maximo_ventas['text'] = "El maximo de ventas fue "+str(max_ventas)+" y fue en "+str(max_ventas_mes)
    
def minimo():
    min_ventas=min(Ventas)
    print(min_ventas)
    min_ventas_indice=Ventas.index(min_ventas)
    print(min_ventas_indice)
    min_ventas_mes=Mess[min_ventas_indice]
    print("la ganancia minima de "+str(min_ventas)+" se registro en el mes de "+(min_ventas_mes))
    minimo_ventas['text'] = "El minimo de ventas fue "+str(min_ventas)+" y fue en "+str(min_ventas_mes)

btn_max = Button(root, text="Maximo de ventas", command=maximo, bg = "Royal blue", fg = "white")
btn_min = Button(root, text="Minimo de ventas", command=minimo, bg = "Royal blue", fg = "white")

btn_max.place(relx=0.5, rely=0.4, anchor=CENTER)

maximo_ventas.place(relx=0.5, rely=0.5, anchor=CENTER)
minimo_ventas.place(relx=0.5, rely=0.7, anchor=CENTER)

btn_min.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()