import cv2 #cv2 es el programa para filtrar colores 
import sys #otra biblioteca para filtrar colores
import numpy as np #numpy es la biblioteca de intervalos para que todos los digitos sean introducidos en HSV (Hue, saturation, value)
#biblioteca de excel para que se junten tanto los datos del drone como los del gps
#y saber en que frame esta cierta caja en relacion a posicion
import xlwt
from imutils.video import VideoStream
import imutils

from matplotlib import pyplot as plt #otra biblioteca similar a numpy

def nothing(x): 
    pass

startvl=int(sys.argv[1]);
startvh=int(sys.argv[2]);
n_frame=0;

#el parrafo anterior define los frames del sistema y que sean procesados de un archivo en la computadora

cap = VideoStream(src=0).start()

while(True):
    frame = cap.read()
    n_frame=n_frame+1;
    blur = cv2.blur(frame,(9,9))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
#video capture sirve para abrir la biblioteca en mi computadora
#en donde esten los videos del drone, en este caso en la carpeta llamada drone, y todo lo siguiente es un while en
#el que el sistema hara varias funciones de filtro de colores.
#La primera es abrir una ventana que se llame frame con el video y que se codifique con BGR que son los valores de
#intervalos que sacamos de cada caja. 
  
    cv2.namedWindow("res",1);
    cv2.namedWindow("mask",1);
    cv2.namedWindow("frame",1);
  
  #Este parrafo abre tres ventanas con nombres res, mask y frame
  
    AZUL_MIN = np.array([100,30,150],np.uint8)
    AZUL_MAX = np.array([119,255,255], np.uint8)
    AMAR_MIN = np.array([18,30,150],np.uint8)
    AMAR_MAX = np.array([34,255,255], np.uint8)
    ROJO_MIN = np.array([0,30,150],np.uint8)
    ROJO_MAX = np.array([11,255,255], np.uint8)
    VERD_MIN = np.array([40,30,150],np.uint8)
    VERD_MAX = np.array([72,255,255], np.uint8)
  
  #aqui defini yo los minimos y maximos de cada color de caja, siendo la unica diferencia el primer
  #valor de cada uno como el low y el high dentro de una misma saturacion (30-255) y value o brillo (150-255), intervalos de HSV
  
    cv2.createTrackbar("track_low","mask",startvl,179,nothing);
    cv2.createTrackbar("track_high","mask",startvh,179,nothing);
    low=cv2.getTrackbarPos("track_low","mask");
    high=cv2.getTrackbarPos("track_high","mask");
    lower_blue = np.array([low,30,150])
    upper_blue = np.array([high,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #print(low);
    #print(high);
    print(n_frame);
    test=mask;

  #Aqui se crea un trackbar para mover la mascara que se le aplica a la imagen, en lower y upper blue se
  #deja el low y el high como variables que el usuario pone en la terminal para hacer el filtro por caja individual,
    #si se quisiera juntar las cuatro se usaria las variables definidas arriba en lugar de solo low y high
  
    kernel = np.ones((31,31),np.uint8);
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,0);
    kernel = np.ones((17,17),np.uint8);
    dilation=cv2.dilate(opening,kernel,iterations=2);
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,2);
    edges = cv2.Canny(mask,100,255)
    im2, contours, hierarchy = cv2.findContours(opening, 1, cv2.CHAIN_APPROX_SIMPLE);
    res = cv2.bitwise_and(frame,frame, mask= dilation)
    #contours=np.zeros(mask.shape,np.uint8);
    areas = [cv2.contourArea(c) for c in contours]
    ar = 0.0
    i = 0
  
    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=False)

    sheet1.write(0, 0, "Frame")
    sheet1.write(0, 1, "Pixel")
  
    list1 = [0]
  
    for a in areas:
        print(a);
        i += 1
        ar=float(a)
        list1.append(ar)
        sheet1.write(i,0,ar)
        book.save("/home/pi/git/drone-dev/xls/trials.xls")
        if (a>10000):
            print("encontre caja");
            break;

  #este proceso es para que se filtre el ruido en la imagen, juntando los pixeles mas proximos y grandes y eliminado los muy pequenos o muy lejanos de la imagen de la caja, con un tamano de pixel de 10000, cuando el valor es mas grande aparece un mensaje de encontre caja y el tamano en pixeles de la caja en ese frame
  
  #cv2.drawContours(contours,fcontours,-1,0,255,1)
  #cv2.drawContours(frame,contours,-1,(0,255,0),3);
  #cv2.imshow("edges",edges);
  #cv2.imshow("contours",opening);
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
  
  #se muestran las tres ventanas al usuario
    key = cv2.waitKey(1) & 0xFF  
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.stop()
