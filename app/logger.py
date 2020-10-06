from datetime import datetime

class Logger:

	def __init__(self, file):
		self.logfile = file

	def log(self, response, url_dict):
		try:
			file = open(self.logfile, 'a+')
			file.write(f"Sent:			{'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())}\n")
			file.write(f"URL:			{str(response.url)}\n")
			file.write(f"Response:		{str(response.elapsed.total_seconds())}\n")
			file.write(f"Code:			{('Correct' if url_dict['code'] == response.status_code else 'Incorrect')}\n")
			file.write(f"Content-Type:	{('Correct' if url_dict['content-type'] in response.headers['content-type'] else 'Incorrect')}\n")
			file.write(f"Content:		{('Correct' if url_dict['content'] in response.text else 'Incorrect')}\n")
			file.write('\n')
			file.close()
		except IOError:
			raise SystemExit('Problems with logger.')

	def error(self, url, message):
		try:
			file = open(self.logfile, 'a+')
			file.write(f"Sent:			{'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())}\n")
			file.write(f"URL:			{str(url)}\n")
			file.write(f"Exception:		{message}\n")
			file.write('\n')
			file.close()
		except IOError:
			raise SystemExit('Problems with logger.')
