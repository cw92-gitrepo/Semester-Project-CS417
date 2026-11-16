# CPU temperature Interpolation and Least-Squares Approximaton program

A python program that parses a text file and formats the information in that file and then processes the temperatures of each core at each 0 to n-1 interval through Piecewise Linear Interpolation.

The scope of this program will change as the semester progresses. It is currently in stage 2/3 of being developed.



# Requirements

  * Python 3.9

> This code makes use of generic type hints which require python 3.9 and later

# Input Formatting

Input must a valid .txt file name passed as a string. 

EX:

```
test.txt
```

The file must be formatted as follows:

  - One line per time step
  - Each line holds one temperature per core, separated by whitespace
  - Every line has the same number of temperatures (one column per core)

EX:
```
61.0 63.0 50.0 58.0
80.0 81.0 68.0 77.0
62.0 63.0 52.0 60.0
83.0 82.0 70.0 79.0
68.0 69.0 58.0 65.0
```

Where each number represent the temperature of a core at an interval.

The main program will strip extra whitespace before 
or after the file name; but that is the extent of input validation.

# Sample Execution & Output

After changing to the 
```
./Semester Project Phase 1
```
directory in the terminal, run the command
```
python main.py
```

Then type your .txt file file name into the command line.

The output is one .txt file per core, written to the current directory and named core-0-output.txt, core-1-output.txt, and so on. Each file has one line per pair of consecutive time steps, giving the line y = b + m x that joins the two temperatures, in the format:

```
{time step i} <= x <= {time step i+1} ; y = {b} + {m} x ; interpolation
........
{time step i_n-1} <= x <= {time step i_n} ; y = {b_n} + {m_n} x ; interpolation
........
```

EX Output:

```
   0 <= x <=      30 ; y =     61.0000 +      0.6333 x ; interpolation
  30 <= x <=      60 ; y =     98.0000 +     -0.6000 x ; interpolation
  60 <= x <=      90 ; y =     20.0000 +      0.7000 x ; interpolation
  90 <= x <=     120 ; y =    128.0000 +     -0.5000 x ; interpolation
```

