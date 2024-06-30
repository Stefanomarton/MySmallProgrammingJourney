import yaml
import sys
import re
from rich.console import Console
from rich.progress import track

console = Console()


def load_replacements(yaml_file):
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)
    return data["replacements"]


def search_replace_rtf(input_file, output_file, replacements):
    # Read the RTF file content
    with open(input_file, "r", encoding="utf-8") as file:
        rtf_content = file.read()

    # Perform the search and replace for each pair in the replacements list
    for item in track(replacements, description="Processing replacements..."):
        search_text = item["search"]
        replace_text = item["replace"]
        if search_text in rtf_content:
            console.print(
                f"Replacing [bold yellow]{search_text}[/bold yellow] with [bold green]{replace_text}[/bold green]"
            )
        rtf_content = rtf_content.replace(search_text, replace_text)

    # Replace two or more consecutive \par with a single \par
    rtf_content = re.sub(r"(\\par\s*){2,}", r"\\par ", rtf_content)

    # Save the modified RTF content
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(rtf_content)
    console.print(
        f"[bold green]Replacements completed and saved to {output_file}[/bold green]"
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        console.print(
            "[bold red]Usage: python script.py input.rtf output.rtf replacements.yaml[/bold red]"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    yaml_file = sys.argv[3]

    console.print(f"[bold blue]Loading replacements from {yaml_file}...[/bold blue]")
    replacements = load_replacements(yaml_file)
    search_replace_rtf(input_file, output_file, replacements)
