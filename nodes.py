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
                "input_data": ("LIST", {"forceInput": True}),  # Expecting list of tuples (True, [file_paths])
            }
        }

    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("FilteredVideoFiles",)
    FUNCTION = "filter_video_files"
    CATEGORY = "VHS"

    def filter_video_files(self, input_data):
        # List of common video file extensions
        video_extensions = (".mp4", ".webm", ".mkv", ".avi")

        # Initialize an empty list to collect video files
        video_files = []

        # Iterate over input data, which should be tuples (bool, [file_paths])
        for is_valid, file_paths in input_data:
            if is_valid and isinstance(file_paths, list):  # Check if the tuple is valid and has a list of paths
                # Filter only video files based on the extensions
                video_files.extend([file for file in file_paths if file.endswith(video_extensions)])

        # Return the filtered video files
        return (video_files,)


N_CLASS_MAPPINGS = {
    "VHS_VideoOutputFilter": VHSSaveOutputFilter,
}

N_DISPLAY_NAME_MAPPINGS = {
    "VHS_VideoOutputFilter": "VHS Video Output Filter",
}
