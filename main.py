import statistics

def dataset_tahlili(royxat):
    mean = statistics.mean(royxat)
    median = statistics.median(royxat)
    mode = statistics.mode(royxat)
    stdev = statistics.stdev(royxat)
    
    return mean, median, mode, stdev

royxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean, median, mode, stdev = dataset_tahlili(royxat)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Stdev: {stdev}")
