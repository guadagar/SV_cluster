
import os, sys,time
import subprocess as sp


python_path ='python3.9'
run_file = 'model.py'
tdir = './'
NUM_SEEDS = 10

for i in range(1, int(NUM_SEEDS) + 1):
	Proc = sp.Popen([python_path,run_file,'-seed',str(i)],cwd = tdir, close_fds=True)
	pid_ = Proc.pid
	
