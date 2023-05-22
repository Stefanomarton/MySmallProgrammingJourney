import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv
import glob
from matplotlib.ticker import MaxNLocator

csv_files = glob.glob(
    "/home/stefanom/GoogleDrive/Università/Internship/SpettriIR/*.csv"
)

for csv_file in csv_files:
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

    plt.savefig(csv_file[:-4] + ".svg", format="svg")
    plt.savefig(csv_file[:-4] + ".eps", format="eps")
    plt.clf()

plt.close()
