from ultralytics import YOLO
import cv2

# Modelo YOLO
model = YOLO("yolov8n.pt")

# Traducciones principales
TRADUCCIONES = {
    "person": "Persona",
    "cell phone": "Celular",
    "bottle": "Botella",
    "cup": "Vaso",
    "chair": "Silla",
    "tv": "Televisor",
    "laptop": "Portatil",
    "keyboard": "Teclado",
    "mouse": "Mouse",
    "book": "Libro",
    "clock": "Reloj",
    "car": "Carro",
    "motorcycle": "Moto",
    "bus": "Bus",
    "truck": "Camion",
    "dog": "Perro",
    "cat": "Gato"
}

def detectar_objetos(frame):

    resultados = model(frame, verbose=False)

    conteo_objetos = 0
    conteo_personas = 0

    for r in resultados:

        for box in r.boxes:

            conf = float(box.conf[0])

            if conf > 0.50:

                conteo_objetos += 1

                clase = int(box.cls[0])
                nombre = model.names[clase]

                if clase == 0:
                    conteo_personas += 1

                nombre_es = TRADUCCIONES.get(nombre, nombre)

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Caja
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (255, 255, 255),
                    2
                )

                # Texto
                cv2.putText(
                    frame,
                    f"{nombre_es} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

    return frame, conteo_objetos, conteo_personas