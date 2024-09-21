# __init__.py

from .nodes import *

# Register the nodes with ComfyUI
NODE_CLASS_MAPPINGS = {
    "List Difference": ListDifferenceNode,
    "VHS Output Filter": VHSSaveOutputFilter,
    # Add more node mappings here as you create them
}
