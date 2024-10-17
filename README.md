# Sistema de Detección de Equipo de Protección Personal (EPP) con YOLO y OpenCV

En entornos laborales donde la seguridad es una prioridad, como la construcción y la industria manufacturera, es esencial garantizar el uso adecuado del equipo de protección personal (PPE) para reducir los riesgos de accidentes. Este proyecto tiene como objetivo desarrollar un sistema automatizado para monitorear el uso correcto de PPE utilizando técnicas de visión por computadora y el modelo YOLO para la detección de objetos.

El sistema permite analizar el uso correcto de EPP en imágenes y videos subidos por el usuario, así como en videos en tiempo real capturados por una cámara. Si se detecta que un trabajador no lleva algún elemento de seguridad obligatorio, como cascos, chalecos, orejeras, lentes de seguridad o botas, se genera evidencia visual del incidente. Esto mejora significativamente el cumplimiento de las normas de seguridad y reduce los riesgos de accidentes laborales.

Este proyecto fue desarrollado en la cátedra de **Soporte a la Gestión de Datos con Programación Visual** de la **UTN Rosario** por Andrea Matteucci, Agostina Chiara y Laura Tulian.

## Objetivo

El objetivo principal es implementar un sistema que analice imágenes y videos subidos, o videos en tiempo real, para detectar si los trabajadores están usando el equipo de protección personal (PPE) requerido, utilizando la biblioteca OpenCV.

## Características principales

- Detección del uso correcto de PPE en imágenes subidas, videos pregrabados, y video en vivo.
- Captura automática de imágenes en situaciones de incumplimiento.
- Entrenamiento del modelo utilizando Grounding DINO y Roboflow para asegurar una alta precisión en la identificación de los elementos de seguridad.

Este proyecto proporciona una solución automatizada para la mejora de la seguridad en el lugar de trabajo, eliminando la necesidad de inspecciones manuales y reduciendo los riesgos asociados a los accidentes laborales.

## Documentación

Para más información, revisar el archivo [Narrativa-TPI-PPEDetection-Grupo8.pdf](https://github.com/lauratulian/PPE-Detection-Python/blob/main/Narrativa-TPI-PPEDetection-Grupo8.pdf).
