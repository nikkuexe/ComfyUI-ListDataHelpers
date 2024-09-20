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

    def execute(self, list_a_str, list_b_str):
        """
        Executes the node's functionality.

        Args:
            list_a_str (str): The first list as a JSON array or newline-separated string.
            list_b_str (str): The second list as a JSON array or newline-separated string.

        Returns:
            tuple: A single-element tuple containing the JSON-formatted difference list.
        """
        try:
            # Attempt to parse inputs as JSON arrays
            list_a = json.loads(list_a_str)
            list_b = json.loads(list_b_str)
        except json.JSONDecodeError:
            # Fallback to newline-separated parsing if JSON fails
            list_a = list(filter(None, list_a_str.strip().split('\n')))
            list_b = list(filter(None, list_b_str.strip().split('\n')))

        # Compute the difference: elements in list_a not in list_b
        difference = [item for item in list_a if item not in list_b]

        # Convert the difference list back to a JSON-formatted string
        difference_str = json.dumps(difference)
        return (difference_str,)
