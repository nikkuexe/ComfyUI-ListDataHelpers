# __init__.py

from .nodes import ListDifferenceNode

# Register the nodes with ComfyUI
NODE_CLASS_MAPPINGS = {
    "List Difference": ListDifferenceNode,
    # Add more node mappings here as you create them
}
