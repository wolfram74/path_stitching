'''
pixel lock is the tendency for centroid detection to preferentially result in in units of rational fractions of pixels when producing sub-pixel locations.
measuring how prominent this effect is can be done by inspection by making a plot of just the subpixel position information
or by calculating how it differs from the linear distribution.
If there are N particles, there 2N position values. Any given value should appear 2N/1000=k times if the program returns 3 digits past the pixel.
If we count how many times a value appears and call it Cj, corresponding with values from 0 to 999 a range of 1000 or gamma, we can sum over (k-cj)^2/gamma
If the distribution of Cj is flat, the sum returns 0. If the distribution is a dirac delta, we'd get (k-2n)^2/gamma + 999*k^2/gamma
'''
import numpy
def plock_metric(file_name):
    slide = load_file(file_name)
    elements = flatten_slide(slide)
    census = numpy.zeros(1000)
    count = len(elements)
    for element in elements:
        census[int(element.split('.')[1])] += 1
    k = float(count)/len(census)
    print elements[:4]
    print census[:4]
    print slide[:4]
    print k
    addition = ((census-k)**2).sum()
    print addition/(len(census)**2)

def load_file(path):
    output = []
    with open(path) as f:
        next(f)
        for line in f:
            output.append(parse_line(line))
    return output

def parse_line(line):
    values = line.rstrip().split()
    values.pop(0)
    return values

def flatten_slide(points):
    return [ e0 for point in points for e0 in point]

plock_metric('/Users/apprentice/Desktop/schoolwork/independent_study/image_processing/python_attempt/test_suite/2016_04_12:12:06:27_test_data/test_slide_0006.txt')
plock_metric('/Users/apprentice/Desktop/schoolwork/independent_study/image_processing/imageJ_exploration/test_results/cW__0005.txt')
