#!/usr/bin/python  
#-*- coding:utf-8 -*-

#err.py
#import os
#os.name

#try:
#	import cpickle as pickle
#except importerror:
#	import pickle



#import json

#class Student(object):
#	def __init__(self,name,age,score):
#		self.name=name
#		self.age=age
#		self.score=score

#如果要启动大量的子进程，可以用进程池的方式批量创建子进程



#from multiprocessing import Pool
#import os,time,random

#def long_time_task(name):
#	print 'Run task %s (%s)...' %(name,os.getpid())
#	start=time.time()
#	time.sleep(random.random()*3)
#	end=time.time()
#	print 'Task %s runs %0.2f seconds.' %(name,(end-start))

#if __name__=='__main__':
#	print 'Parent process %s.' % os.getpid()
#	p=Pool()
#	for i in range(5):
#		p.apply_async(long_time_task,args=(i,))
#	print 'Waiting for all subprocesses done...'
#	p.close()
#	p.join()
#	print 'All subprocesses done.'


import threading, multiprocessing

def loop():
	x=0
	while True:
		x=x^1

for i in range(multiprocessing.cpu_count()):
	t=threading.Thread(target=loop)
	t.start()
