def empty_bins(j, k):
  '''resulting nested structure will have j rows and k columns'''
  # return [[[] for n in range(k)] for m in range(j)]
  return tuple(tuple([] for n in range(k)) for m in range(j))

def flatten_list(input_list):
  return [item for sublist in input_list for item in sublist]

def neighbor_indices(particle, length, max_x, max_y):
  '''Presumes a particle is tracked as a tuple (x,y,t)'''
  center = (particle[0]/length,particle[1]/length)
  targets = []
  for dx in range(3):
    for dy in range(3):
      x_index = (center[0]-1+dx) % max_x
      y_index = (center[1]-1+dy) % max_y
      targets.append((x_index, y_index))
  return targets

def proximity_check(particle1, particle2, threshold):
  delta_x = particle1[0] - particle2[0]
  delta_y = particle1[1] - particle2[1]
  return delta_y**2+delta_x**2 < threshold**2
