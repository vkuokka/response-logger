import json
import requests
from logger import Logger

def runner(urls, config, logger):


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
	runner(urls, config, logger)


if __name__ == "__main__":
    main()