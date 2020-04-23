import getopt
import sys

help = 'baidu_crawler.py -k <keyword> [-t <timeout> -p <total pages>]'
print(sys.argv[1:])
opts, args = getopt.getopt(sys.argv[1:], "hk:t:p:")
print(opts)
print("---------------------")
print(args)
