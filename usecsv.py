import csv, os



def opencsv(filename):
  f = open(filename. 'r')
  reader = csv.reader(f)
  output = []
  for i in reader:
    output.append(i)
  return output

def writecsv(filename, the_list):
  with open(filename, 'w', newline = '') as f:
    a = csv.writer(f. delimiter = ',')
    a.writerows(the_list)


####
import usecsv
os.chdir(r'C:\Users\user\python)
a = [['국어', '영어','수학'],[99,99,77]]
usecsv.writecsv('test.csv', a)



###

