# Import the InferencePipeline object
from inference import InferencePipeline
# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="impresionesv2/21", # Usa el nombre correcto del modelo y versión
    api_key="APIKEY",         # <-- Agrega tu API Key aquí
    video_reference=0,            # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=render_boxes,   # Function to run after each prediction
)
print("Pipeline creado, iniciando...")
pipeline.start()
pipeline.join()