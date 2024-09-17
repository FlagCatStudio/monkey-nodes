"""
@author: Flagcat Studio SAS
@title: Monkey Nodes
@nickname: Monkey Nodes
@description: Nothing worthy so far. Maybe later
"""

import os, path

modules_path = os.path.join(os.path.dirname(__file__), "modules")
sys.path.append(modules_path)

import monkey

print(f"### Loading: Monkey Nodes ({monkey.VERSION})")

g
NODE_CLASS_MAPPINGS = {
    "ImageSizeAlign": monkey.ImageSizeAlign,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSizeAlign": "Image Size Align (Monkey)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
