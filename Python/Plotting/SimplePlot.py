import numpy as np
import os
from matplotlib import pyplot as plt
import pandas as pd
import csv
import glob
from matplotlib.ticker import MaxNLocator

script_directory = os.path.dirname(
    os.path.abspath(__file__)
)  # Get the directory path of the script
csv_file = "/home/stefanom/Projects/MySmallProgrammingJourney/Python/Plotting/Plotty/ExampleSpectra/SM1.csv"

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

    fig, ax1 = plt.subplots()
    plt.plot(x, y, color="black", linewidth=0.4)
    plt.xlabel("Numero d'onda / $cm^{-1}$")
    plt.ylabel("T / %")
    plt.xlim(4000, 500)  # Set the x-axis limits

    plt.ylim(0, 100)  # Set the x-axis limits

    ax2 = ax1.twinx()
    ax2.set_xticks(ax1.get_xticks())  # Set the same x-axis ticks as the primary axis
    ax2.set_xlabel("")
    ax2.set_ylabel("")
    ax2.set_yticklabels([])  # Remove tick labels from ax2

    ax3 = ax1.twiny()  # Create the tertiary x-axis
    ax3.set_xlabel("")
    ax3.set_ylabel("")
    ax3.set_xticks(ax1.get_xticks())  # Set the same x-axis ticks as the primary axis
    ax3.set_xticklabels([])  # Remove tick labels from ax2
    plt.gca().invert_xaxis()  # Invert the x-axis

    target_x_list_unordered = [3000, 3500, 4000]  # List of target x-values
    target_x_list_ordered = target_x_list_unordered[::-1]
    arrow_counter = 1  # Counter for the progressive numeration

    for target_x in target_x_list_ordered:
        target_y = None

        for i in range(len(x)):
            if x[i] == target_x:
                target_y = y[i]
                break

        if target_y is not None:
            arrow_text = f"{arrow_counter}"
            plt.annotate(
                arrow_text,
                xy=(target_x, target_y - 3),
                xytext=(target_x, target_y - 13),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
                ha="center",
            )
            arrow_counter += 1
        else:
            print("I'm fucked")

    output_filename = os.path.join(
        script_directory, os.path.splitext(os.path.basename(csv_file))[0] + ".svg"
    )
    plt.savefig(output_filename)
    plt.clf()

plt.close()
