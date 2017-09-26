#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 - InfinityLoop <swsoyee@gmail.com>
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('python delnull.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('python delnull.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   #　何番目の列
   index = []
   #　全部の出力結果を保存
   totalContent = []
   fileObject = open(inputfile, 'rU')
   try:
      for line in fileObject:
         #　一行の内容をタブで区切って、Contentで保存
         content = line.split('\t')
         content = [w.replace('\n', '') for w in content]
		 
         totalContent.append(content)
         # Indexに既に値が入った場合は、足す。なかった場合はそのCellの文字数をIndexに追加
         for i in range(len(content)):
            try:
               index[i]+=len(content[i])
            except IndexError:
               index.append(len(content[i]))
   finally:
      fileObject.close()
   # Indexで列のすべての文字長さが１に超える列だけを抽出し、fileで保存
   file = ''
   for i in range(len(totalContent)):
      for j in range(len(totalContent[i])):
         if index[j]!=0:
            file += totalContent[i][j] + '\t'
      file += '\n'
   # 出力する
   with open(outputfile, 'wt') as f:
      print(file, file=f)

if __name__ == "__main__":
   main(sys.argv[1:])
