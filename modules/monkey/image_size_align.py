from PIL import Image, ImageOps

from .helpers import tensor_to_pil, pil_to_tensor


def _compute_padding(size, modulus):
    return (modulus - (size % modulus)) % modulus


class ImageSizeAlign:
    """
    A Node adding padding to an image so that it's dimensions align on a
    certain multiples of pixels

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    DEPRECATED (`bool`):
        Indicates whether the node is deprecated. Deprecated nodes are hidden by default in the UI, but remain
        functional in existing workflows that use them.
    EXPERIMENTAL (`bool`):
        Indicates whether the node is experimental. Experimental nodes are marked as such in the UI and may be subject to
        significant changes or removal in future versions. Use with caution in production workflows.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
        Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
        The type can be a list for selection.

        Returns: `dict`:
            - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
            - Value input_fields (`dict`): Contains input fields config:
                * Key field_name (`string`): Name of a entry-point method's argument
                * Value field_config (`tuple`):
                    + First value is a string indicate the type of field or a list for selection.
                    + Second value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "modulus": (
                    "INT",
                    {
                        "default": 8,
                        "min": 0,  # Minimum value
                        "max": 4096,  # Maximum value
                        "step": 1,  # Slider's step
                        "display": "number",  # Cosmetic only: display as "number" or "slider"
                        "lazy": False,  # Will only be evaluated if check_lazy_status requires it
                    },
                ),
                "padding_color": (
                    "STRING",
                    {
                        "multiline": False,  # True if you want the field to look like the one on the ClipTextEncode node
                        "default": "#ffffff",
                        "lazy": False,
                    },
                ),
            },
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT", "INT", "INT", "INT", "INT")
    RETURN_NAMES = (
        "padded_image",
        "original_width",
        "original_height",
        "padded_width",
        "padded_height",
        "padding_width",
        "padding_height",
    )
    CATEGORY = "image/transform"

    FUNCTION = "perform"

    def perform(self, *, image, modulus, padding_color):
        pil_image = tensor_to_pil(image)
        width, height = pil_image.size

        padding_width = _compute_padding(width, modulus)
        padding_height = _compute_padding(height, modulus)
        padded_width = width + padding_width
        padded_height = height + padding_height

        padded_image = ImageOps.expand(
            image=pil_image,
            border=(padding_width, padding_height, 0, 0),
            fill=padding_color,
        )

        return (
            pil_to_tensor(padded_image),
            width,
            height,
            padded_width,
            padded_height,
            padding_width,
            padding_height,
        )
