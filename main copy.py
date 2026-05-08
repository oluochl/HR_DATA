import Cleaner as clean
import StatisticsCalculations as stats

data = []

file = open("data/phase0.txt")
lines = file.readlines()
data_phase_0 = []
for line in lines:
    data_phase_0.append(line.strip())

data_phase_1 = []
file = open("data/phase1.txt")
lines = file.readlines()
for line in lines:
    data_phase_1.append(line.strip())

data_phase_2 = []
file = open("data/phase2.txt")
lines = file.readlines()
for line in lines:
    data_phase_2.append(line.strip())

data_phase_3 = []
file = open("data/phase3.txt")
lines = file.readlines()
for line in lines:
    data_phase_3.append(line.strip())

def clean_heartrate_data(data: list) -> tuple:
    file = open(data)
    lines = file.readlines()
    clean_data = []
    removed_count = 0
    for line in lines:
        if line.strip().isdigit():
            clean_data.append(int(line))
        else:
            removed_count += 1    
    return clean_data, "rows skipped:",removed_count

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    clean_heartrate_data(data)
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

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")

cleaned_data_phase_0 = print("Cleaned data phase 0: ", clean_heartrate_data(data_phase_0))
cleaned_data_phase_1 = print("Cleaned data phase 1: ", clean_heartrate_data(data_phase_1))
cleaned_data_phase_2 = print("Cleaned data phase 2: ", clean_heartrate_data(data_phase_2))
cleaned_data_phase_3 = print("Cleaned data phase 3: ", clean_heartrate_data(data_phase_3))

print("Phase 0 Average: ", average(data_phase_0))
print("Phase 1 Average: ", average(data_phase_1))
print("Phase 2 Average: ", average(data_phase_2))
print("Phase 3 Average: ", average(data_phase_3))

print("Phase 0 Range: ", range(data_phase_0))
print("Phase 1 Range: ", range(data_phase_1))
print("Phase 2 Range: ", range(data_phase_2))
print("Phase 3 Range: ", range(data_phase_3))

print("Phase 0 Median: ", median(data_phase_0))
print("Phase 1 Median: ", median(data_phase_1))
print("Phase 2 Median: ", median(data_phase_2))
print("Phase 3 Median: ", median(data_phase_3))

print("Phase 1 Average Using Statistics Module:", stats.average(cleaned_data_phase_0))
print("Phase 1 Median Using Statistics Module:", stats.median(cleaned_data_phase_0))
print("Phase 1 Range Using Statistics Module:", stats.range(cleaned_data_phase_0))
print("Phase 1 Varience Using Statistics Module:", stats.varience(cleaned_data_phase_0))


print("Using the Cleaner Module, this is Phase 0 of the cleaned data:",
      clean.clean_heartrate_data(data_phase_0))