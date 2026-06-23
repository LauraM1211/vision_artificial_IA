from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
import cv2

from detector import detectar_objetos

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Cámara (más estable en Windows)
camara = cv2.VideoCapture(0)

# variables globales
conteo_actual = 0
frame_count = 0


@app.get("/")
def inicio():
    return {"mensaje": "Sistema funcionando correctamente"}


def generar_frames():
    global conteo_actual, frame_count

    while True:
        ret, frame = camara.read()

        if not ret or frame is None:
            continue

        # 🔥 REDUCIR RESOLUCIÓN (clave para rendimiento)
        frame = cv2.resize(frame, (640, 480))

        frame_count += 1

        # 🔥 YOLO SOLO CADA 2 FRAMES (optimización)
        if frame_count % 2 == 0:
            frame, conteo_actual = detectar_objetos(frame)

        # 🔥 compresión más rápida
        _, buffer = cv2.imencode(
            '.jpg',
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 70]
        )

        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.get("/video")
def video():
    return StreamingResponse(
        generar_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


@app.get("/conteo")
def conteo():
    return JSONResponse({
        "objetos_detectados": conteo_actual
    })