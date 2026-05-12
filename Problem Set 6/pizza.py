import sys
import csv
from tabulate import tabulate

#if the argv is less than 2 return too few arguments
try:
    if len(sys.argv) < 2:
        print("Too few command-line arguments.")
    #if the argv is greater than 2 return too many arguments
    if len(sys.argv) > 2:
        print("Too many command-line arguments.")
    #if len(sys.argv) == 2
    if len(sys.argv) == 2:
        #if sys.argv.endswith(".csv")
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], "r") as file:
                output = csv.DictReader(file)
                header = output.fieldnames
                print(tabulate(output, headers="keys",tablefmt="grid"))
        #elif not sys.argv.endswith(".csv")
        elif not sys.argv[1].endswith(".csv"):
            print("Not a csv file.")
except FileNotFoundError:
    sys.exit("File not found")



