import os
import click
import pyfzf
import subprocess
import shutil


@click.group()
def cli():
    pass


@cli.command()
@click.option("--directory", "-d", default="/dev", help="Directory to search for files")
@click.option(
    "--usb-folder", "-u", default="~/USB", help="USB folder to mount the file"
)
@click.option("--open-file", "-o", is_flag=True, help="Open the file after mounting")
def mount(directory, usb_folder, open_file):
    """Mount a selected file into the USB folder."""
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Create a Pyfzf instance
    fzf = pyfzf.FzfPrompt()

    # Prompt the user to select a file
    selected_files = fzf.prompt(files)

    # Process the selected file
    if selected_files:
        for selected_file in selected_files:
            file_path = os.path.join(directory, selected_file)
            usb_folder = os.path.expanduser(usb_folder)

        # Create the USB folder if it doesn't exist
        if not os.path.exists(usb_folder):
            os.makedirs(usb_folder)

        file_name = os.path.splitext(selected_file)[0]
        mount_folder = os.path.join(usb_folder, file_name)
        os.makedirs(mount_folder, exist_ok=True)

        # Mount the file into the USB folder
        mount_cmd = ["sudo", "mount", file_path, mount_folder]
        subprocess.run(mount_cmd)

        click.echo("File mounted successfully.")
    else:
        click.echo("No file selected.")

    # Open mounted folder if the selected file are less then one
    if len(selected_files) == 1:
        open_cmd = [
            "ranger",
            mount_folder,
        ]  # Adjust this command based on your system
        subprocess.run(open_cmd)


@cli.command()
@click.option(
    "--usb-folder", "-u", default="~/USB", help="USB folder to unmount the file"
)
def unmount(usb_folder):
    """Unmount a selected file in the USB folder."""
    # Create a Pyfzf instance
    fzf = pyfzf.FzfPrompt()

    """Unmount the previously mounted file"""
    usb_folder = os.path.expanduser(usb_folder)

    mounted_files = os.listdir(usb_folder)

    to_unmount_files = fzf.prompt(mounted_files)

    if to_unmount_files:
        for to_unmount_file in to_unmount_files:
            to_unmount_file_path = os.path.join(usb_folder, to_unmount_file)

            # Unmount the USB folder
            unmount_cmd = ["sudo", "umount", to_unmount_file_path]
            subprocess.run(unmount_cmd)
            shutil.rmtree(to_unmount_file_path)

        click.echo("File unmounted successfully.")
    else:
        click.echo("No file selected")

    still_mounted_files = os.listdir(usb_folder)
    if len(still_mounted_files) == 0:
        shutil.rmtree(usb_folder)
    else:
        pass


@cli.command()
@click.option(
    "--usb-folder", "-u", default="~/USB", help="USB folder to unmount the file"
)
def open(usb_folder):
    """Open a selected file into the USB folder."""
    # Needed to locate ~/
    usb_folder = os.path.expanduser(usb_folder)
    if os.path.exists(usb_folder):
        # Get the list of files in the USB folder
        files = os.listdir(usb_folder)
        # Create a Pyfzf instance
        fzf = pyfzf.FzfPrompt()
        # Prompt the user to select a file
        selected_files = fzf.prompt(files)
        # Open mounted folder if the selected file are less then one
        if len(selected_files) == 1:
            selected_file = selected_files[0]
            selected_file_path = os.path.join(usb_folder, selected_file)
            open_cmd = [
                "ranger",
                selected_file_path,
            ]  # Adjust this command based on your system
            subprocess.run(open_cmd)
        else:
            print("Multiple files has been selected")
    else:
        print("No files mounted")


if __name__ == "__main__":
    cli()
