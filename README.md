# 1. Visión General del Proyecto
Este repositorio documenta un proyecto de grado centrado en el desarrollo de un sistema de control de calidad automatizado para materiales impresos, dirigido a empresas de diseño y marketing. El proyecto aborda la problemática de la inspección manual de defectos (como manchas, fallas y corrimientos), que es propensa a errores e ineficiencias, proponiendo una solución innovadora basada en procesamiento de imágenes e inteligencia artificial. A través de una emulación a nivel de laboratorio, se implementa y valida un módulo de detección de anomalías utilizando el modelo avanzado de visión por computadora, YOLOv11 (Large). El objetivo principal es demostrar la viabilidad y la alta precisión de la IA en la identificación de defectos, sentando las bases para una futura integración en sistemas embebidos que optimicen los procesos de producción y aseguren la calidad final del material publicitario.

# 2. Introducción a YOLOv11
YOLOv11 es la última generación de modelos de detección de objetos en tiempo real de Ultralytics, destacándose por ser líder en precisión, velocidad y eficiencia. Construido sobre avances previos, optimiza su arquitectura para una extracción de características superior, logrando una mayor precisión con menos parámetros y FLOPs que sus predecesores. Es versátil para múltiples tareas de visión por computadora y ofrece inferencia más rápida en CPU y GPU, lo que lo convierte en la opción recomendada para proyectos que buscan el mejor rendimiento.


# 3. Dataset (Conjunto de datos)
El entrenamiento del modelo YOLOv11 se llevó a cabo utilizando un dataset personalizado. Este conjunto de datos incluye imágenes que representar los tres tipos de defectos: manchas (clase ID 0), fallas (clase ID 1) y corrimientos (clase ID 2). 
## Imágenes extraídas (3.278)
(https://drive.google.com/drive/folders/1wbYGIQqdGHMmi01kj1-fVAYg0xkz7vcI?usp=sharing)
## Imágenes etiquetadas en Roboflow (3.278)


# 4. Pre-procesamiento y Aumento de Datos
Para potencias la robustez y capacidad de generalización del modello, se implementó un proceso estratégico de pre-procesamiento y aumento de datos, gestionado a través de Roboflow. Antes de ser utilizadas para el entrenamiento, todas las imágenes del dataset fueron estandarizadas a una resolución uniforme (640x640 pixeles), optimizando la red neuronal.

![PREPROCESSING](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/PREPROCESSING.png)

Adicional, se aplicaron diversas técnicas de aumento de datos para simular variaciones y condiciones de iluminación que el sistema podría encontrar en un entorno de producción real.

![AUGMENTATIONS](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/AUGMENTATIONS.png)

Luego de aplicar estos procesos, o "filtros", aumentaron los datos a 14.254 imágenes.

# 5. Entrenamiento del Modelo en Roboflow
La fase de entrenamiento del modelo YOLOv11 (Large), esencial para su alto rendimiento, se llevó a cabo íntegramente sobre la plataforma de Roboflow. Esta elección fue estratégica y crítica, dada la significativa complejidad computacional del modelo y las limitaciones de recursos (GPU y tiempo de ejecución) encontradas en entornos locales de desarrollo como Google Colab para modelos de esta envergadura. Roboflow proporcionó un entorno optimizado, utilizando hardware potente en la nube (como las GPU NVIDIA A100), lo cual resultó crucial para el entrenamiento eficiente y la convergencia del modelo de deep learning.

El proceso de entrenamiento incluyó los siguientes pasos clave:

- **Carga y Versión del Dataset:** El dataset personalizado, ya pre-procesado y aumentado, fue subido y versionado en la plataforma Roboflow, asegurando la consistencia de los datos de entrada.
- **Configuración del Modelo:** Se seleccionó el modelo base RF-DETR (Base) y por defecto los hiperparámetros de entrenamiento (ej., número de épocas, tasa de aprendizaje) según las recomendaciones de Roboflow.

![seleccion](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/seleccion.png)

![base](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/base.png)

- **Ejecución y Monitoreo:** El entrenamiento se inició en los servidores de Roboflow. Se realizó un seguimiento continuo de su progreso a través de las herramientas de visualización integradas en la plataforma, las cuales mostraban en tiempo real las curvas de pérdida (loss) y las métricas de precisión media (mAP) en el conjunto de validación.
  
![entrenamiento](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/entrenamiento.jpeg)

Al finalizar este proceso, Roboflow generó los archivos de pesos del modelo (.pt), encapsulando el conocimiento adquirido por la IA para la detección precisa de manchas, fallas y corrimientos.
# 6. Evaluación y Métricas de Desempeño
Las métricas finales de manera destacada:

- **mA@50:** 83.4%
- **Precisión:** 82.1%
- **Recall:** 74.6%

![METRICAS](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/METRICAS.png)

# 7. Inferencia en Video
Una vez entrenado y validado, el modelo YOLOv11 (Large) se utiliza para realizar inferencia de detección de objetos en tiempo real a través de video, aprovechando la API de inferencia de Roboflow. Este enfoque es crucial para la emulación a nivel de laboratorio, ya que permite que el procesamiento computacionalmente intensivo de la inteligencia artificial se ejecute en la potente infraestructura en la nube de Roboflow, mientras que el cliente local gestiona únicamente la adquisición de video y la visualización de los resultados.

**Funcionamiento Conceptual:**

- **Captura de Fotogramas:** Un script Python ejecutado en la Raspberry Pi 4 utiliza la librería OpenCV para capturar continuamente fotogramas desde una cámara web (ej. la cámara digital).

![PYTHON-RFDETR](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/PYTHON-RFDETR_2.png)

- **Envío a la Nube:** Cada fotograma es enviado, vía conexión a Internet, a la API de inferencia de Roboflow. Para este envío, se utilizan credenciales específicas del proyecto y la versión del modelo entrenado.

- **Procesamiento de IA:** En los servidores de Roboflow, el modelo RF-DETR procesa el fotograma recibido, aplicando sus capacidades de detección para generar predicciones (coordenadas de las cajas delimitadoras, etiquetas de clase y puntuaciones de confianza para cada defecto identificado).

- **Recepción y Visualización:** Las predicciones son devueltas al cliente local, donde el script Python las interpreta y las superpone gráficamente sobre el fotograma original, mostrando las detecciones en vivo en la pantalla del PC.

Librerías necesarias para el correcto funcionamiento del código en Python:

- opencv-python (la versión del opencv debe coincidir con la versión del Python)
- numpy
- roboflow
- inference

# 8. Demostración Visual

A continuación, algunas imágenes con resultados.

![corrimientos](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/CORRIMIENTOS_(TEST%20SET).png)

![fallas](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/FALLAS_(TEST%20SET).png)

![manchas](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/MANCHAS_(TEST%20SET).png)

![manchas2](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/MANCHAS_2(TEST%20SET).png)

![video](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/video4.gif)

