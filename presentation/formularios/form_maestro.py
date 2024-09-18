from ultralytics import YOLO
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox, Label, Button, filedialog
from presentation.formularios.form_maestro_design import FormMaestroDesign
import imutils
import numpy as np

class FormMaestro(FormMaestroDesign):

    def __init__(self):
        super().__init__()  
        self.cap = None
        self.model = "./best.pt"
        self.content_label = Label()
        self.content_label.pack()
        self.model = YOLO(self.model_path)

    def update_display(self, image):
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        if hasattr(self, 'content_label'):
            self.content_label.configure(image=image)
            self.content_label.image = image
        else:
            print("content_label no está definido.")

    def start_camera_detection(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "No se pudo abrir la cámara.")
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error al capturar el fotograma.")
                break

            frame = imutils.resize(frame, width=640)
            results = self.model(frame)
            annotated_frame = results[0].plot()

            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            self.update_display(annotated_frame)

            self.root.update_idletasks()
            self.root.update()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def process_image(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            messagebox.showerror("Error", "No se pudo cargar la imagen.")
            return

        results = self.model(image)
        annotated_image = results[0].plot()

        annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        self.update_display(annotated_image)

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            messagebox.showerror("Error", "No se pudo abrir el video.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error al capturar el fotograma o video terminado.")
                break

            results = self.model(frame)
            annotated_frame = results[0].plot()

            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            self.update_display(annotated_frame)

            self.root.update_idletasks()
            self.root.update()

        cap.release()
        cv2.destroyAllWindows()

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Imágenes y Videos", "*.jpg;*.jpeg;*.png;*.mp4;*.avi")]
        )

        if not file_path:
            return

        if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            self.process_image(file_path)
        elif file_path.lower().endswith(('.mp4', '.avi')):
            self.process_video(file_path)
        else:
            messagebox.showerror("Error", "Tipo de archivo no soportado.")