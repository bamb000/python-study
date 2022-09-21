# -*- coding:utf-8 -*-
import random
import argparse
parser = argparse.ArgumentParser(description='按行随机排序,注意最后一行加回车')

parser.add_argument('--input','-i' ,type=str,nargs=1,help='输入目录',required=True)
parser.add_argument('--output','-a', type=str,nargs=1,help='输出目录',default=["随机排序结果.txt"])
args = parser.parse_args()

f = open(args.input[0], "r", encoding="utf-8")
list=f.readlines()
f.close()

random.shuffle(list)
string=''.join(list)
print(string)

f = open(args.output[0], "w", encoding="utf-8")
f.write(string)
f.close
