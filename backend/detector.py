from ultralytics import YOLO

# Modelo ligero y ultra rápido con 80 clases nativas
model = YOLO("yolov8n.pt")

def detectar_objetos(frame):
    # Inferencia rápida sin textos basura en consola
    resultados = model(frame, verbose=False)
    conteo = 0

    for r in resultados:
        # r.plot() dibuja AUTOMÁTICAMENTE las cajas y nombres de CUALQUIER objeto detectado
        frame = r.plot()

        for box in r.boxes:
            conf = float(box.conf[0])
            
            # 🔥 Regla de negocio de tu spec.md: confianza superior al 50%
            if conf > 0.50:
                # Al eliminar el filtro de nombres, CUALQUIER objeto detectado sumará al conteo
                conteo += 1

    return frame, conteo