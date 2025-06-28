# ABI_PRACTICO: Algoritmos de Cifrado Simétricos – Vulnerabilidades y Mitigaciones

Este repositorio contiene implementaciones prácticas de distintos mecanismos criptográficos que abordan vulnerabilidades comunes en algoritmos de cifrado simétrico y proponen soluciones modernas basadas en modelos híbridos, cifrado multinivel, generación de claves robustas y hashing resistente a ataques de fuerza bruta.

## 📚 Fundamento Teórico

El proyecto está basado en el análisis de vulnerabilidades en algoritmos de cifrado simétrico, especialmente en aquellos utilizados en entornos de bajo consumo como GPRS (GEA-1, GEA-2, GEA-2a), y en la mitigación mediante técnicas como:

- **Ataques de canal lateral (SCA)**
- **Cifrado multinivel (RCTS)**
- **Generación de claves simétricas usando redes neuronales convolucionales (VGG16)**
- **Cifrado ligero de imágenes con ChaCha e hipercaos**
- **Hashing multifactorial (MFCHF)**

## 📁 Estructura del Proyecto

Cada carpeta contiene una implementación específica o experimento práctico asociado a una técnica de mitigación:

### 🔐 `EJ1-GPRS/`
**GEA-1/GEA-2 y Canal Lateral (SCA):**
- Modela ataques de canal lateral sobre algoritmos GEA.
- Simula extracción de claves a través de correlación basada en modelos de fuga (peso/diferencia de Hamming).
- Incluye ejemplos básicos en Python y el uso de Z3 para resolución SMT.

### 🔁 `EJ2-CRYPMULTINIVEL/`
**Cifrado Multinivel (RCTS):**
- Implementa un esquema secuencial: `RC5 -> Twofish -> Serpent modificado`.
- Evalúa estadísticas como entropía, histograma y autocorrelación.
- Demuestra cómo la combinación de múltiples algoritmos incrementa exponencialmente el espacio de claves.

### 🧠 `EJ3-VGG16/`
**Generación de claves con VGG16:**
- Utiliza una red neuronal VGG16 para extraer características de dos imágenes.
- Combina las características mediante XOR para formar claves altamente aleatorias y extensas.
- Valida la aleatoriedad con pruebas NIST SP 800-22.

### 🔐 `EJ4-MFCHF/`
**MFCHF – Multifactor Credential Hashing Function:**
- Integra OTPs (como HOTP, TOTP) en el proceso de hashing de contraseñas.
- Implementa un hash resistente a ataques de fuerza bruta asistida, incluso post-filtración.
- Mantiene latencias bajas para usuarios legítimos mientras eleva la entropía para atacantes.

Instalación rápida:

```bash
pip install -r requirements.txt
