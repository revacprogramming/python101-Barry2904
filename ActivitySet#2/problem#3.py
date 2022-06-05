def get_cs():
  """get string input"""
  k=input("Enter the credentials:- ")
  return k

def cs_to_lot(cs):
  """convert connected string to list of strings"""
  l=list()
  k=cs.split(";")
  for i in k:
    p=i.split("=")
    n=tuple(p)
    l.append(n)
  return l
  
def main():
  cs = get_cs()
  lot = cs_to_lot(cs)
  print(lot)
  
if __name__ == '__main__':
  main()
