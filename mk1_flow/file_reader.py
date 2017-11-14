import os
def read_folder(path):
  contents = os.listdir(path)
  return contents

def read_files(folder):
  # presumes that all files have nnnn.txt as last characters
  file_names = os.listdir(folder)
  output = []
  for name in file_names: #full scan
  # for name in file_names[0:10]: #first 10
    address = os.path.join(folder, name)
    output.append(read_file(address))
  return output

def read_file(address):
  # presumes that all files have nnnn.txt as last characters
  time = int(address[-8:-4])
  time_step = []
  if time % 100 == 0:
    print time
  with open(address) as f:
    # content = f.readlines()
    # content.pop(0)
    next(f)
    for line in f:
      time_step.append(parse_line(line, time))
  return time_step

def parse_line(line, i):
  values = line.rstrip().split()
  values.pop(0)
  return (float(values[0]), float(values[1]), i)

def save_paths(paths_list):
  output = open('saved_paths.txt', 'w')
  for path in paths_list:
    line = []
    for point in path:
      line.append('-'.join(str(e) for e in point))
    output.write(','.join(line))
    output.write('\n')
  return
