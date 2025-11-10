from modelslab_py.core.client import Client
from modelslab_py.core.apis.video import Video
from modelslab_py.schemas.video import Text2Video
from modelslab_py.schemas.interior import (
    ExteriorSchema,
    ScenarioSchema,
    FloorSchema,
    RoomDecoratorSchema,
    InteriorSchema
)
from modelslab_py.schemas.realtime import RealtimeText2ImageSchema
from modelslab_py.schemas.image_editing import BackgroundRemoverSchema
from modelslab_py.core.apis.interior import Interior
from modelslab_py.core.apis.realtime import Realtime
from modelslab_py.core.apis.image_editing import Image_editing
from modelslab_py.utils.image_utils import *

# ===== Sync Example =====
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


# ===== Async Example =====

import asyncio
from modelslab_py.core.client import Client
from modelslab_py.core.apis.video import Video
from modelslab_py.schemas.video import Text2Video

schema1 = Text2Video(
    model_id="wan2.2",
    prompt="a cat walking",
    num_frames=25,
    fps=16
)

schema2 = Text2Video(
    model_id="wan2.2",
    prompt="a dog running",
    num_frames=25,
    fps=16
)

async def main():
    async with Client(api_key="your_api_key") as client:
        api = Video(client=client, enterprise=False)

        results = await asyncio.gather(
            api.async_text_to_video(schema=schema1),
            api.async_text_to_video(schema=schema2),
        )

        print(results)

# Uncomment to run async example
# asyncio.run(main())
