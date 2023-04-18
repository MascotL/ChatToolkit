*（这只是一个个人测试项目，用于学习）*  
## 说明 ##

项目调用了由openai开发的用于使用ChatGPT的第三方接口  
项目使用python编写，使用了第三方pip包：```openai```  

## 使用 ##

您需要先安装python  
下载的第三方pip包：openai  
获取你的openai的api的密钥

* 双击打开```window_main.py```文件，运行主窗口程序  
* 输入```.set key <密钥>```设置您的api密钥
* 在主窗口下面输入框中输入您想要聊天的内容
* 点击```Send```按钮或者按下回车键发送
* 等待ChatGPT回复

## 设置 ##

    指令格式：  ```.set <参数> <值>```
* 在输入栏输入```.set key <密钥>```设置您的api密钥
* 在输入栏输入```.set temp <值>```设置创造度（取值0~1）
* 在输入栏输入```.help'''查看帮助```
