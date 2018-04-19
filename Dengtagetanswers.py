#! /usr/bin/env python
#coding=utf-8
import cv2
import numpy as np
import requests
import json
import sys
import os
from pymouse import PyMouse
from PIL import Image, ImageGrab
import time
import aircv as ac
import logging
#from pykeyboard import PyKeyboard

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(level = logging.INFO,
		format = '%(levelname)s %(message)s')

def curl_get():
	print (u'>>正在获取随机题库')
	sublist = []
	for i in range(200):
		print (u'>>正在爬取第%d套试题' % i)
		req = requests.get("http://xxjs.dtdjzx.gov.cn/quiz-api/subject_info/randomList")
		text = json.loads(req.text)['data']['subjectInfoList']

		
		for item in text:
			tt = [item['subjectTitle']]
			# print item['subjectTitle']
			# print item['answer']
			for optionInfo in item['optionInfoList']:
				if optionInfo['optionType'] in item['answer']:
					tt.append(optionInfo['optionTitle'])
					#print optionInfo['optionTitle']
			if tt not in sublist:
				sublist.append(tt)

	with open('C:/tiku.txt','w') as f:
		for item in sublist:
			f.writelines( "******************************\n")
			for s in item:
				f.writelines(s)
				f.writelines('\n')
		f.writelines( "******************************\n")
		f.close()
	print (u'>>共爬取到%d道题' % len(sublist))

if __name__ == '__main__':
	curl_get()