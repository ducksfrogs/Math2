'''
Caluculating the mean
'''

def caluculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    #caluculate mean
    mean = s/N

    return mean

if __name__ == '__main__':
    donations = [ 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = caluculate_mean(donations)
    N = len(donations)
    print("Mean donations over the last {0} days is {1}".format(N, mean))
