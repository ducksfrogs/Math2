'''
Find the variance and standard deviation of a list of numbers
'''

def caluculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    #caluculate the mean
    mean = s/N

    return mean

def find_difference(numbers):
    #find the mean
    mean = caluculate_mean(numbers)
    #find the differnces from the mean
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff

def caluculate_variance(numbers):
    #find the list of differnces
    diff = find_difference(numbers)
    #find squared differnces

    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    #find the variance
    sum_suquared_diff = sum(squared_diff)
    variance = sum_suquared_diff/len(numbers)
    return variance

if __name__ == '__main__':
    donations = [ 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = caluculate_variance(donations)
    print("The variance of the list of numbers is {0}".format(variance))

    std = variance**0.5
    print("The standard deviation of the list of numbers is {0}".format(std))
