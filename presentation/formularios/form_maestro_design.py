import tkinter as tk
from tkinter import font
from tkinter import ttk
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import presentation.util.util_ventana as util_ventana
import presentation.util.util_imagenes as util_img
from tkfontawesome import icon_to_image

class FormMaestroDesign(tk.Tk):
    icon_images = {}

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./presentation/imagenes/logo.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        self.title('Python UTN')
        self.iconbitmap("./presentation/imagenes/logo.png")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="UTN")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelInfo = tk.Label(self.barra_superior, text="utn@frro.edu.ar")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.icon_images["live"] = icon_to_image("video", fill="#FFFFFF", scale_to_width=16)
        self.icon_images["upload"] = icon_to_image("upload", fill="#FFFFFF", scale_to_width=16)
        self.icon_images["info"] = icon_to_image("info-circle", fill="#FFFFFF", scale_to_width=16)
        self.icon_images["quit"] = icon_to_image("power-off", fill="#FFFFFF", scale_to_width=16)

        buttonLive = tk.Button(self.menu_lateral, image=self.icon_images["live"], text="Video en vivo", compound=tk.LEFT,
                            command=self.start_camera_detection, bd=0, bg=COLOR_MENU_LATERAL, fg="white", font=font_awesome,
                            padx=10)
        buttonUpload = tk.Button(self.menu_lateral, image=self.icon_images["upload"], text="Subir archivo", compound=tk.LEFT,
                                command=self.upload_file, bd=0, bg=COLOR_MENU_LATERAL, fg="white", font=font_awesome,
                                padx=10)
        buttonInfo = tk.Button(self.menu_lateral, image=self.icon_images["info"], text="Info", compound=tk.LEFT,
                                bd=0, bg=COLOR_MENU_LATERAL, fg="white", font=font_awesome,
                                padx=10)
        buttonQuit = tk.Button(self.menu_lateral, image=self.icon_images["quit"], text="Salir", compound=tk.LEFT,
                                command=self.destroy, bd=0, bg=COLOR_MENU_LATERAL, fg="white", font=font_awesome,
                                padx=10)

        buttonLive.pack(side=tk.TOP, pady=20, anchor="w")
        buttonUpload.pack(side=tk.TOP, pady=20, anchor="w")
        buttonInfo.pack(side=tk.TOP, pady=20, anchor="w", fill=tk.X)
        buttonQuit.pack(side=tk.TOP, pady=20, anchor="w", fill=tk.X)

    def controles_cuerpo(self):
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        # Limpiar el cuerpo principal
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

        # Mostrar la imagen del logo al inicio
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        global content_label
        content_label = ttk.Label(self.cuerpo_principal, font=('Segoe UI', 14))
        content_label.pack(expand=True, anchor="center")



    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def update_display(self, image):
        pass

    def start_camera_detection(self):
        pass

    def process_image(self, image_path):
        pass

    def process_video(self, video_path):
        pass
