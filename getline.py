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
cfips = [
   {
      "ip":"104.17.107.179",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.17",
      "speed":"199.75"
   },
   {
      "ip":"104.25.141.117",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.57",
      "speed":"122.67"
   },
   {
      "ip":"172.64.82.70",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.21",
      "speed":"745.64"
   },
   {
      "ip":"104.25.188.246",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.63",
      "speed":"295.67"
   },
   {
      "ip":"104.20.98.209",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.55",
      "speed":"113.33"
   },
   {
      "ip":"104.19.208.122",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.18",
      "speed":"268.97"
   },
   {
      "ip":"104.25.206.120",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.41",
      "speed":"396.27"
   },
   {
      "ip":"104.24.147.21",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.48",
      "speed":"147.43"
   },
   {
      "ip":"104.17.23.244",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.11",
      "speed":"128.38"
   },
   {
      "ip":"104.20.3.114",
      "已发送":"4",
      "已接收":"4",
      "loss":"0.00",
      "ping":"155.63",
      "speed":"503.74"
   }
]

ippath = "$..ip"
speedpath = "$..speed"
losspath = "$..loss"
ips = jsonpath.jsonpath(cfips, ippath)
speeds = jsonpath.jsonpath(cfips, speedpath)
losses = jsonpath.jsonpath(cfips, losspath)
print(len(ips))
print(losses)
tmpspeed = speeds[0]
ret = ips[0]
for i in range(len(ips)):
	if tmpspeed < speeds[i] and int(float(losses[i])) == 0:
		tmpspeed = speeds[i]
		ret = ips[i]
print(ret)