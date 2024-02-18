## 本地开发

### 创建虚拟环境

~~~~sh
$ python3 -m venv venv
~~~~

### 激活\退出虚拟环境

~~~~sh
$ source venv/bin/activate
$ deactivate
~~~~

如果你是使用 VSCode 或者 PyCharm 等 IDE 进行开发的，则需要在选择解释器（Interpreter）的时候，选择 venv/bin/python 这个解释器，否则代码补全和跳转的功能会不正常。


### 安装依赖
~~~~sh
$ pip install -r requirements.txt
#从线上拉取全部的包
$ venv/bin/pip install -r requirements.txt --no-dependencies
~~~~