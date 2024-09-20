import json

class ListDifferenceNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list_a": ("STRING", {"multiline": True, "forceInput": True}),
                "list_b": ("STRING", {"multiline": True, "forceInput": True})
            }
        }

    RETURN_TYPES = ("STRING", "INT",)
    RETURN_NAMES = ("MergedList", "MergedListCount")
    OUTPUT_IS_LIST = (True, False)
    OUTPUT_NODE = True
    FUNCTION = "execute"
    CATEGORY = "nikku"

    def execute(self, list_a, list_b):
        """
        Takes two lists as strings, converts them into lists, performs the set difference operation,
        and returns the difference as a list and the count of elements.

        Args:
            list_a (str): Multiline string (or JSON array) representing the first list.
            list_b (str): Multiline string (or JSON array) representing the second list.

        Returns:
            tuple: Two elements:
                   - A list of the difference (MergedList).
                   - The total count of elements in the difference (MergedListCount).
        """
        if not list_a or not list_b:
            return ([], 0)

        try:
            list_a = json.loads(list_a)
            list_b = json.loads(list_b)
        except json.JSONDecodeError:
            list_a = list_a.strip().splitlines()
            list_b = list_b.strip().splitlines()

        # Remove any empty strings from the lists
        list_a = [item for item in list_a if item.strip()]
        list_b = [item for item in list_b if item.strip()]

        # Perform set subtraction
        list_diff = list(set(list_b) - set(list_a))

        # Get the count of elements in the difference
        list_diff_count = len(list_diff)

        return (list_diff, list_diff_count)
