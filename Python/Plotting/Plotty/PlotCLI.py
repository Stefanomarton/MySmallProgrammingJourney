import click
import os
import csv
import random
from matplotlib import pyplot as plt
from rich.console import Console

console = Console()


class CSVPlotter:
    """Plot from csv file."""

    def __init__(self, csv_files, output_format, plot_style, combined):
        """Initialize all the variables."""
        self.csv_files = csv_files
        self.output_format = output_format
        self.plot_style = plot_style
        self.combined = combined
        self.colors = [
            "blue",
            "red",
            "green",
            "orange",
            "purple",
            "black",
        ]  # Add more colors if needed

    def process_csv_file(self, csv_file):
        """Create x and y list for each file."""
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

        return x, y

    def create_plot(self):
        """Create plot from x and y list."""
        if self.combined:
            fig, ax = plt.subplots()  # Create a single figure and axes objects
        else:
            fig, ax = None, None

        for csv_file in self.csv_files:
            x, y = self.process_csv_file(csv_file)

            color = "black" if not self.combined else random.choice(self.colors)
            label = os.path.splitext(os.path.basename(csv_file))[0]

            if self.plot_style == "IR":
                if self.combined:
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

                else:
                    fig, ax = plt.subplots()
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
                    ax.legend()  # Add the legend to the axes object
                    output_filename = (
                        os.path.splitext(csv_file)[0] + "." + self.output_format
                    )
                    plt.savefig(output_filename, format=self.output_format)
                    plt.clf()
                    click.echo(f"Plot saved as {output_filename}")

            elif self.plot_style == "UV":
                if self.combined:
                    ax.plot(x, y, color=color, linewidth=0.2, label=label)
                else:
                    fig, ax = plt.subplots()
                    ax.plot(x, y, color=color, linewidth=0.2, label=label)
                    ax.set_xlabel("$\lambda$ / nm ")
                    ax.set_ylabel("A / a.u.")
                    ax.legend()  # Add the legend to the axes object
                    output_filename = (
                        os.path.splitext(csv_file)[0] + "." + self.output_format
                    )
                    plt.savefig(output_filename, format=self.output_format)
                    plt.clf()
                    click.echo(f"Plot saved as {output_filename}")

        if self.combined:
            combined_filename = "_".join(
                [os.path.splitext(os.path.basename(f))[0] for f in self.csv_files]
            )
            output_filename = f"{combined_filename}.{self.output_format}"
            ax.legend()  # Add the legend to the axes object
            plt.savefig(output_filename, format=self.output_format)
            plt.clf()
            click.echo(f"Combined plot saved as {output_filename}")


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "--output-format",
    type=click.Choice(["png", "svg", "pdf", "eps"]),
    default="png",
    help="Output format for the plot",
)
@click.option(
    "--style",
    type=click.Choice(["IR", "UV"]),
    default="default",
    help="Plot style",
)
@click.option(
    "--combined",
    is_flag=True,
    default=False,
    help="Create a combined plot with multiple CSV files",
)
def export_plot(files, output_format, style, combined):
    """Call an instance to export the plot."""
    if not files:
        click.echo("Please provide one or more CSV files.")
        return

    plotter = CSVPlotter(files, output_format, style, combined)
    plotter.create_plot()

    # Print a success message
    console.print(":tada: [bold green]Plots created successfully![/bold green] :tada:")


if __name__ == "__main__":
    export_plot()
