#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 - InfinityLoop <swsoyee@gmail.com>

import sys, getopt
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
# 処理ファイルパス及び出力ファイルパス
inputPath = ""
outputPath = ""
# Help page.
def usage():
  print("-i: Path of input file.\n-o: Path of output file.\n-h: Show this help.")
  return
# 入力パラメータを記録
for op, value in opts:
  if op == "-i":
    inputPath = value
  elif op == "-o":
    outputPath = value
  elif op == "-h":
    usage()
    sys.exit()

#　何番目の列
index = []
#　全部の出力結果を保存
totalContent = []
fileObject = open(inputPath, 'rU')
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
with open(outputPath, 'wt') as f:
    print(file, file=f)
