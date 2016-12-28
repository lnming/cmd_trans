#命令行翻译工具


##初衷
本人英语比较渣，在Linux环境工作时经常遇到不认识的单词，需要跳出命令行翻译，多有不便
正好在学习Python，因此产生了编写这个工具的想法，权当练习


##使用方法
1. 下载脚本到本地
2. 在命令行在切换到脚本所在目录
3. 运行如下命令
```
python cmd_trans.py 需要翻译的文本
```
例：输入<code>python cmd_trans.py 你好</code>
返回“hello”


##特别说明
1. 目前仅支持中英互译
2. 为更方便使用，推荐用alias别名
在<code>~/.bashrc</code>中写入
<code>alias trans='python /file/path/cmd_trans.py'</code>
如此便可直接通过<code>trans 需要翻译的文本</code>，随时进行翻译
3. 工具使用的是有道的翻译API，每天请求次数有限，建议自己申请key
