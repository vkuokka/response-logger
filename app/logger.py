from datetime import datetime

class Logger:

	def __init__(self, file):
		self.logfile = file

	def log(self, response, url_dict):
		try:
			file = open(self.logfile, 'a+')
			file.write(
				f"Sent:         {'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())}\n" +
				f"URL:          {str(response.url)}\n" +
				f"Response:     {str(response.elapsed.total_seconds())}\n" +
				f"Code:         {('PASS' if url_dict['code'] == response.status_code else 'FAIL')}\n" +
                                f"Content-Type: {('PASS' if url_dict['content-type'] in response.headers['content-type'] else 'FAIL')}\n" +
				f"Content:      {('PASS' if url_dict['content'] in response.text else 'FAIL')}\n" +
				'\n'
			)
			file.close()
		except IOError:
			raise SystemExit('Problems with logger.')

	def error(self, url, message):
		try:
			file = open(self.logfile, 'a+')
			file.write(
				f"Sent:         {'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())}\n" +
                                f"URL:          {str(url)}\n" +
                                f"Exception:    {message}\n" +
				'\n'
			)
			file.close()
		except IOError:
			raise SystemExit('Problems with logger.')
