def round_to_2(x):
    return round(x, 2)
    
    
from math import *
def correlation_solution(xs, ys):
    xm = sum(xs)/len(xs)
    ym = sum(ys)/len(ys)
    sum1 = sum2 = sum3 = 0;
    for i in range(len(xs)):
        sum1 += (xs[i] - xm)*(ys[i] - ym)
        sum2 += (xs[i] - xm)**2
        sum3 += (ys[i] - ym)**2
    corr = sum1/sqrt(sum2 * sum3)
    corr = round_to_2(corr)
    return corr


if __name__ == '__main__':
    xs = [float(x) for x in input().strip('[]').split(', ')]
    ys = [float(x) for x in input().strip('[]').split(', ')]
    
    print(correlation_solution(xs, ys))
