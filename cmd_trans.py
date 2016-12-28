import requests,sys

def translate(query):
    params = {'keyfrom':'lin-trans','key':914995308,'version':1.1,'type':'data','doctype':'json','q':query}
    r = requests.get('http://fanyi.youdao.com/openapi.do',params=params)
    #print(r.json()['query'])
    print(r.json()['translation'][0])

def trans(query=None):
    if query  == None:
        argv = sys.argv
        if len(argv) == 1 and __name__ == '__main__':
            print('命令行翻译工具\n用法：trans 要翻译的单词或句子')
        elif len(argv) == 1 and __name__ != '__main__':
            raise TypeError('请输入要翻译的单词或句子')
        elif len(argv) > 1:
            query = ' '.join(argv[1:])
            translate(query)
    else:
        translate(query)

if __name__ == '__main__':
    trans()
