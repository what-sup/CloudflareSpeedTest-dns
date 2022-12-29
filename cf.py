import random
import time
import json
import urllib3
import traceback
import jsonpath
import requests
import yaml
import os
import csv
from log import Logger

log_debug = Logger('cfdns.log', level='debug')
urllib3.disable_warnings()

cfips = []
api = ''
mail = ''
domain = ''
dns = ''

def get_line():
	with open('./result.csv', encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		print(type(csvReader))
		cfips.append(next(csvReader))


def get_ip():
	for i in range(10):
#		os.system("CloudflareSpeedTest.exe -t 8 -tll 100 -sl 1")
		os.system("./CloudflareSpeedTest -t 8 -tll 100 -sl 1")
		get_line()



def sort_ip():
	ippath = "$..ip"
	speedpath = "$..speed"
	losspath = "$..loss"
	ips = jsonpath.jsonpath(cfips, ippath)
	speeds = jsonpath.jsonpath(cfips, speedpath)
	losses = jsonpath.jsonpath(cfips, losspath)
	tmpspeed = speeds[0]
	ret = ips[0]
	for i in range(len(ips)):
		if float(tmpspeed) < float(speeds[i]) and int(float(losses[i])) == 0:
			tmpspeed = speeds[i]
			ret = ips[i]
	return ret

def put_cf(ip):

	url = "https://api.cloudflare.com/client/v4/zones/" + domain + "/dns_records/" + dns
	head = {
		"Content-Type": "application/json",
		"X-Auth-Email": mail,
		"X-Auth-Key": api
	}
	data = '{"content": "'+ ip + '"}'
	log_debug.logger.info(ip)
	log_debug.logger.info(url)
	log_debug.logger.info(requests.patch(url, headers = head, data = data).content)
	

def main():
	os.system("chmod +x CloudflareSpeedTest")
	get_ip()
	print(cfips)
	result = sort_ip()
	put_cf(result)

if __name__ == '__main__':
	main()