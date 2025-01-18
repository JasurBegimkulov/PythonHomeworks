universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(info):
    enrollments = [university[1] for university in info]
    tuitions = [university[2] for university in info]
    return enrollments, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    mid = len(values) // 2
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2 if len(values) % 2 == 0 else sorted_values[mid]