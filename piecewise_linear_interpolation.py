"""
Piecewise linear interpolation of CPU core temperatures.
 
For each core, a straight line is fitted through every pair of consecutive
time steps in a Dataset. Each line is written in the form y = b + m*x, where
m is the slope and b is the y-intercept, to a per-core output file
(core-<n>-output.txt), one line of text per time-step pair:
 
    {t_i} <= x <= {t_i+1} ; y = {b} + {m} x ; interpolation
"""

from temps_data import Dataset
from pathlib import Path

def calculate_interpolation(interval_0: float, interval_1: float, temp_0: float, temp_1: float ) -> str:
    """
    Build one formatted output line for a time_step to temperature pair.
 
    Finds the line y = b + m*x through (interval_0, temp_0) and
    (interval_1, temp_1), where m = (temp_1 - temp_0) / (interval_1 - interval_0)
    and b is the y-intercept.
 
    Args:
        interval_0: Start time of the segment, in seconds.
        interval_1: End time of the segment, in seconds.
        temp_0: Core temperature at interval_0.
        temp_1: Core temperature at interval_1.
 
    Yields:
        A newline-terminated string with the segment's time range, intercept
        and slope, with the intercept and slope rounded to 4 decimal places.
    """

    slope_m = (temp_1 - temp_0) / (interval_1 - interval_0)
    intercept_b = temp_1 - slope_m * interval_1
    return f"{interval_0:8.0f} <= x <={interval_1:8.0f} ; y ={intercept_b:12.4f} +{slope_m:12.4f} x ; interpolation\n"

def output_interpolation(temps: Dataset) -> list[Path]:

    """
    Write the piecewise linear interpolation for every core to its own file.
 
    Args:
        temps: Dataset of time steps and per-core temperatures. The number of
            cores is taken from the first time step of each pair.
 
    Yields:
        The list of paths to the per-core output files.
    """

    output_files: list[Path] = []

    for interval in range(len(temps.intervals)-1):
        curr_interval = temps.intervals[interval]
        next_interval = temps.intervals[interval+1]
        for core_n in range(len(temps.intervaltemps[curr_interval])):
            #If creating interpolation strings for the first interval, overwrites any existing output files using the same naming convention.
            if curr_interval == temps.intervals[0]: 
                with open(Path(f"core-{core_n}-output.txt"), "w") as f:
                    f.write(calculate_interpolation(curr_interval, next_interval, temps.intervaltemps[curr_interval][core_n], temps.intervaltemps[next_interval][core_n]))
            else: 
                with open(Path(f"core-{core_n}-output.txt"), "a") as f:
                    f.write(calculate_interpolation(curr_interval, next_interval, temps.intervaltemps[curr_interval][core_n], temps.intervaltemps[next_interval][core_n]))
            if Path(f"core-{core_n}-output.txt") not in output_files:
                output_files.append(Path(f"core-{core_n}-output.txt"))
    return output_files