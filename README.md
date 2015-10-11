# 要求系统安装 python tornado ansible 

用tornado websocket 实现在线聊天室基本功能

实现功能:
	1.websocket连接成功服务器后，服务器会返回“欢迎加入聊天室”
	2.加入聊天室后，发送消息其他用户可以接到消息
	3.发送的消息如果是“在线的用户数”，服务器会解析成询问命令，并返回当前在线用户数

假设chat_room目录在tmp下

自动化部署脚本:
	cd /tmp/chat_room/bin && ansible-playbook ./playbook.yml -i ./hosts

启动服务器:
	cd /tmp/chat_room/ && python ./server.py chat_room

自动化测试脚本:
	cd /tmp/chat_room/test && ./run_tests.py

修改/tmp/chat_room/static/js/global.js 中的g_host变量, 改成本地服务器的ip地址+8088
浏览器输入 http://ip_address:8088/static/index.html 即可访问到


