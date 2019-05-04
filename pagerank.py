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
        from_doc = line[0]
        to_doc = line[1]

        # Check if key exists avoid KeyError
        if from_doc not in page_dict:
          page_dict[from_doc] = set()
        page_dict[from_doc].add(to_doc)

    return page_dict  

  except OSError:
            print(OSError)

"""
Main funciton
"""
def main():
  checkFileExist(input_file)
  file_name = input_file
  page_dict = buildDictionary(input_file)


  # print ("page_dic size: %d" % (len(page_dict)))
  # for key in page_dict:
  #   print ("key: %s" % (key))
  #   print ("values: ", page_dict[key], sep = ' ')

  print (page_dict["212"])



if __name__ == "__main__":
    main()
