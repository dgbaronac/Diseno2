import cv2
import numpy as np

def dibujar(mask, color):
    (contornos, _) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 10000:
            M = cv2.moments(c)
            if M["m00"] == 0:
                M["m00"] = 1
            x = int(M["m10"] / M["m00"])
            y = int(M['m01'] / M['m00'])
            nuevoContorno = cv2.convexHull(c)
            cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
            cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
            if color == (255, 0, 0):
                print("azul")
            elif color == (0, 128, 255):
                print("naranja")
            elif color == (0, 255, 255):
                print("amarillo")
            elif color == (0, 0, 255):
                print("rojo")
            elif color == (128, 0, 255):
                print('morado')
            elif color == (0, 255, 0):
                print("verde")
SaturLow = 100
ValueLow = 100

redBajo1 = np.array([0,SaturLow,ValueLow],np.uint8)
redAlto1 = np.array([11,255,255],np.uint8)

orangebajo = np.array([12,SaturLow,ValueLow],np.uint8)
orangealto = np.array([23,255,255],np.uint8)

amarilloBajo = np.array([24,SaturLow,ValueLow],np.uint8)
amarilloAlto = np.array([32,255,255],np.uint8)

greenBajo = np.array([33,SaturLow,ValueLow],np.uint8)
greenAlto = np.array([80,255,255],np.uint8)

azulBajo = np.array([85,SaturLow,ValueLow],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

moradobajo = np.array([126,SaturLow,ValueLow],np.uint8)
moradoAlto = np.array([163,255,255],np.uint8)


redBajo2 = np.array([170,SaturLow,ValueLow],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
# Cargar la imagen preguardada
image_path = 'rojo.jpg'  # Reemplaza 'ruta_de_tu_imagen.jpg' con la ruta correcta de tu imagen
frame = cv2.imread(image_path)

frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
maskRed = cv2.add(maskRed1, maskRed2)
maskOrange = cv2.inRange(frameHSV, orangebajo, orangealto)
maskAmarillo = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
maskGreen = cv2.inRange(frameHSV, greenBajo, greenAlto)
maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
maskMorado = cv2.inRange(frameHSV, moradobajo, moradoAlto)

dibujar(maskRed, (0, 0, 255))
dibujar(maskOrange, (0, 128, 255))
dibujar(maskAmarillo, (0, 255, 255))
dibujar(maskGreen, (0, 255, 0))
dibujar(maskAzul, (255, 0, 0))
dibujar(maskMorado, (128, 0, 255))

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()