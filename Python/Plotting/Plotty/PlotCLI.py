import argparse
import os
import csv
import random
import click
from matplotlib import pyplot as plt


@click.group()
def cli():
    """CLI group."""
    pass


@click.command()
def create_plot(csv_files, output_format, plot_style):
    """Create a plot starting from data file."""
    fig, ax = plt.subplots()  # Create a single figure and axes objects
    colors = ["black", "blue", "red"]

    for index, csv_file in enumerate(csv_files):
        x = []
        y = []

        with open(csv_file, "r") as csvfile:
            plots = csv.reader(csvfile, delimiter=";")
            for row in plots:
                try:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
                except ValueError:
                    continue

        # Set the color black if only 1 file csv is used
        color = "black" if len(csv_files) == 1 else random.choice(colors)
        colors.remove(color)

        # Use pathbase name to remove path and extension of the file
        label = os.path.splitext(os.path.basename(csv_file))[0]

        if plot_style == "IR":
            ax.plot(x, y, color=color, linewidth=0.4, label=label)
            ax.set_xlabel("Numero d'onda / $cm^{-1}$")
            ax.set_ylabel("T / %")
            ax.set_xlim(4000, 500)  # Set the x-axis limits
            ax.set_ylim(0, 100)  # Set the y-axis limits
            ax2 = ax.twinx()
            ax2.set_xticks(
                ax.get_xticks()
            )  # Set the same x-axis ticks as the primary axis
            ax2.set_xlabel("")
            ax2.set_ylabel("")
            ax2.set_yticklabels([])  # Remove tick labels from ax2

            ax3 = ax.twiny()  # Create the tertiary x-axis
            ax3.set_xlabel("")
            ax3.set_ylabel("")
            ax3.set_xticks(
                ax.get_xticks()
            )  # Set the same x-axis ticks as the primary axis
            ax3.set_xticklabels([])  # Remove tick labels from ax2

        elif plot_style == "NMR":
            ax.plot(x, y, color=color, linewidth=0.2, label=label)
            ax.set_xlabel("ppm")
            ax.set_ylabel("A / %")

    ax.legend()  # Add the legend to the axes object

    if len(csv_files) == 1:
        output_filename = os.path.splitext(csv_files[0])[0] + "." + output_format
    else:
        output_filename = "combined_plot." + output_format

    plt.savefig(output_filename, format=output_format)
    plt.clf()
    print(f"Plot saved as {output_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a plot from CSV files")
    parser.add_argument("files", nargs="+", help="Paths to the CSV files")
    parser.add_argument(
        "--format",
        choices=["png", "svg", "pdf", "eps"],
        default="png",
        help="Output format for the plot (default: png)",
    )
    parser.add_argument(
        "--style",
        choices=["IR", "NMR"],
        default="default",
        help="Plot style (default: default)",
    )

    args = parser.parse_args()

    create_plot(args.files, args.format, args.style)
