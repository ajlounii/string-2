def end_other(a, b):
  sum=a.lower()
  sum2=b.lower()
  if sum.endswith(sum2):
    return True
  if sum2.endswith(sum):
    return True
  return False

