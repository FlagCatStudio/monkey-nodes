import torch

import numpy as np

from PIL import Image


def _tensor_check_image(image):
    if image.ndim != 4:
        raise ValueError(
            f"Expected NHWC tensor, but found {image.ndim} dimensions"
        )
    if image.shape[-1] not in (1, 3, 4):
        raise ValueError(
            f"Expected 1, 3 or 4 channels for image, but found {image.shape[-1]} channels"
        )
    return


def tensor_to_pil(image):
    _tensor_check_image(image)
    return Image.fromarray(
        np.clip(255.0 * image.cpu().numpy().squeeze(0), 0, 255).astype(np.uint8)
    )


def pil_to_tensor(image):
    return torch.from_numpy(
        np.array(image).astype(np.float32) / 255.0
    ).unsqueeze(0)
