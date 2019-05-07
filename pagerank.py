#/usr/bin/env python

# ======================================================================================
# title           :assighment1.py
# description     :TCSS 554 Information retrieval and Search assignment 1
# author          :Zac Lu
# date            :20190504
# version         :1.0
#
# usage           :python3 pagerank.py
#
# notes           :stopwords.txt and transcripts need to be downloaded for this script
# python_version  :3.7.3
# ======================================================================================

import os
import sys

# constants and gloabl variable
input_file = "Adjacency Matrix.txt"
size = 0

"""
Check if directory exist
"""
def checkFileExist(dirname):
    if not os.path.isfile(dirname):
        print("File doesn't exist")
        exit(1)

"""
Use the input directory and stopword set to build the a dictory{term, term_data}
"""
def buildDictionary(file_name):
  page_dict = {}
  try:
    with open(file_name) as f:
      count = 0
      content = f.read().splitlines()

      for line in content:
        count += 1
        # if count > 200:
        #   break

        line = line.split()
        connected = line[2]
        if connected != '1':
          continue
        from_doc = int(line[0])
        to_doc = int(line[1])
        # Find out the matrix length
        global size
        size = max(size, from_doc)
        size = max(size, to_doc)

        # Check if key exists avoid KeyError
        if from_doc not in page_dict:
          page_dict[from_doc] = set()
        page_dict[from_doc].add(to_doc)

    return page_dict  

  except OSError:
            print(OSError)


def buildMatrix(page_dict):
  matrix = []
  for i in range (size):                 
      new = []         
      for j in range (size):
        new.append(1 if j % 2 == 0 else 0)
      matrix.append(new)

  return matrix

def printArray(input_arr):
  for i in range(0, len(input_arr)):
    for j in input_arr[i]:
      print (input_arr[i][j], end=' ')
    print ()

"""
Main funciton
"""
def main():
  checkFileExist(input_file)
  page_dict = buildDictionary(input_file)
  print (size)
  print (len(page_dict))
  matrix_m = buildMatrix(page_dict)
  # printArray(matrix_m)
 


  # print ("page_dic size: %d" % (len(page_dict)))
  # for key in page_dict:
  #   print ("key: %s" % (key))
  #   print ("values: ", page_dict[key], sep = ' ')


  # key = "2"
  # if key in page_dict:
  #   print (page_dict["2"])
  # else:
  #   print ("Key doesn't exist in the page_dict.")


if __name__ == "__main__":
    main()
