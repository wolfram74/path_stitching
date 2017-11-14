import time
import math
import file_reader
import utilities

raw_data = file_reader.read_files('test_data')
print "3 files read %s " % str(len(raw_data)==3)

BIN_LENGTH = 7
SPACE_THRESHOLD = 5
FRAME_WIDTH = 800
FRAME_HEIGHT = 600
MAX_X = int(math.ceil(float(FRAME_WIDTH)/BIN_LENGTH))
MAX_Y = int(math.ceil(float(FRAME_HEIGHT)/BIN_LENGTH))
paths = []
frontier = []
for slide_index in xrange(len(raw_data)):
  bins = utilities.empty_bins(MAX_Y, MAX_X)
  print slide_index, frontier
  for particle_index in xrange(len(raw_data[slide_index])):
    particle = raw_data[slide_index].pop()
    x_index = particle[0]/BIN_LENGTH
    y_index = particle[1]/BIN_LENGTH
    bins[y_index][x_index].append(particle)
  for frontier_index in xrange(len(frontier)-1, -1, -1):
    path_index = frontier[frontier_index]
    terminus = paths[path_index][-1]
    neighbors = utilities.neighbor_indices(terminus, BIN_LENGTH, MAX_X, MAX_Y)
    candidates = []
    for location in neighbors:
      candidates += bins[location[1]][location[0]]
    matches = []
    for candidate in candidates:
      if utilities.proximity_check(terminus, candidate, SPACE_THRESHOLD):
        matches.append(candidate)
    if len(matches) == 1:
      match = matches.pop()
      paths[path_index].append(match)
      bins[match[1]/BIN_LENGTH][match[0]/BIN_LENGTH].pop()
    else:
      frontier.pop(frontier_index)
  unmatched = utilities.flatten_list(utilities.flatten_list(bins))
  for particle in unmatched:
    frontier.append(len(paths))
    paths.append([particle])

