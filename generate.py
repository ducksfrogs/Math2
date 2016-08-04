'''
Generate equally spaced floating point
numbers between two given values
'''

def frange(start, final, increment):
    numbers= []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

