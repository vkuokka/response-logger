import json
import requests
import time
from logger import Logger

def request(url_dict, timeout, logger):
	try:
		response = requests.get(url_dict['url'], timeout=timeout)
		logger.log(response, url_dict)
	except requests.exceptions.RequestException as error:
		logger.error(url_dict['url'], str(error))

def loop(urls_json, config_json, logger):
	timeout = config_json['timeout']
	interval = config_json['interval']
	while True:
		for url_dict in urls_json:
			request(url_dict, timeout, logger)
		time.sleep(interval)

def main():
	try:
		urls = open('config/urls.json', 'r')
		config = open('config/config.json', 'r')
		urls_json = json.loads(urls.read())
		config_json = json.loads(config.read())
		urls.close()
		config.close()
	except IOError:
		raise SystemExit('Problems with configuration.')
	logger = Logger(config_json['logfile'])
	loop(urls_json, config_json, logger)

if __name__ == '__main__':
	main()
