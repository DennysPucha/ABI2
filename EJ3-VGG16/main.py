import cv2
import numpy as np

def extraer_clave_binaria(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"No se pudo cargar la imagen: {img_path}")

    orb = cv2.ORB_create(nfeatures=256)
    keypoints, descriptors = orb.detectAndCompute(img, None)

    if descriptors is None:
        raise ValueError(f"No se detectaron descriptores en la imagen: {img_path}")

    # Tomamos los primeros 8 descriptores para limitar el tamaño de la clave
    descriptors = descriptors[:8]

    # Convertimos los descriptores binarios a una cadena de bits
    binary_string = ''.join(format(byte, '08b') for row in descriptors for byte in row)
    return binary_string

def generar_clave(img1_path, img2_path):
    bin1 = extraer_clave_binaria(img1_path)
    bin2 = extraer_clave_binaria(img2_path)

    min_len = min(len(bin1), len(bin2))
    clave = ''.join(str(int(bin1[i]) ^ int(bin2[i])) for i in range(min_len))
    return clave

# Ejemplo de uso:
clave = generar_clave("img1.jpg", "img2.jpg")
print("Clave generada (bits):", clave[:128] + "...")
print("Longitud total:", len(clave), "bits")
