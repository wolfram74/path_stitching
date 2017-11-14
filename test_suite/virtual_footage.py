'''
#concept
generate a few slides of data in the format
  XM  YM
n ddd.ddd ddd.ddd
generate a list of points in a hexagonal grid filling a widthXheight space.
print to file
loop as many times as desired
    apply a velocity field Vx = Vdrift(Y-height/2)/(height/2) so the lowest y values are moving left, the highest right
    print to file
printing will introduce intentional error in the form of a gaussian displacement vector.
#parameters
V0
width
height
spread
cycles
spacing
'''
import random
import os
import time
width = 800.0
height = 600.0
spacing = (width*height / 3000) **.5 #3000 particles in a square lattice would have this as their spacing constant
V0 = spacing / 2 # driving would be chosen with the expectation that max velocity keeps particles theoretically distinguishable.
spread = 1.0 # the standard deviation in a normal distribution centered at 0
cycles = 5
fail_rate = .005
#hexagon bravais vectors
a1=[1.0,0.0]
a2=[.5,3**.5/2.0]
#positions governed by spacing*(a1*i + a2*j)
minI = int(-2*(width/spacing))
maxI = -minI
minJ = int(-2*(height/spacing))
maxJ = -minJ
##
def line_out(index, point):
    return "%d %.3f %.3f\n" % (index, point[0], point[1])

def noise(point, sigma):
    return (point[0]+random.gauss(0,sigma), point[1]+random.gauss(0,sigma))

def folder_name():
    stamp = time.strftime('%Y_%m_%d:%H:%M:%S')
    return "%s_test_data" % stamp
##
def generate_data():
    samples = []
    for i in range(minI, maxI):
        for j in range(minJ,maxJ):
            pos = [0, 0]
            pos[0] += spacing*(a1[0]*i+a2[0]*j)
            pos[1] += spacing*(a1[1]*i+a2[1]*j)
            if pos[0]%width == pos[0] and pos[1]%height == pos[1]:
                samples.append(pos)
    slides = [samples]
    for dt in range(cycles):
        next_slide = []
        for point in slides[-1]:
            next_point = [0.0,0.0]
            next_point[0] += point[0] + V0*(point[1]-height/2)/(height/2)
            next_point[1] += point[1]
            next_point[0] %= width
            next_slide.append(next_point)
        slides.append(next_slide)
    return slides

def make_files(slide_collection):
    directory = folder_name()
    cwd = os.getcwd()
    abs_path = os.path.join(cwd, directory)
    print 'making %s' % abs_path
    os.makedirs(abs_path)
    for i in range(len(slide_collection)):
        write_file(abs_path, slide_collection, i)
        # file_name = 'test_slide_%04d.txt' % (i+1)
        # address = os.path.join(abs_path, file_name)
        # print 'making %s' % address
        # data = open(address, 'w')
        # for index in range(len(slide_collection[i])):

    return abs_path

def write_file(folder_path, slides, index):
    file_name = 'test_slide_%04d.txt' % (index+1)
    address = os.path.join(folder_path, file_name)
    print 'making %s' % address
    data = open(address, 'w')
    data.write('  XM  YM\n')
    for point_index in range(len(slides[index])):
        if random.random() > fail_rate:
            fuzzed = noise(slides[index][point_index], spread)
            data.write(line_out(point_index, fuzzed ))
    return

def make_virtual_data():
    return make_files(generate_data())

