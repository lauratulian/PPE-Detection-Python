import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
from tkinter import filedialog, messagebox, ttk
from ultralytics import YOLO
from tkfontawesome import icon_to_image
import presentation.util.util_ventana as util_ventana
import presentation.util.util_imagenes as util_img

class FormMaestroDesign(tk.Tk):
    
    root = tk.Tk()

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./presentation/imagenes/logo.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python UTN')
        self.iconbitmap("./presentation/imagenes/logo.png")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        barra_superior = tk.Frame(self.root, bg=COLOR_BARRA_SUPERIOR, height=50)
        barra_superior.pack(side=tk.TOP, fill='both')

        menu_lateral = tk.Frame(self.root, bg=COLOR_MENU_LATERAL, width=150)
        menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        cuerpo_principal = tk.Frame(self.root, bg=COLOR_CUERPO_PRINCIPAL)
        cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

        return barra_superior, menu_lateral, cuerpo_principal
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="UTN")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="utn@frro.edu.ar")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
        # Botones del menú lateral
        
        self.buttonDashBoard = tk.Button(self.menu_lateral, command=self.detectar_video)         
        self.buttonProfile = tk.Button(self.menu_lateral, command=self.detectar_imagen)     
        self.buttonPicture = tk.Button(self.menu_lateral, command=self.abrir_camara) 
        self.buttonInfo = tk.Button(self.menu_lateral)        
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Cargar Video", "\uf109", self.buttonDashBoard),
            ("Cargar Imagen", "\uf007", self.buttonProfile),
            ("Video en vivo", "\uf03e", self.buttonPicture),
            ("Info", "\uf129", self.buttonInfo),
            ("Settings", "\uf013", self.buttonSettings)
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)                    
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
        
    def abrir_camara():
        pass

    def detectar_imagen():
        pass

    def detectar_video():
        pass