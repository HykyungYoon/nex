import os, sys
import json

paths = os.getcwd()
files = 'transforms.json'

with open(os.path.join(paths, files), 'r') as f:
  lines = json.load(f)
  number_of_info = []
  frames = lines['frames']
  for frame in frames:
    frame_path = frame['file_path']
    print(frame_path[2:-4])
    number_of_info.append(frame_path)
    frame['file_path'] = frame_path[2:-4]
  print(lines)

  with open(os.path.join(paths, 'transforms_train.json'), 'w') as file:
    json.dump(lines, file,indent="\t")

print(f'length pf frame_info :{len(number_of_info)}')
