import time
import sys
import math
import file_reader
import utilities
from random import randint

# start_time = time.time()
# raw_data = file_reader.read_files('text_data')
# print type(raw_data[0][0]).__name__ == 'tuple'
# print type(raw_data[0][0][0]).__name__ == 'int'
# print sys.getsizeof(raw_data)
# # works, but it's very time consuming. roughly a minute
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))

# for slide in raw_data:
#   print len(slide)

# start_time = time.time()
# empty_bins = utilities.empty_bins(5, 3)
# print len(empty_bins) == 5
# print len(empty_bins[0]) == 3
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))

# start_time = time.time()
# test_bin = utilities.empty_bins(5, 3)
# test_bin[randint(0,4)][randint(0,2)].append('a')
# compress = utilities.flatten_list(test_bin)
# print len(compress) == 15
# more_compress = utilities.flatten_list(compress)
# print 'a' in more_compress
# print len(more_compress) == 1
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))

# start_time = time.time()
# flat_data = utilities.flatten_list(raw_data)
# print len(flat_data)
# print sys.getsizeof(flat_data)
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))

start_time = time.time()
for i in range(5500):
  test_bin = utilities.empty_bins(60, 80)
  test_bin[randint(0,59)][randint(0,79)].append('a')
  test_bin[randint(0,59)][randint(0,79)].append('a')
  compress = utilities.flatten_list(test_bin)
  more_compress = utilities.flatten_list(compress)
  if i % 100 == 0:
    print i
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
print("--- %s seconds per cycle---" % ((end_time - start_time)/5500) )
print("--- %s seconds per particle---" % ((end_time - start_time)/(5500*3000)) )

# test_bins = []
# for i in range(11):
#   insertions = 2**i
#   sample = []
#   print i
#   for samples in range(100):
#     test_bin = utilities.empty_bins(60, 80)
#     for part in range(insertions):
#       test_bin[randint(0,59)][randint(0,79)].append('a')
#     sample.append(test_bin)
#   test_bins.append(sample)

# for scale in range(len(test_bins)):
#   start_time = time.time()
#   for sample in test_bins[scale]:
#     flat_data = utilities.flatten_list(sample)
#     linear_data = utilities.flatten_list(flat_data)
#   end_time = time.time()
#   print("%s  %s" % ((end_time - start_time)/100, 2**scale))

# for length in range(1, 11):
#   ybins = int(math.ceil(600.0/length))
#   xbins = int(math.ceil(800.0/length))

#   start_time = time.time()
#   for i in range(1000):
#     test_bin = utilities.empty_bins(ybins, xbins)
#     test_bin[randint(0,ybins-1)][randint(0,xbins-1)].append('a')
#     test_bin[randint(0,ybins-1)][randint(0,xbins-1)].append('a')
#     compress = utilities.flatten_list(test_bin)
#     more_compress = utilities.flatten_list(compress)
#     if i % 100 == 0:
#       print i
#   end_time = time.time()
#   print("--- %s seconds %d bins ---" % (end_time - start_time, ybins*xbins))


# print sys.getsizeof(flat_data)

