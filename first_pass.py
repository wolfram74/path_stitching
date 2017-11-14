import numpy
from PIL import Image
import sys
import random
import time
from skimage import measure
# print sys.path
print "things loaded"
name = "../blue_drive/movie2_12W_expt8/cW__%04d.tif"
im = Image.open("cW__0001.tif")

print im.getpixel((0,0))
# 1600 x 1200 pixels
# 2-byte grey scale, max value is 65535?
# observed max for 0001 is 65532
# observed min is 1112
# related search terms: region detection, blob detection, weighted centroid detection
# http://www.iis.sinica.edu.tw/~fchang/paper/component_labeling_cviu.pdf
#
# http://benbritten.com/2008/05/29/70/
def backgroundNoise():
  sampleSize = 100
  samples = []
  sampleSum = 0
  height = len(imarray)
  width = len(imarray[0])
  for i in range(sampleSize):
    samples.append(imarray[random.randint(0,height-1)][random.randint(0,width-1)])
    sampleSum += samples[-1]
  print samples
  print sampleSum/sampleSize

imarray = numpy.array(im)
print imarray.shape
print imarray.size
# print imarray[2][70:110]
# print imarray[3][70:110]
# print imarray[4][70:110]
print len(imarray[0])
print numpy.amax(imarray)
print numpy.amin(imarray)
a = measure.regionprops(imarray)
print a[0].centroid
print a[0:5]
for i in range(200):
  print a[i].centroid
print [len(a), 'centroids']

start_time = time.time()
# for i in range(100):
#   imageI = Image.open(name % (10*(i+1)))
#   imageArray = numpy.array(imageI)
#   properties = measure.regionprops(imageArray)
#   print properties[400].centroid
#   print len(properties)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
print("--- %s seconds per slide ---" % ((end_time - start_time)/100))
