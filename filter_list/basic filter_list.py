def filter_list(l):
  arr = []
  for i in l:
      if (type(i) == type(1)):
          arr.append(i)
  return arr