from PIL import Image
from modules.gemini_utils import model

def extract_text_from_image(image_path):

    image = Image.open(image_path)

    prompt = """
    Extract all handwritten text from this image.

    Return only the extracted text.

    Preserve paragraphs.
    """

    response = model.generate_content(
        [prompt, image]
    )

    return response.text