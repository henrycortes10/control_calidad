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

Adicional, se aplicaron diversas técnicas de aumento de datos para simular variaciones y condiciones de iluminación que el sistema podría encontrar en un entorno de producción real.

# 5. Entrenamiento del Modelo en Roboflow

# 6. Evaluación y Métricas de Desempeño


# 7. Inferencia en Video

# 8. Demostración Visual

# 9. Consideraciones de Hardware y Emulación 
