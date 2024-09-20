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

    RETURN_TYPES = ("STRING", "INT",)
    RETURN_NAMES = ("MergedList", "MergedListCount")
    OUTPUT_IS_LIST = (True, False)
    OUTPUT_NODE = True
    FUNCTION = "execute"
    CATEGORY = "Custom"

    def execute(self, list_a, list_b):
        """
        Takes two lists and returns the difference (elements in list_b that are not in list_a)
        and the total difference (len(list_a) - len(difference_list)).

        Args:
            list_a (str): JSON array or newline-separated list.
            list_b (str): JSON array or newline-separated list.

        Returns:
            tuple: Two elements:
                   - A list of differences (DifferenceList).
                   - The total count of remaining elements in list_a after removing the differences (TotalDifference).
        """
        if not list_a or not list_b:
            # If either input is None or empty, return an empty list and zero
            return ([], 0)

        try:
            # Attempt to parse inputs as JSON arrays
            list_a = json.loads(list_a)
            list_b = json.loads(list_b)
        except json.JSONDecodeError:
            # Fallback to newline-separated parsing if JSON fails
            list_a = list(filter(None, list_a.strip().split('\n')))
            list_b = list(filter(None, list_b.strip().split('\n')))

        # Perform set subtraction: items in list_b that are not in list_a
        list_merged = list(set(list_b) - set(list_a))

        # new list length
        list_merged_count = len(list_merged)

        return (list_merged, list_merged_count)
