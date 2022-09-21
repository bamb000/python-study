import argparse

# 描述，可以写程序名或功能
parser = argparse.ArgumentParser(description='命令行中传入一个数字')

# type参数类型

# nargs是用来说明传入的参数个数，多个参数会聚集到一个列表
# nargs='?'　表示参数可设置零个或一个
# nargs='*' 　表示参数可设置零个或多个
# nargs'+' 表示传入至少一个参数
# nargs=N   N个参数

# 可选参数'--name' '-n'

# default='xxx' 默认值

# required=True 必须参数
parser.add_argument('--integers', type=int,nargs=2,help='传入的数字')
parser.add_argument('--abc','-a', type=int,nargs='+',help='传入的数字')

args = parser.parse_args()
print(sum(args.abc))


#所有传入的参数
print(args)

#获得传入的参数
# print(args.integers)

# 参考链接  https://zhuanlan.zhihu.com/p/56922793
# https://www.jianshu.com/p/9ac116b59215
# https://docs.python.org/zh-cn/3/library/argparse.html