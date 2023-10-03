import tkinter
import sys
import tkinter.messagebox
import customtkinter

# Main
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Programación Lineal - Métodos Cuantitativos")  
        

        # Crear el marco principal
        self.frame1 = customtkinter.CTkFrame(self, border_width=2, width=300, height=100)
        self.frame1.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.frame1.grid_propagate(False) # desactiva el cambio de tamaño automático
        
        # Crear el marco de los colores
        self.colors = customtkinter.CTkFrame(self.frame1, border_width=2, width=200, height=20)
        self.colors.grid(row=1, sticky="nsew")
        #self.colors.grid_propagate(False) # desactiva el cambio de tamaño automático

        #La nueva idea es crear frames inifnitos de colores para llenar el frame de los colores, sinedo 
        #self.color(i) = customtkinter.CTKFrame(self.color, backgroundcolor=#sdfa)
        
        #Colores
        color_numer = ['red', 'green', 'blue', 'orange', 'purple', 'gray', 'brown', 'pink', 'yellow', 'cyan',
          'magenta', 'teal', 'navy', 'olive', 'maroon', 'lime', 'aqua', 'silver', 'black', 'white',
          'indigo', 'violet', 'turquoise', 'coral', 'gold', 'salmon', 'orchid', 'khaki', 'peru',
          'slategray', 'chartreuse', 'steelblue', 'tomato', 'plum', 'dodgerblue', 'sienna', 'seagreen',
          'sandybrown', 'rosybrown', 'mediumvioletred', 'mediumturquoise', 'mediumslateblue', 'mediumpurple',
          'mediumaquamarine', 'lightsteelblue', 'lightsalmon', 'lightseagreen', 'lightgray', 'lightcyan']

        #Colorear
        for i, color in enumerate(color_numer):
            frame = customtkinter.CTkFrame(self.colors, fg_color=color, width=15, height=20)
            frame.grid(row=0, column=i)    

        
if __name__ == "__main__":
    app = App()
    # Cerrar la ventana completamente

    def cerrar_ventana():
        app.destroy()
    # Agregar un botón de cerrar a la ventana
    app.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    app.mainloop()