import requests,sys

def _translate(query):
    params = {'keyfrom':'lin-trans','key':914995308,'version':1.1,'type':'data','doctype':'json','q':query}
    errors = {20:'要翻译的文本过长',30:'无法进行有效的翻译',40:'不支持的语言类型',50:'无效的key',60:'无词典结果'}
    
    r = requests.get('http://fanyi.youdao.com/openapi.do',params=params)
    statu = r.json()['errorCode']
    if statu == 0:
        print(r.json()['translation'][0])
    else:
        print(errors[statu])

def trans(query=None):
    if query  == None:
        argv = sys.argv
        if len(argv) == 1 and __name__ == '__main__':
            print('命令行翻译工具\n用法：trans 要翻译的单词或句子')
        elif len(argv) == 1 and __name__ != '__main__':
            raise TypeError('请输入要翻译的单词或句子')
        elif len(argv) > 1:
            query = ' '.join(argv[1:])
            _translate(query)
    else:
        _translate(query)

if __name__ == '__main__':
    trans()
