# write image utils liek convert image  to base64 and convert bse64 to image .. also write image to file and read image from file
import base64
from PIL import Image
from io import BytesIO

def image_to_base64(image: Image.Image) -> str:
    """
    Convert a PIL Image to a base64 encoded string.

    Args:
        image (Image.Image): The image to convert.

    Returns:
        str: Base64 encoded string of the image.
    """
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def base64_to_image(base64_str: str) -> Image.Image:
    """
    Convert a base64 encoded string to a PIL Image.

    Args:
        base64_str (str): The base64 encoded string of the image.

    Returns:
        Image.Image: The decoded PIL Image.
    """
    image_data = base64.b64decode(base64_str)
    return Image.open(BytesIO(image_data))

def save_image_to_file(image: Image.Image, file_path: str) -> None:
    """
    Save a PIL Image to a file.

    Args:
        image (Image.Image): The image to save.
        file_path (str): The path where the image will be saved.
    """
    image.save(file_path)

def read_image_from_file(file_path: str) -> Image.Image:
    """
    Read a PIL Image from a file.

    Args:
        file_path (str): The path of the image file to read.

    Returns:
        Image.Image: The loaded PIL Image.
    """
    return Image.open(file_path)
