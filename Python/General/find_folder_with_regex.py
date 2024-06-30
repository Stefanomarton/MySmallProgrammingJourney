import os
import re


def find_mozilla_firefox_folder(base_path):
    # Compile the regex for matching the folder name
    pattern = re.compile(r".*[a-zA-Z0-9].default-release")

    # Walk through the directory tree
    for root, dirs, files in os.walk(base_path):
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            if pattern.match(full_path):
                return full_path
    return None


def create_chrome_folder_and_symlink(mozilla_firefox_folder, target_path):
    chrome_folder = os.path.join(mozilla_firefox_folder, "chrome")
    os.makedirs(chrome_folder, exist_ok=True)
    symlink_path = os.path.join(chrome_folder, "userChrome.css")

    # Resolve the absolute path for the target and the symlink
    target_abs_path = os.path.expanduser(target_path)
    symlink_abs_path = os.path.abspath(symlink_path)

    # Create the symbolic link
    try:
        if os.path.exists(symlink_abs_path):
            os.remove(symlink_abs_path)
        os.symlink(target_abs_path, symlink_abs_path)
        print(f"Symbolic link created: {symlink_abs_path} -> {target_abs_path}")
    except OSError as e:
        print(f"Failed to create symbolic link: {e}")


# Specify the base path to start the search (typically the user's home directory)
base_path = os.path.expanduser("~/.mozilla/firefox/")
target_path = "~/.dotfiles/.config/firefox/userChrome.css"

# Find the folder
mozilla_firefox_folder = find_mozilla_firefox_folder(base_path)

if mozilla_firefox_folder:
    print(f"Found folder: {mozilla_firefox_folder}")
    create_chrome_folder_and_symlink(mozilla_firefox_folder, target_path)
