
import Cleaner as clean

data = []

file = open("data/phase0.txt")
lines = file.readlines()

data_phase_0 = []

for line in lines:
    data_phase_0.append(line.strip())
#print("Opened data from Phase 0 :  ", data_phase_0)

data_phase_1 = []

file = open("data/phase1.txt")
lines = file.readlines()

for line in lines:
    data_phase_1.append(line.strip())
#print(data_phase_1)

data_phase_2 = []

file = open("data/phase2.txt")
lines = file.readlines()

for line in lines:
    data_phase_2.append(line.strip())
#print(data_phase_2)

file = open("data/phase3.txt")
lines = file.readlines()

data_phase_3 = []

for line in lines:
    data_phase_3.append(line.strip())
#print(data_phase_3)

print("Using the Cleaner Module, this is Phase 0 of the cleaned data:",
      clean.clean_heartrate_data(data_phase_0))



def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_data = []
    removed_count = 0
    for line in data:
        if len(line) == 0 or not line.isdigit():
            data.remove(line)
            removed_count += 1
        else:
            line = int(line)
            cleaned_data.append(line)
    return cleaned_data, "rows skipped:",removed_count

cleaned_data_phase_0 = print("Cleaned data phase 0: ", clean_heartrate_data(data_phase_0))
print()
cleaned_data_phase_1 = print("Cleaned data phase 1: ", clean_heartrate_data(data_phase_1))
print()
cleaned_data_phase_2 = print("Cleaned data phase 2: ", clean_heartrate_data(data_phase_2))
print()
cleaned_data_phase_3 = print("Cleaned data phase 3: ", clean_heartrate_data(data_phase_3))
print()



def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for i in data:
        i = float(i)
        total +=i
    return round(total/len(data), 2)

print("Phase 0 Average: ", average(data_phase_0))
print("Phase 1 Average: ", average(data_phase_1))
print("Phase 2 Average: ", average(data_phase_2))
print("Phase 3 Average: ", average(data_phase_3))


def median(data: list) -> float:
    sorted_data = sorted(data)
    length_data = len(data)
    index = length_data//2
    
    if length_data % 2 == 0:
        a = float(sorted_data[index])
        b = float(sorted_data[index - 1] )
        return (a + b)/2
    return float(sorted_data[index])
    
    

print("Phase 0 Median: ", median(data_phase_0))
print("Phase 1 Median: ", median(data_phase_1))
print("Phase 2 Median: ", median(data_phase_2))
print("Phase 3 Median: ", median(data_phase_3))

def range(data: list) -> float:
    maximum = float(max(data))
    minimum = float(min(data))
    return maximum - minimum
    
print("Phase 0 Range: ", range(data_phase_0))
print("Phase 1 Range: ", range(data_phase_1))
print("Phase 2 Range: ", range(data_phase_2))
print("Phase 3 Range: ", range(data_phase_3))

def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str) -> float:
     
    file = open(" ")
    lines = file.readlines()

    for line in lines:
        file.append(line.strip())

    return "Average:",average,"Median:", median, "Range:", range


print(run("data/phase0.txt"))

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
