import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv
import glob

csv_files = glob.glob('/home/stefanom/GoogleDrive/Università/Internship/SpettriIR/*.csv')

for csv_file in csv_files:
    x = []
    y = []

    with open(csv_file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=';')
        for row in plots:
            try:
                x.append(float(row[0]))
                y.append(float(row[1]))
            except ValueError:
                continue

    plt.plot(x, y, color='black', linewidth=0.3)
    plt.xlabel("Numero d'onda / $cm^{-1}$")
    plt.ylabel('T / %')
    plt.xlim(500, 4000)  # Set the x-axis limits
    plt.gca().invert_xaxis()
    plt.savefig(csv_file[:-4] + '.svg', format='svg')
    plt.savefig(csv_file[:-4] + '.eps', format='eps')
    plt.clf()

plt.close()
