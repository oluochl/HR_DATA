
import Cleaner as clean

import statistics as stats
     



def clean_heartrate_data(file_name: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """

    file = open(file_name)
    lines = file.readlines()

    clean_data = []
    for line in lines:
        if line.strip().isdigit():
            clean_data.append(int(line))

    return clean_data

    








def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for i in data:
        i = float(i)
        total +=i
    return round(total/len(data), 2)


def median(data: list) -> float:
    sorted_data = sorted(data)
    length_data = len(data)
    index = length_data//2
    
    if length_data % 2 == 0:
        a = float(sorted_data[index])
        b = float(sorted_data[index - 1] )
        return (a + b)/2
    return float(sorted_data[index])
    
    


def range(data: list) -> float:
    maximum = float(max(data))
    minimum = float(min(data))
    return maximum - minimum
    

def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str) -> float:
        
    clean_data = clean_heartrate_data(file)
    
    avg = average(clean_data)
    med = median(clean_data)
    rng = range(clean_data)
    print("Average: ", avg)
    print("Median: ", med)
    print("Range: ", rng)
    print("booyeah!")
    print()
if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")

# Using functions from the statistics module to perform operations on each phase:


