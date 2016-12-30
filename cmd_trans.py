#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,argparse

key = 914995308
keyfrom = 'lin-trans'

def translate(query=''):
	params = {'keyfrom':keyfrom,'key':key,'version':1.1,'type':'data','doctype':'json','q':query}
	r = requests.get('http://fanyi.youdao.com/openapi.do',params=params)
	#print(r.json()['query'])
	print(r.json()['translation'][0])


if __name__ == '__main__':	
	parser = argparse.ArgumentParser()
	parser.add_argument('query',nargs='+',help='输入需翻译的文本',type=str,default='')
	args = parser.parse_args()
	QUERY = ' '.join(args.query)
	
	translate(QUERY)
