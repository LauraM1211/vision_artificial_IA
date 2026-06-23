from ultralytics import YOLO

# modelo ligero (rápido)
model = YOLO("yolov8n.pt")


def detectar_objetos(frame):
    # 🔥 inferencia rápida
    resultados = model(frame, verbose=False)

    conteo = 0

    for r in resultados:
        # dibujar cajas
        frame = r.plot()

        for box in r.boxes:
            cls = int(box.cls[0])
            nombre = model.names[cls]

            # 🔥 filtrar objetos importantes
            if nombre in ["person", "cell phone", "bottle", "cup"]:
                conteo += 1

    return frame, conteo