import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cam.read()

    if not ret:
        print("No se puede abrir la cámara")
        break

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) == 27:  # ESC para salir
        break

cam.release()
cv2.destroyAllWindows()