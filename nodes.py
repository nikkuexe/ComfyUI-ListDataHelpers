import json
import ast
import os

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
        Takes two lists as strings, converts them into sets, performs a set difference operation,
        and returns the items in list_a that are not in list_b.

        Args:
            list_a (str): Multiline string (or JSON array) representing the first list.
            list_b (str): Multiline string (or JSON array) representing the second list.

        Returns:
            tuple: Two elements:
                   - A list of items in list_a that are not in list_b (MergedList).
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

        # Convert both lists to sets
        set_a = set(list_a)
        set_b = set(list_b)

        # Perform set difference: items in set_a that are not in set_b
        set_diff = set_a - set_b

        # Convert the set back to a list to return
        list_diff = list(set_diff)

        # Get the count of elements in the difference
        list_diff_count = len(list_diff)

        return (list_diff, list_diff_count)

class VHSSaveOutputFilter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_data": ("STRING", {"forceInput": True}),  # Expecting string that represents a list of tuples
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("FilteredVideoFile",)
    FUNCTION = "execute"
    CATEGORY = "nikku"

    def execute(self, input_data):
        # List of common video file extensions
        video_extensions = (".mp4", ".webm", ".mkv", ".avi")

        # Base path to remove from the file path
        base_path = "/workspace/ComfyUI/output/"

        # Safely evaluate the string input as a Python literal (list of tuples)
        try:
            parsed_data = ast.literal_eval(input_data)  # Convert the string into a Python object (list/tuple)
        except (SyntaxError, ValueError):
            return ("",)  # If there's an error, return an empty string

        # Iterate over parsed data, which should be tuples (bool, [file_paths])
        for is_valid, file_paths in parsed_data:
            if is_valid and isinstance(file_paths, list):  # Check if the tuple is valid and has a list of paths
                for file in file_paths:
                    # Check if the file is a video file by its extension
                    if file.endswith(video_extensions):
                        # Remove the base ComfyUI path
                        relative_path = file.replace(base_path, "")

                        # Remove the file extension
                        filename_without_extension = os.path.splitext(relative_path)[0]

                        # Return the first matching video file (subfolder path + filename without extension)
                        return (filename_without_extension,)

        # If no video file is found, return an empty string
        return ("",)


N_CLASS_MAPPINGS = {
    "VHS_VideoOutputFilter": VHSSaveOutputFilter,
}

N_DISPLAY_NAME_MAPPINGS = {
    "VHS_VideoOutputFilter": "VHS Video Output Filter",
}
