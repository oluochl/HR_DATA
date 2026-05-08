import statistics as stats

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

def varience(data: list) -> float:
    return stats.variance(data)

def standard_dev(data: list) -> float:
    return stats.stdev(data)




    
