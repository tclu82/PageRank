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

# constants and global variable
INPUT_FILE = "graph.txt"
SIZE = 0
BETA = 0.85
EPSILON = 0.0001

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
        global SIZE
        SIZE = max(SIZE, from_doc)
        SIZE = max(SIZE, to_doc)

        # Check if key exists avoid KeyError
        if from_doc not in page_dict:
          page_dict[from_doc] = set()
        page_dict[from_doc].add(to_doc)

    return page_dict  

  except OSError:
            print(OSError)

"""
Use page_dict to build Matrix M
"""
def buildMatrixM(page_dict):
  matrix = []
  for i in range (0, SIZE):                 
    temp = []
    for j in range (0, SIZE):
      temp.append(0) 
    matrix.append(temp)

  for i in page_dict:
    count = len(page_dict[i])
    for j in page_dict[i]:
      matrix[j-1][i-1] = 1 / count

  return matrix

"""
Use Matrix M and BETA to build Matrix A
"""
def buildMatrixA(matrix_m):
  matrix_a = []
  for i in range (0, SIZE):                 
    temp = []
    for j in range (0, SIZE):
      value = matrix_m[i][j] * BETA + (1 - BETA) / SIZE
      temp.append(value) 
    matrix_a.append(temp)
  return matrix_a

"""
Build the origin rank vector
"""
def buildOriginRankVector():
  matrix = []
  for i in range (0, SIZE):                 
    temp = []
    for j in range (0, 1):
      temp.append(1 / SIZE) 
    matrix.append(temp)
  return matrix

"""
Print out matrix
"""
def printArray(input_arr):
  for i in range(0, len(input_arr)):
    for j in range(0, len(input_arr[0])):
      print ("%.4f\t" % (input_arr[i][j]), end='')
    print ()

"""
Main funciton
"""
def main():
  checkFileExist(INPUT_FILE)
  page_dict = buildDictionary(INPUT_FILE)
  matrix_m = buildMatrixM(page_dict)
  
  print ("1. The output of Matrix M:")
  printArray(matrix_m)

  print ("\n2. The output of Matrix A:")
  matrix_a = buildMatrixA(matrix_m)
  printArray(matrix_a)
  
  print ("\n3. The origin rank vector:")
  origin_rank_vector = buildOriginRankVector()
  printArray(origin_rank_vector)


if __name__ == "__main__":
    main()
