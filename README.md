<p align="center">
  <img src="https://github.com/user-attachments/assets/925d5d81-780a-44f6-81e9-3093cdce7363" alt="new one" />
</p>
<div align="center">
  <a href="https://discord.gg/ujtGyjY2">
    <img src="https://img.shields.io/badge/Discord-Join%20Us-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
  <a href="https://x.com/ModelsLabAI">
    <img src="https://img.shields.io/badge/X-@ModelsLabAI-000000?style=for-the-badge&logo=twitter&logoColor=white" alt="X/Twitter">
  </a>
  <a href="https://github.com/ModelsLab">
    <img src="https://img.shields.io/badge/GitHub-ModelsLab-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://pepy.tech/projects/modelslab-py">
    <img src="https://static.pepy.tech/personalized-badge/modelslab-py?period=total&units=international_system&left_color=black&right_color=green&left_text=downloads" alt="PyPI Downloads">
  </a>
  <a href="https://deepwiki.com/ModelsLab/modelslab-py">
    <img src="https://img.shields.io/badge/DeepWiki-Open%20Wiki-blue?style=for-the-badge&logo=readthedocs&logoColor=white" alt="DeepWiki">
  </a>
</div>

# ModelsLab Python SDK

Official Python SDK for ModelsLab API - Generate AI content including images, videos, audio, 3D models, and more.

## Installation

```bash
pip install modelslab_py
```

For async support:
```bash
pip install 'modelslab_py[async]'
```

## Create a client

```python
from modelslab_py.core.client import Client

client = Client(api_key="your_api_key")
```

## Features

- Image Generation and Editing
- Video Generation
- Audio Processing
- 3D Model Generation
- Interior Design
- Deepfake Operations
- Community Models Integration

## Usage Examples

### Image Editing

```python
from modelslab_py.core.client import Client
from modelslab_py.core.apis.image_editing import Image_editing
from modelslab_py.schemas.image_editing import BackgroundRemoverSchema

client = Client(api_key="your_api_key")
api = Image_editing(client=client, enterprise=False)

schema = BackgroundRemoverSchema(
    image="https://example.com/image.jpg",
    base64=False
)

response = api.background_remover(schema=schema)
print(response)
```

### Video Generation

```python
from modelslab_py.core.apis.video import Video
from modelslab_py.schemas.video import Text2Video

client = Client(api_key="your_api_key")
api = Video(client=client, enterprise=False)

schema = Text2Video(
    model_id="zeroscope",
    prompt="a cat walking in a garden",
    num_frames=30
)

response = api.text_to_video(schema=schema)
print(response)
```

### Interior Design

```python
from modelslab_py.core.apis.interior import Interior
from modelslab_py.schemas.interior import InteriorSchema

client = Client(api_key="your_api_key")
api = Interior(client=client, enterprise=False)

schema = InteriorSchema(
    prompt="modern minimalist bedroom",
    init_image="https://example.com/room.jpg"
)

response = api.interior(schema=schema)
print(response)
```

### Audio Processing

```python
from modelslab_py.core.apis.audio import Audio
from modelslab_py.schemas.audio import Text2Speech

client = Client(api_key="your_api_key")
api = Audio(client=client, enterprise=False)

schema = Text2Speech(
    prompt="Hello, welcome to ModelsLab",
    voice_id="madison",
    language="english"
)

response = api.text_to_speech(schema=schema)
print(response)
```

### 3D Generation

```python
from modelslab_py.core.apis.three_d import Three_D
from modelslab_py.schemas.threed import Text23D

client = Client(api_key="your_api_key")
api = Three_D(client=client, enterprise=False)

schema = Text23D(
    prompt="a wooden chair",
    model_id="meshy-4",
    output_format="obj"
)

response = api.text_to_3d(schema=schema)
print(response)
```

### Community Models

#### Z Image Turbo

```python
from modelslab_py.core.apis.community import Community
from modelslab_py.schemas.community import ZImageTurbo

client = Client(api_key="your_api_key")
api = Community(client=client)

schema = ZImageTurbo(
    prompt="a beautiful sunset over mountains",
    width=1024,
    height=1024,
    samples=1
)

response = api.z_image_turbo(schema=schema)
print(response)
```

#### Flux 2 Dev

```python
from modelslab_py.core.apis.community import Community
from modelslab_py.schemas.community import Flux2Dev

client = Client(api_key="your_api_key")
api = Community(client=client)

schema = Flux2Dev(
    prompt="a futuristic city at night",
    width=1024,
    height=1024,
    samples=1
)

response = api.flux_2_dev(schema=schema)
print(response)
```

#### Text to Image

```python
from modelslab_py.core.apis.community import Community
from modelslab_py.schemas.community import Text2Image

client = Client(api_key="your_api_key")
api = Community(client=client, enterprise=False)

schema = Text2Image(
    prompt="a beautiful landscape",
    model_id="midjourney",
    width=512,
    height=512
)

response = api.text_to_image(schema=schema)
print(response)
```

## Async/Await Support

All API methods have async equivalents. Use them for concurrent requests and better performance.

### Async Example with Concurrent Requests

```python
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

        # Run both requests concurrently
        results = await asyncio.gather(
            api.async_text_to_video(schema=schema1),
            api.async_text_to_video(schema=schema2),
        )

        print(results)

asyncio.run(main())
```

### Async Method Naming Convention

For any synchronous method, prefix with `async_`:
- `text_to_video()` → `async_text_to_video()`
- `text_to_image()` → `async_text_to_image()`
- `background_remover()` → `async_background_remover()`

## Provider-Based API Usage

The SDK includes provider-specific implementations for easy access to various AI models:

### Minimax Provider (Video Generation)

```python
from modelslab_py.core.client import Client
from modelslab_py.providers import MinimaxProvider
from modelslab_py.providers.minimax.schemas import Hailuo23T2VSchema

client = Client(api_key="your_api_key")
minimax = MinimaxProvider(client=client)

schema = Hailuo23T2VSchema(
    prompt="A sunset aerial shot of a lone rider galloping across a snow-covered plain"
)

response = minimax.hailuo_23_t2v(schema=schema)
print(response)
```

### BFL Provider (Image Generation)

```python
from modelslab_py.providers import BFLProvider
from modelslab_py.providers.bfl.schemas import FluxPro11Schema

client = Client(api_key="your_api_key")
bfl = BFLProvider(client=client)

schema = FluxPro11Schema(
    prompt="A futuristic cityscape at sunset with flying cars",
    width=1024,
    height=768
)

response = bfl.flux_pro_11(schema=schema)
print(response)
```

### KlingAI Provider (Video Generation)

```python
from modelslab_py.providers import KlingAIProvider
from modelslab_py.providers.klingai.schemas import KlingV25TurboT2VSchema

client = Client(api_key="your_api_key")
kling = KlingAIProvider(client=client)

schema = KlingV25TurboT2VSchema(
    prompt="Cinematic drone shot of a luxury cruise ship sailing",
    duration="5",
    aspect_ratio="16:9"
)

response = kling.kling_v25_turbo_t2v(schema=schema)
print(response)
```

### Sync Provider (Lip Sync)

```python
from modelslab_py.providers import SyncProvider
from modelslab_py.providers.sync.schemas import Lipsync2Schema

client = Client(api_key="your_api_key")
sync = SyncProvider(client=client)

schema = Lipsync2Schema(
    init_video="https://example.com/video.mp4",
    init_audio="https://example.com/audio.mp3"
)

response = sync.lipsync_2(schema=schema)
print(response)
```

### Available Providers

- **AlibabaProvider**: Wan2.5 video generation models
- **BFLProvider**: Flux Pro image generation models
- **BytePlusProvider**: SeeDream, SeeDance, and Omni Human models
- **ElevenLabsProvider**: Text-to-speech and audio generation
- **GoogleProvider**: Imagen models for image generation
- **InworldProvider**: Text-to-speech with voice cloning
- **KlingAIProvider**: Kling video generation models
- **MinimaxProvider**: Hailuo video generation models
- **OpenAIProvider**: Sora video generation
- **RunwayProvider**: Gen-4 image and video models
- **SonautoProvider**: Music and song generation
- **SyncProvider**: Video lip-sync models

## API Categories

- **Image Editing**: Background removal, super resolution, inpainting, outpainting
- **Video**: Text-to-video, image-to-video, watermark removal
- **Audio**: Text-to-speech, voice conversion, music generation
- **Interior**: Room design, floor planning, object placement
- **3D**: Text-to-3D, image-to-3D model generation
- **Deepfake**: Face swapping, video manipulation
- **Community**: Access to community-trained models

## Documentation

For detailed documentation, visit [docs.modelslab.com](https://docs.modelslab.com/sdk/python)

## Support

- Discord: [Join our community](https://discord.gg/ujtGyjY2)
- Twitter: [@ModelsLabAI](https://x.com/ModelsLabAI)
- GitHub: [ModelsLab](https://github.com/ModelsLab)

## License

See LICENSE file for details.
