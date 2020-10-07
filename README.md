# response-logger
A program that monitors web sites and reports their availability.

## Getting started

#### Prerequisites
You need to have python3 installed into your computer. You can find installation guides for different operating systems here: https://realpython.com/installing-python/

#### Installation
Clone the repository and install required package distributions with the following commands:
```
git clone https://github.com/vkuokka/response-logger.git && cd response-logger && pip3 install -r requirements.txt
```
#### Running the application
After succesful installation you can run the application with the following command:
```
python3 app/main.py
```
This launches the program which sends HTTP GET request to https://google.fi in three second intervals. Program compares key information from server response
with expected information set in `urls.json` file and logs the results into `response.log` file. By default the program does not do much, but the user can
modify the configurations ie. adding websites where requests are sent and what information is expected to be received.
#### Configurations
The main configurations are set in config.json file.
```
{
	"logfile": "log/response.log",
	"timeout": 0.5,
	"interval": 3
}
```
- `logfile` determines the file where logs are written.  
- `timeout` determines general instruction how long each request will wait for response before logging timeout exception.  
- `interval` determines the time spent in "waiting" between requests.  

The program sends requests and compares responses according to the information found in `urls.json` file.
```
[
	{
		"url": "https://google.fi",
		"code": 200,
		"content-type": "text/html",
		"content": ""
	}
]
```
- `url` determines where the requests are sent to.  
- `code` determines what HTTP status code is expected in response.  
- `content-type` determines expected type of content sent from server.  
- `content` determines a string that will be searched from the response body.  

<strong> ! </strong> All of the fields have to be present in the object, but `content-type` and `content` can contain empty string.<strong> ! </strong>
#### Logs
By default the logs are written into `response.log` file.
```
Sent:         2020-10-07 14:30:08
URL:          https://www.google.fi/
Response:     0.089264
Code:         PASS
Content-Type: PASS
Content:      PASS
```
- `Sent` contains the timestamp when the request was logged. 
- `URL` contains the information where the request was sent to.  
- `Response` contains the time it took to receive a response from server.  
- `Code` determines if the received HTTP status code matches the code set in the `urls.json` object.  
- `Content-Type` determines if the received content-type matches the content-type set in the `urls.json` object.  
- `Content` determines if the response body includes the string set in the `urls.json` object.  

<strong> ! </strong> If the response value does not match with the expected one, it is logged as `FAIL` instead of `PASS`<strong> ! </strong>  

In case the program encounters error while sending a request, the request is logged as an exception.
```
Sent:       2020-10-07 14:48:06
URL:        https://google.fi
Exception:  HTTPSConnectionPool(host='google.fi', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x10bff0b20>, 'Connection to google.fi timed out. (connect timeout=0.001)'))
```
In this specific case we notice that the response from https://google.fi took too long and the connection was closed.
