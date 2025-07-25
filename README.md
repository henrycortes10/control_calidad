# 1. Visión General del Proyecto
Este repositorio documenta un proyecto de grado centrado en el desarrollo de un sistema de control de calidad automatizado para materiales impresos, dirigido a empresas de diseño y marketing. El proyecto aborda la problemática de la inspección manual de defectos (como manchas, fallas y corrimientos), que es propensa a errores e ineficiencias, proponiendo una solución innovadora basada en procesamiento de imágenes e inteligencia artificial. A través de una emulación a nivel de laboratorio, se implementa y valida un módulo de detección de anomalías utilizando el modelo avanzado de visión por computadora, RF-DETR (Base). El objetivo principal es demostrar la viabilidad y la alta precisión de la IA en la identificación de defectos, sentando las bases para una futura integración en sistemas embebidos que optimicen los procesos de producción y aseguren la calidad final del material publicitario.

# 2. Introducción a RF-DETR
El corazón del módulo de inteligencia artificial de este sistema de control de calidad es el modelo RF-DETR (Base). DETR, o "Detection Transformer", representa una arquitectura de vanguardia en la detección de objetos, que se distingue por su enfoque innovador al utilizar transformadores para realizar predicciones directas, eliminando la necesidad de componentes tradicionales como las anclas (anchors) o la supresión no máxima (NMS) en su fase original. RF-DETR es la implementación y optimización de esta arquitectura por parte de Roboflow, diseñada para un entrenamiento y despliegue eficientes en diversas aplicaciones de visión por computadora. Este modelo fue seleccionado para el proyecto debido a su demostrado rendimiento superior en la detección de los defectos específicos (manchas, fallas y corrimientos) en comparación con otras arquitecturas evaluadas, proporcionando la precisión y capacidad de generalización requeridas para la emulación a nivel de laboratorio.


# 3. Dataset
El entrenamiento del modelo RF-DETR se llevó a cabo utilizando un dataset personalizado. Este conjunto de datos incluye imágenes que representar los tres tipos de defectos: manchas (clase ID 0), fallas (clase ID 1) y corrimientos (clase ID 2). 
## Imágenes extraídas (3.278)
*Adjuntar link*
## Imágenes etiquetadas en Roboflow (3.278)


# 4. Pre-procesamiento y Aumento de Datos
Para potencias la robustez y capacidad de generalización del modello, se implementó un proceso estratégico de pre-procesamiento y aumento de datos, gestionado a través de Roboflow. Antes de ser utilizadas para el entrenamiento, todas las imágenes del dataset fueron estandarizadas a una resolución uniforme (640x640 pixeles), optimizando la red neuronal.

![PREPROCESSING](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/PREPROCESSING.png)

Adicional, se aplicaron diversas técnicas de aumento de datos para simular variaciones y condiciones de iluminación que el sistema podría encontrar en un entorno de producción real.

![AUGMENTATIONS](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/AUGMENTATIONS.png)

Luego de aplicar estos procesos, o "filtros", aumentaron los datos a 14.254 imágenes.

# 5. Entrenamiento del Modelo en Roboflow
La fase de entrenamiento del modelo RF-DETR (Base), esencial para su alto rendimiento, se llevó a cabo íntegramente sobre la plataforma de Roboflow. Esta elección fue estratégica y crítica, dada la significativa complejidad computacional del modelo y las limitaciones de recursos (GPU y tiempo de ejecución) encontradas en entornos locales de desarrollo como Google Colab para modelos de esta envergadura. Roboflow proporcionó un entorno optimizado, utilizando hardware potente en la nube (como las GPU NVIDIA A100), lo cual resultó crucial para el entrenamiento eficiente y la convergencia del modelo de deep learning.

El proceso de entrenamiento incluyó los siguientes pasos clave:

-  **Carga y Versión del Dataset:** El dataset personalizado, ya pre-procesado y aumentado, fue subido y versionado en la plataforma Roboflow, asegurando la consistencia de los datos de entrada.
- **Configuración del Modelo:** Se seleccionó el modelo base RF-DETR (Base) y por defecto los hiperparámetros de entrenamiento (ej., número de épocas, tasa de aprendizaje) según las recomendaciones de Roboflow.

![seleccion](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/seleccion.png)

![base](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/base.png)

- **Ejecución y Monitoreo:** El entrenamiento se inició en los servidores de Roboflow. Se realizó un seguimiento continuo de su progreso a través de las herramientas de visualización integradas en la plataforma, las cuales mostraban en tiempo real las curvas de pérdida (loss) y las métricas de precisión media (mAP) en el conjunto de validación.
  
![entrenamiento](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/entrenamiento.jpeg)

Al finalizar este proceso, Roboflow generó los archivos de pesos del modelo (.pt), encapsulando el conocimiento adquirido por la IA para la detección precisa de manchas, fallas y corrimientos.
# 6. Evaluación y Métricas de Desempeño
Las métricas finales de manera destacada:

- **mA@50:** 81.9%
- **Precisión:** 81.5%
- **Recall:** 77.0%

![METRICAS](https://github.com/henrycortes10/control_calidad/blob/main/imagenes/METRICAS.png)

# 7. Inferencia en Video
Una vez entrenado y validado, el modelo RF-DETR (Base) se utiliza para realizar inferencia de detección de objetos en tiempo real a través de video, aprovechando la API de inferencia de Roboflow. Este enfoque es crucial para la emulación a nivel de laboratorio, ya que permite que el procesamiento computacionalmente intensivo de la inteligencia artificial se ejecute en la potente infraestructura en la nube de Roboflow, mientras que el cliente local gestiona únicamente la adquisición de video y la visualización de los resultados.

**Funcionamiento Conceptual:**

- **Captura de Fotogramas:** Un script Python ejecutado en el PC local utiliza la librería OpenCV para capturar continuamente fotogramas desde una cámara web (ej. la cámara digital).

- **Envío a la Nube:** Cada fotograma es enviado, vía conexión a Internet, a la API de inferencia de Roboflow. Para este envío, se utilizan credenciales específicas del proyecto y la versión del modelo entrenado.

- **Procesamiento de IA:** En los servidores de Roboflow, el modelo RF-DETR procesa el fotograma recibido, aplicando sus capacidades de detección para generar predicciones (coordenadas de las cajas delimitadoras, etiquetas de clase y puntuaciones de confianza para cada defecto identificado).

- **Recepción y Visualización:** Las predicciones son devueltas al cliente local, donde el script Python las interpreta y las superpone gráficamente sobre el fotograma original, mostrando las detecciones en vivo en la pantalla del PC.
- 
# 8. Demostración Visual

# 9. Consideraciones de Hardware y Emulación 
