# -*- coding:utf-8 -*-
import random
import argparse
from tkinter import N

parser = argparse.ArgumentParser(description='随机数生成')

parser.add_argument('min', type=int,nargs=1,help='最小值')
parser.add_argument('max',type=int,nargs=1,help='最大值')
parser.add_argument('num',type=int,nargs=1,help='输出数量')
args = parser.parse_args()

list=[]
for i in range(args.min[0],(args.max[0]+1)):
    list+=[i]

random.shuffle(list)

i=0
while 1:
    print(list[i])
    i+=1
    if i == args.num[0]:
        break









# parser = argparse.ArgumentParser(description='随机数生成')

# parser.add_argument('--min','-min', type=int,nargs=1,help='最小值，默认为1',default=1)
# parser.add_argument('--max','-max' ,type=int,nargs=1,help='最大值，必须',required=True)
# parser.add_argument('--num','-n' ,type=int,nargs=1,help='输出数量，必须',required=True)
# args = parser.parse_args()

# list=[]
# for i in range(args.min[0],(args.max[0]+1)):
#     list+=[i]

# random.shuffle(list)
# for i in list:
#     print(i)
