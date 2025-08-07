import tkinter as tk
from tkinter import messagebox
import math

#Funcion que realiza la suma de dos numeros
def ventana_suma_dos_numeros():
    def calcular_suma():
        try:
            numero1 = float(entry1.get())
            numero2 = float(entry2.get())
            resultado = numero1 + numero2
            messagebox.showinfo("Resultado", f"La suma es: {resultado}")
            suma_win.destroy()
            ventana_funciones_extras()
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce números válidos.")

    suma_win = tk.Tk()
    suma_win.title("CALCULADORA- Suma 2 numeros")
    
    tk.Label(suma_win, text="Ingresa el primer número:").pack()
    entry1 = tk.Entry(suma_win)
    entry1.pack()

    tk.Label(suma_win, text="Ingresa el segundo número:").pack()
    entry2 = tk.Entry(suma_win)
    entry2.pack()

    tk.Button(suma_win, text="Sumar", command=calcular_suma).pack(pady=10)

    suma_win.mainloop()

#Se declaran las funciones para resta,multiplicacion,division
def ventana_funciones_extras():
    def calcular_operacion(op):
        try:
            n1 = float(entry_op1.get())
            n2 = float(entry_op2.get())
            if op == "resta":
                res = n1 - n2
            elif op == "multiplicacion":
                res = n1 * n2
            elif op == "division":
                if n2 == 0:
                    raise ZeroDivisionError
                res = n1 / n2
            resultado_var.set(f"Resultado: {res}")
            preguntar_otro(n1, n2)
        except ValueError:
            messagebox.showerror("Error", "Números inválidos.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "División por cero.")
#Se pregunta si se quiere realizar otra funcion
    def preguntar_otro(n1, n2):
        respuesta = messagebox.askquestion("Otra operación", "¿Deseas realizar otra función?")
        if respuesta == "yes":
            modulo = n1 % n2
            resultado_var.set(f"Módulo: {modulo}")
        else:
            funcionesE.destroy()
            menu_avanzado()

    funcionesE = tk.Tk()
    funcionesE.title("Operaciones +-*/")

    tk.Label(funcionesE, text="Número 1:").pack()
    entry_op1 = tk.Entry(funcionesE)
    entry_op1.pack()

    tk.Label(funcionesE, text="Número 2:").pack()
    entry_op2 = tk.Entry(funcionesE)
    entry_op2.pack()

    tk.Button(funcionesE, text="Restar", command=lambda: calcular_operacion("resta")).pack(pady=2)
    tk.Button(funcionesE, text="Multiplicar", command=lambda: calcular_operacion("multiplicacion")).pack(pady=2)
    tk.Button(funcionesE, text="Dividir", command=lambda: calcular_operacion("division")).pack(pady=2)

    resultado_var = tk.StringVar()
    tk.Label(funcionesE, textvariable=resultado_var, fg="blue").pack(pady=10)

    funcionesE.mainloop()

#Funcion para elegir la operacion suma, resta, multiplicacion, division y modulo
def menu_avanzado():
    def calcular_basico():
        try:
            n1 = float(entry1.get())
            n2 = float(entry2.get())
            op = operacion_var.get()
            if op == "Suma":
                res = n1 + n2
            elif op == "Resta":
                res = n1 - n2
            elif op == "Multiplicación":
                res = n1 * n2
            elif op == "División":
                res = n1 / n2
            elif op == "Módulo":
                res = n1 % n2
            resultado_var.set(f"Resultado: {res}")
        except Exception:
            resultado_var.set("Error en operación")
#Funcion para sumar 3 numeros
    def sumar_tres():
        try:
            num1 = float(entry3_1.get())
            num2 = float(entry3_2.get())
            num3 = float(entry3_3.get())
            res = num1 + num2 + num3
            resultado_var.set(f"Suma de 3 números: {res}")
        except:
            resultado_var.set("Error en suma")

    def evaluar_expresion():
        try:
            expr = entry_expr.get()
            res = eval(expr)
            resultado_var.set(f"Resultado: {res}")
        except:
            resultado_var.set("Expresión inválida")

    def volver_a_suma():
        vfuncion_extra.destroy()
        ventana_suma_dos_numeros()

    vfuncion_extra = tk.Tk()
    vfuncion_extra.title("Calculadora funciones extras")

    #Operación básica entre 2 números
    tk.Label(vfuncion_extra, text="Operaciones básicas entre 2 números").pack()
    entry1 = tk.Entry(vfuncion_extra)
    entry1.pack()
    entry2 = tk.Entry(vfuncion_extra)
    entry2.pack()

    operacion_var = tk.StringVar(value="Suma")
    opciones = ["Suma", "Resta", "Multiplicación", "División", "Módulo"]
    tk.OptionMenu(vfuncion_extra, operacion_var, *opciones).pack()
    tk.Button(vfuncion_extra, text="Calcular", command=calcular_basico).pack(pady=5)

    #Suma de 3 números
    tk.Label(vfuncion_extra, text="Sumar 3 números").pack()
    entry3_1 = tk.Entry(vfuncion_extra)
    entry3_1.pack()
    entry3_2 = tk.Entry(vfuncion_extra)
    entry3_2.pack()
    entry3_3 = tk.Entry(vfuncion_extra)
    entry3_3.pack()
    tk.Button(vfuncion_extra, text="Sumar 3", command=sumar_tres).pack(pady=5)

    #Operaciones mixtas
    tk.Label(vfuncion_extra, text="Operación mixta (Ej: 2+4-3*2/1)").pack()
    entry_expr = tk.Entry(vfuncion_extra, width=30)
    entry_expr.pack()
    tk.Button(vfuncion_extra, text="Evaluar", command=evaluar_expresion).pack(pady=5)

    #Resultado
    resultado_var = tk.StringVar()
    tk.Label(vfuncion_extra, textvariable=resultado_var, fg="green").pack(pady=10)

    #Botón para regresar a la ventana de inicio "Suma de dos numeros"
    tk.Button(vfuncion_extra, text="Regresar a ventana principal", command=volver_a_suma).pack(pady=10)

    vfuncion_extra.mainloop()


ventana_suma_dos_numeros()