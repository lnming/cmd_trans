#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,sys,argparse

def translate(query):
	params = {'keyfrom':keyfrom,'key':key,'version':1.1,'type':'data','doctype':'json','q':query}
	r = requests.get('http://fanyi.youdao.com/openapi.do',params=params)
	#print(r.json()['query'])
	print(r.json()['translation'][0])

key = 914995308
keyfrom = 'lin-trans'

parser = argparse.ArgumentParser()
parser.add_argument('query',help='输入需翻译的文本')
args = parser.parse_args()
QUERY = args.query

if __name__ == '__main__':
	translate(QUERY)
