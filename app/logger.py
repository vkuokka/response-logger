from datetime import datetime

class Logger:

	def __init__(self, file):
		self.logfile = file

	def write(self, url, status, time, content):
		try:
			file = open(self.logfile, 'a')
			file.write('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) + '\n')
			file.write('URL:	' + str(url) + '\n')
			file.write('Time:	' + str(time) + '\n')
			file.write('Code:	' + str(status) + '\n')
			if content:
				file.write('Correct content' + '\n')
			else:
				file.write('Incorrect content' + '\n')
			file.write('\n')
			file.close()
		except IOError:
			raise Exception('Problems while logging.')

