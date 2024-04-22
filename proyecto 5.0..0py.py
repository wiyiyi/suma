import tkinter as tk
from tkinter import messagebox
import subprocess

#defs

def validar_login():

    usuario = entry_usuario.get()
    clave = entry_clave.get()

    if usuario == "doc1" and clave == "1234":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso") 
        ruta_archivo = "proyecto parte willy.py"
        subprocess.run(["python", ruta_archivo])
        ventana.destroy()

    elif usuario=="doc1" and clave !="1234":
        messagebox.showerror( "Intente de Nuevo","Contraseña Incorrecta")
        entry_clave.config(bg="red")
    elif usuario!="doc1" and clave=="1234":
        messagebox.showerror("Intente de Nuevo","Usuario Incorrecto")
        entry_usuario.config(bg="red")
    if not usuario or not clave:
        messagebox.showerror("Error de inicio de sesión", "Por favor, ingrese usuario y contraseña")

        return   
   
def recuperar():
    ventana_recuperacion = tk.Toplevel(ventana)
    ventana_recuperacion.title("Recuperar contraseña")
    ventana_recuperacion.geometry("300x150")
    ventana_recuperacion.transient(ventana)
    ventana_recuperacion.grab_set()

    tk.Label(ventana_recuperacion, text="Introduce tu correo electrónico:", font=("arial", 12)).pack(pady=5)
    correo_entry = tk.Entry(ventana_recuperacion, font=("arial", 12))
    correo_entry.pack(pady=5, padx=10)

    def enviar_correo():
        correo = correo_entry.get()
        if correo:
            messagebox.showinfo("Recuperar contraseña", f"Se ha enviado un correo de recuperación a {correo}")
            ventana_recuperacion.destroy()
        else:
            messagebox.showerror("Recuperar contraseña", "Por favor, introduce tu correo electrónico")

    enviar_button = tk.Button(ventana_recuperacion, text="Enviar Mensaje", command=enviar_correo, font=("Helvetica", 12))
    enviar_button.pack(pady=5)

#ventana inicio
ventana = tk.Tk()
ventana.title("Bienvenido a la clinica dd")
ventana.configure(bg="#00295A")

bienve=tk.Label(ventana,text="Bienvenido",font="arial 13",bg="#00295A",fg="#460202")
bienve.pack()


marc=tk.LabelFrame(ventana)
marc.config(bg="#003676",relief=tk.RAISED)
marc.pack()

#etiquetas

etiqueta_usuario = tk.Label(marc,text="Usuario:")
etiqueta_usuario.grid(row=0, column=0, padx=10, pady=5)

etiqueta_clave = tk.Label(marc, text="Contraseña:")
etiqueta_clave.grid(row=1, column=0, padx=10, pady=5)

entry_usuario = tk.Entry(marc)
entry_usuario.grid(row=0, column=1, padx=20, pady=10)

entry_clave = tk.Entry(marc, show="*")
entry_clave.grid(row=1, column=1, padx=20, pady=10)

boton_login = tk.Button(marc, text="Iniciar Sesión") 
boton_login.grid(row=2,column=1, padx=20, pady=5,sticky="ew")

recuperar= tk.Button(marc, text="Recuperar contraseña",font="Arial 10",fg="blue")
recuperar.grid(padx=20,pady=5,sticky="w" ,row=5,column=1)


ventana.mainloop()

#programa 2

import tkinter as tk  
from tkinter import ttk, messagebox
import subprocess


def cerrar_y_abrir():
    # Cierra la ventana actual
    vent.destroy()
    # Abre una nueva ventana
  
    vent2 = "gastosmedicos.py"
    subprocess.run(["python", vent2])


vent= tk.Tk()
vent.title("Segunda")
 
enf = tk.Label(vent, text="Enfermedades:", font=("Arial", 12, "bold"))
enf.grid(row=0, column=0, padx=10, pady=10)

sele = tk.Label(vent, text="Seleccione que busca:", font=("Arial", 12, "bold"))
sele.grid(row=7, column=0, padx=10, pady=10)

pag2=tk.Button(vent,text="Gastos medicos",font=("arial",10,"bold"),fg="red",command=cerrar_y_abrir) 




combo = ttk.Combobox(vent, values=["QUIMIOTERAPIA", "CIRUGIA", "TERAPIA HORMONAL","TERAPIA DIRIGIDA","TERAPIA DE CELULAS MADRES"])
combo.grid(row=9, column=0, sticky="ew", padx=10,columnspan=2)

c1=tk.Checkbutton(vent, text="Cancer de Pancreas")
c2 = tk.Checkbutton(vent, text="Cancer de Pulmon" )
c3 = tk.Checkbutton(vent, text="Cancer de Mama" )
c4 = tk.Checkbutton(vent, text="Cancer de Prostata")
c5 = tk.Checkbutton(vent, text="Cancer de Riñon")
c6 = tk.Checkbutton(vent, text="Cancer de Vejiga")
c7 = tk.Checkbutton(vent, text="Cancer de Higado")
c8 = tk.Checkbutton(vent, text="Cancer de Estomago")
c9 = tk.Checkbutton(vent, text="Cancer de Piel")
c10 = tk.Checkbutton(vent, text="Cancer de Utero")
c11 = tk.Checkbutton(vent, text="Cancer de Vagina")
c12 = tk.Checkbutton(vent, text="Cancer de Colorrectal")
c13 = tk.Checkbutton(vent, text="Cancer de Tiroides")
c14 = tk.Checkbutton(vent, text="Cancer de Colon")


c1.grid(row=1, column=0, sticky="w", padx=10)
c2.grid(row=1, column=1, sticky="w", padx=10)
c3.grid(row=1, column=2, sticky="w", padx=10)
c4.grid(row=2, column=0, sticky="w", padx=10)
c5.grid(row=2, column=1, sticky="w", padx=10)
c6.grid(row=2, column=2, sticky="w", padx=10)
c7.grid(row=3, column=0, sticky="w", padx=10)
c8.grid(row=3, column=1, sticky="w", padx=10)
c9.grid(row=3, column=2, sticky="w", padx=10)
c10.grid(row=4, column=0, sticky="w", padx=10)
c11.grid(row=4, column=1, sticky="w", padx=10)
c12.grid(row=4, column=2, sticky="w", padx=10)
c13.grid(row=5, column=0, sticky="w", padx=10)
c14.grid(row=5, column=1, sticky="w", padx=10)

ventana.bind('<Return>', lambda event=None: boton_login.invoke())
pag2.grid(row=10,column=3,padx=10,pady=10,columnspan=3)
vent.geometry("")




