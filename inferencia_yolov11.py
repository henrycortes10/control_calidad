

# Import the InferencePipeline object
from inference import InferencePipeline
# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="impresionesv2/25", # Roboflow model to use
     api_key = "nt8nkIkaCL3LxM376V9S", #agrega tu api key
    video_reference=0, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream  url
    on_prediction=render_boxes, # Function to run after each prediction
)
pipeline.start()
pipeline.join()