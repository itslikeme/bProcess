import os, time, sys

class program(object):
	"""Class responsible for program's parameters."""
	def __init__(self, name, version, currentTime):
		super(program, self).__init__()
		self.name = name
		self.version = version
		self.ctime = currentTime


class configuration(object):
	"""Class responsible for defining parameters for process file."""
	def __init__(self, file, folder):
		super(configuration, self).__init__()
		self.process_file = str(file)
		self.process_file_folder = folder


def main():
	print '\n [+] Importing process file configurations...'
	config_file = configuration('processes.txt',str(os.path.dirname('processes.txt')))
	f = open(config_file.process_file,'r')
	print ' [+] Process file imported.'
	print ' [+] Reading lines from ' + str(config_file.process_file) + '...'

	line_list = f.readlines()

	print ' [+] Initiating process killing sequence...'
	try:
		while 1:
			for i in line_list:
				i = i.replace('\n','')
				os.system('taskkill /f /im ' + str(i) + ' >nul 2>&1')
	except KeyboardInterrupt:
		print '\n [!] Process killing sequence manually stopped.'
		sys.exit(0)

def init():
	p = program('bProcess','0.1',str(time.ctime()))
	def banner(name,version,time):
		print ' ' + str(name) + ' v.' + str(version) + ' starting at ' + str(time)
		print ' ________________________________________________________'
	banner(p.name,p.version,p.ctime)
	main()


if __name__ == '__main__':
	init()