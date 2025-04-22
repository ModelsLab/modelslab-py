from modelslab.core.client import Client
from modelslab.schemas.interior import (
    ExteriorSchema,
    ScenarioSchema,
    FloorSchema,
    RoomDecoratorSchema,
    InteriorSchema
)

from modelslab.core.apis.interior import Interior


client = Client(api_key="your_api_key_here")

schema = InteriorSchema(
    prompt="A modern living room with a large window and a view of the city skyline.",
    negative_prompt="A cluttered room with old furniture.",
    width=800,
    height=600,
    num_inference_steps=50,
    guidance_scale=7.5,
    seed=42
)

api = Interior(client=client, enterprise=False)

response = api.interior(schema=schema)

print(response)


