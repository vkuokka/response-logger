from datetime import datetime

class Logger:

	def __init__(self, file):
		try:
			self.logfile = open(file, 'a+')
		except IOError:
			raise IOError

	def log(self, response, url_dict):
		try:
			self.logfile.write(
				f"{'Sent:'.ljust(15)}{'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())}\n" +
				f"{'URL:'.ljust(15)}{str(response.url)}\n" +
				f"{'Response:'.ljust(15)}{str(response.elapsed.total_seconds())}\n" +
				f"{'Code:'.ljust(15)}{('PASS' if url_dict['code'] == response.status_code else 'FAIL')}\n" +
				f"{'Content-Type:'.ljust(15)}{('PASS' if url_dict['content-type'] in response.headers['content-type'] else 'FAIL')}\n" +
				f"{'Content:'.ljust(15)}{('PASS' if url_dict['content'] in response.text else 'FAIL')}\n" +
				'\n'
			)
			self.logfile.flush()
		except IOError:
			raise SystemExit('Problems with logger.')

	def error(self, url, message):
		try:
			self.logfile.write(
				f"{'Sent:'.ljust(15)}{'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())}\n" +
				f"{'URL:'.ljust(15)}{str(url)}\n" +
				f"{'Exception:'.ljust(15)}{message}\n" +
				'\n'
			)
			self.logfile.flush()
		except IOError:
			raise SystemExit('Problems with logger.')
