import time
import math
import file_reader
import utilities

start_time = time.time()
raw_data = file_reader.read_files('test_data')
end_time = time.time()
print("--- %s seconds to load data---" % (end_time - start_time))

BIN_LENGTH = 7
SPACE_THRESHOLD = 5
FRAME_WIDTH = 800
FRAME_HEIGHT = 600
MAX_X = int(math.ceil(float(FRAME_WIDTH)/BIN_LENGTH))
MAX_Y = int(math.ceil(float(FRAME_HEIGHT)/BIN_LENGTH))

start_time = time.time()
paths = []
frontier = []
for slide_index in xrange(len(raw_data)):
  bins = utilities.empty_bins(MAX_Y, MAX_X)
  if slide_index % 100 == 0:
    print slide_index
  for particle_index in xrange(len(raw_data[slide_index])):
    particle = raw_data[slide_index].pop()
    x_index = int(particle[0]/BIN_LENGTH)
    y_index = int(particle[1]/BIN_LENGTH)
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
      bins[int(match[1]/BIN_LENGTH)][int(match[0]/BIN_LENGTH)].pop()
    else:
      frontier.pop(frontier_index)
  unmatched = utilities.flatten_list(utilities.flatten_list(bins))
  for particle in unmatched:
    frontier.append(len(paths))
    paths.append([particle])

end_time = time.time()

print("--- %s seconds to stitch paths ---" % (end_time - start_time))

start_time = time.time()
raw_data = file_reader.save_paths(paths)
end_time = time.time()
print("--- %s seconds to save data---" % (end_time - start_time))

print len(paths)
