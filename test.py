from modelslab.core.client import Client
from modelslab.schemas.interior import (
    ExteriorSchema,
    ScenarioSchema,
    FloorSchema,
    RoomDecoratorSchema,
    InteriorSchema
)

from modelslab.schemas.realtime import RealtimeText2ImageSchema
from modelslab.schemas.image_editing import BackgroundRemoverSchema

from modelslab.core.apis.interior import Interior
from modelslab.core.apis.realtime import Realtime
from modelslab.core.apis.image_editing import Image_editing
from modelslab.utils.image_utils import *

client = Client(api_key="your api key ")
# schema = RealtimeText2ImageSchema(
#     prompt="A modern living room with a large window and a view of the city skyline.",
#     negative_prompt="A cluttered room with old furniture.",
#     width=800,
#     height=600,
#     num_inference_steps=50,
#     guidance_scale=7.5,
#     seed=42
# )

image_pil = read_image_from_file("7c504529-f038-4011-b344-764e0da1d4f2-0.png")
image = image_to_base64(image_pil)
schema = BackgroundRemoverSchema(  
    image=image,
    base64=True,
)



# schema = InteriorSchema(
#     prompt="A modern living room with a large window and a view of the city skyline.",
#     negative_prompt="A cluttered room with old furniture.",
#     width=800,
#     height=600,
#     num_inference_steps=50,
#     guidance_scale=7.5,
#     seed=42
# )

api = Image_editing(client=client, enterprise=False)

response = api.background_remover(schema=schema)

print(response)

# response = api.interior(schema=schema)

# print(response)


