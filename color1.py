import cv2

def main():
    # Inicializa la cámara
    camera = cv2.VideoCapture(0)

    # Captura una imagen de la cámara
    ret, frame = camera.read()

    # Convierte la imagen a formato HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crea máscaras de color
    maskRed = cv2.inRange(hsv_frame, (0, 100, 100), (10, 255, 255))
    maskGreen = cv2.inRange(hsv_frame, (50, 100, 100), (70, 255, 255))
    maskBlue = cv2.inRange(hsv_frame, (100, 100, 100), (130, 255, 255))

    # Encuentra los contornos en las máscaras
    (contornosRed, hierarchyRed, _, _) = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (contornosGreen, hierarchyGreen, _, _) = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (contornosBlue, hierarchyBlue, _, _) = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibuja los contornos en la imagen
    for contorno in contornosRed:
        cv2.drawContours(frame, contorno, -1, (0, 0, 255), 2)
    for contorno in contornosGreen:
        cv2.drawContours(frame, contorno, -1, (0, 255, 0), 2)
    for contorno in contornosBlue:
        cv2.drawContours(frame, contorno, -1, (255, 0, 0), 2)

    # Muestra la imagen en la pantalla
    cv2.imshow("Cámara", frame)

    # Espera a que el usuario presione una tecla
    cv2.waitKey(0)

if __name__ == "__main__":
    main()