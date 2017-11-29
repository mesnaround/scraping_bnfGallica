import collections
import pandas as pd

def flatten(l):
  for el in l:
    if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
      yield from flatten(el)
    else:
      yield el

def initialize_dict(a_set):
  d = {}
  for s in a_set:
    d[s] = [] 
  return d

def extract_dimension(format):
  for elem in format.split('|'):
    if ';' not in elem:
      continue
    else:
      return elem.split(';')[-1] 
  return ''

def append_to_dict(d, a_set):
  for s in a_set:
    d[s].append('')
  return d

with open('keys.csv','r') as f:
  keys = f.readlines()

with open('results.csv','r') as f:
  results = f.readlines()

keys = list(map(lambda x: x.strip().split('#'), keys))
results = list(map(lambda x: x.strip().split('#'), results))
distinct_cols = set(flatten(keys))

if len(keys) != len(results):
  raise ValueError('keys and results lists should be the same!')

data = initialize_dict(distinct_cols)


for i, result in enumerate(results):
  if len(result) != len(keys[i]):
    print(i)
    raise ValueError('results and keys not equal at this index')
  data = append_to_dict(data, distinct_cols)
  
  for j, val in enumerate(result):
    col = keys[i][j]
    if data[col][i] == '':
      data[col][i] = str(val)
    else:
      data[col][i] = data[col][i] + '|' + str(val)

df = pd.DataFrame(data)

df['Dimension'] = df['Format'].apply(lambda x: extract_dimension(x))

df.to_csv('clean.csv', index=False, sep = '#')
  


