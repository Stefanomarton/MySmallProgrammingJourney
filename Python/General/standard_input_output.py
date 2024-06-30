import subprocess

bookmarks = [
    ("work-timesheet", "test"),
    ("personal", "test1"),
]


def test_input_output():
    # Create a list of bookmark names
    names = [bookmark[0] for bookmark in bookmarks]

    # Use dmenu to select a bookmark name
    process = subprocess.Popen(
        ["wofi", "--dmenu"], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    selection, _ = process.communicate(input="\n".join(names).encode("utf-8"))

    # # Decode the selection
    selection = selection.decode("utf-8").strip()

    return selection


if __name__ == "__main__":
    selected_name = test_input_output()
    print(selected_name)
