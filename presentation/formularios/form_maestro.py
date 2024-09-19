from ultralytics import YOLO
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np
from presentation.formularios.form_maestro_design import FormMaestroDesign

model = YOLO(".\best.pt")
class FormMaestro(FormMaestroDesign):
    
    def __init__(self):
        super().__init__()    

    def abrir_camara():
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error al abrir la cámara.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error al capturar el fotograma.")
                break

            frame = imutils.resize(frame, width=640)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            # Realizar detección con YOLO
            results = model(frame)
            annotated_frame = results[0].plot()

            # Mostrar resultados en tiempo real
            cv2.imshow("Detección en tiempo real", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def detectar_imagen():
        # Lógica para seleccionar imagen y procesar
        from tkinter import filedialog
        archivo = filedialog.askopenfilename(filetypes=[('Imagenes', '*.jpg')])
        if archivo:
            image = cv2.imread(archivo)
            
            if image is None:
                print("Error al cargar la imagen.")
                return
            results = model(image)
            annotated_image = results[0].plot()
            cv2.imshow("Detección en imagen", annotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def detectar_video():
        # Lógica para seleccionar video y procesar
        from tkinter import filedialog
        archivo = filedialog.askopenfilename(filetypes=[('Videos', '*.mp4')])
        if archivo:
            cap = cv2.VideoCapture(archivo)
            if not cap.isOpened():
                print("Error al abrir el video.")
                return
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error al capturar el fotograma o video terminado.")
                    break
                results = model(frame)
                annotated_frame = results[0].plot()
                cv2.imshow("Detección en video", annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()