#!/usr/bin/python3

import time
import sys
f = open("qqq.txt", 'w', 1)
for i in range(200):
	# print(time.time())
	print(i, file=f)
	print(i)
	# f.flush()
	time.sleep(2)
