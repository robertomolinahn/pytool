import tkinter
import random
import string

#creacion de la ventana
ventana = tkinter.Tk()
ventana.geometry("300x300")
ventana.title("Aplicativos")


password_lenght_label = tkinter.Label(ventana, text="Largo del password ").grid(row=1, column=0)
password_lenght_entry = tkinter.Entry(ventana)
password_lenght_entry.grid(row=1, column=1)

password = tkinter.Label(ventana, text="Password").grid(row=2, column=0)
password_entry = tkinter.Entry(ventana)
password_entry.grid(row=2, column=1, columnspan=3)

default_value=16
password_lenght_entry.insert(0, default_value)

def sub_password_generator():
    N2 = password_lenght_entry.get()
    def password_generator(chars = string.ascii_uppercase + string.digits, N=int(N2)):
        
        return ''.join(random.choice(chars) for _ in range(N))

    valor = password_generator(chars='abcdefghñ123456ABCDEFGHJKLMNOPQRSTWÑ!"#$%/?¡¿')
    password_entry.insert(0, valor)



bonton_generar_password = tkinter.Button(ventana, text="Generar", fg="white", bg="green", command=sub_password_generator).grid(row=4, column=1, columnspan=2)

ventana.mainloop()