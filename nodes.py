# nodes.py

import json

class ListDifferenceNode:
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

    def execute(self, list_a, list_b):
        """
        Takes two lists and returns the difference (elements in list_b that are not in list_a).

        Args:
            list_a (str): JSON array or newline-separated list.
            list_b (str): JSON array or newline-separated list.

        Returns:
            tuple: A single-element tuple containing the JSON-formatted difference list.
        """
        if not list_a or not list_b:
            # If either input is None or empty, return an empty JSON array
            return (json.dumps([]),)

        try:
            # Attempt to parse inputs as JSON arrays
            list_a = json.loads(list_a)
            list_b = json.loads(list_b)
        except json.JSONDecodeError:
            # Fallback to newline-separated parsing if JSON fails
            list_a = list(filter(None, list_a.strip().split('\n')))
            list_b = list(filter(None, list_b.strip().split('\n')))

        # Perform set subtraction: items in list_b that are not in list_a
        difference = list(set(list_b) - set(list_a))

        # Convert the difference list back to a JSON-formatted string
        difference_str = json.dumps(difference)
        return (difference_str,)
