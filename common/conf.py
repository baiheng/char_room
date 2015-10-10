#!/bin/env python
# -*- coding:utf8 -*-


# 项目名
service_name = "wx_pay"

# mysql user
mysql_user = "erp_user_%s" % service_name
mysql_pwd = "123456"
mysql_db = "erp_db_%s" % service_name

# session 过期时间 1 天
session_timeout = 86400

# 验证码过期时间 30 分钟
verify_timeout = 1800

