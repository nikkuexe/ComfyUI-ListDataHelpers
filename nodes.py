# nodes.py

import json

class ListDifferenceNode:
    """
    A ComfyUI node that computes the difference between two lists.
    It outputs elements that are present in List A but not in List B.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list_a": ("STRING", {"multiline": True}),
                "list_b": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Custom"

    # Update the method signature to accept keyword arguments
    def execute(self, list_a, list_b):
        """
        Executes the node's functionality.

        Args:
            list_a (str): JSON array or newline-separated list.
            list_b (str): JSON array or newline-separated list.

        Returns:
            tuple: A single-element tuple containing the JSON-formatted difference list.
        """
        try:
            # Attempt to parse inputs as JSON arrays
            list_a = json.loads(list_a)
            list_b = json.loads(list_b)
        except json.JSONDecodeError:
            # Fallback to newline-separated parsing if JSON fails
            list_a = list(filter(None, list_a.strip().split('\n')))
            list_b = list(filter(None, list_b.strip().split('\n')))

        # Compute the
