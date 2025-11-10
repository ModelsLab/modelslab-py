import asyncio
from modelslab_py.core.client import Client
from modelslab_py.core.apis.video import Video
from modelslab_py.schemas.video import Text2Video

client = Client(api_key="your_api_key")
api = Video(client=client)

schema1 = Text2Video(model_id="zeroscope", prompt="a cat", num_frames=30)
schema2 = Text2Video(model_id="zeroscope", prompt="a dog", num_frames=30)

async def main():
    results = await asyncio.gather(
        api.async_text_to_video(schema=schema1),
        api.async_text_to_video(schema=schema2),
    )
    await client.close()
    print(results)

asyncio.run(main())
