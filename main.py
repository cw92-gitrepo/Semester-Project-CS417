"""
This is the main file for the CPU Temperatures Project. 
Reads a file name from standard input, parses the temperature readings in that
file into a Dataset, and writes piecewise linear interpolation results to one
.txt file per core. The paths of those files are stored in `output_files`.
"""


import parse_temps
from temps_data import Dataset 
import piecewise_linear_interpolation


"""
Gets the users file then parses it and stores the information in a format that allows it to be used for 
Piecewise Linear Interpolation and Least Squares Approximation calculations. 

Args:
    file_name: the user's file name

    time_step: the time step in the users file
    temperatures: the temperatures in the users file

Yields:
    A dataclass object that stores the temperatures at each time for a given set of data in the users' file. 

"""

file_name = input().strip()
file_dataset = Dataset(file_name = file_name)
with open(file_name, "r", encoding="utf-8") as tmp_file:
    for time_step, temperatures in parse_temps.parse_raw_temps(tmp_file):
        file_dataset.intervals.append(time_step)
        file_dataset.intervaltemps[time_step] = temperatures


"""
Writes one output file per core (core-<n>-output.txt, in the current
directory). Each line gives the line y = b + m*x that joins two consecutive
time steps for that core:
 
    {time step i} <= x <= {time step i+1} ; y = {b} + {m} x ; interpolation
 
Args:
    file_dataset: the Dataset built above.
 
Yields:
    output_files: the list of paths to the .txt files that were written.
"""

output_files = piecewise_linear_interpolation.output_interpolation(file_dataset)