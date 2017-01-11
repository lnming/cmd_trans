#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,argparse

key = 914995308
keyfrom = 'lin-trans'

def translate(query,mode='all'):
	params = {'keyfrom':keyfrom,'key':key,'version':1.1,'type':'data','doctype':'json','q':query}
	r = requests.get('http://fanyi.youdao.com/openapi.do',params=params)
	translation = r.json()['translation'][0]
	try:
		explains = r.json()['basic']['explains']
	except:
		print(translation)
	else:
		if translation != explains[0]:
			if mode == 'all':
				print('%s\n%s' %(translation,'\n'.join(explains)))
			elif mode == 'trans':
				print(translation)
			elif mode == 'dict':
				print('\n'.join(explains))
		else:
			print(translation)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('query',nargs='+',help='输入需翻译的文本',type=str,default='')
	args = parser.parse_args()
	QUERY = ' '.join(args.query)
	translate(QUERY,'all')
