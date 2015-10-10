#!/bin/env python
#-*- coding: UTF-8 -*-

import socket
import struct
import mmhash
import datetime
import time

import mylog
import redis_ctl
import conf


def is_num(word):
    try:
        int(word)
        return True
    except:
        try:
            float(word)
            return True
        except:
            return False

def to_int_ip(str_ip):
    return int(socket.ntohl(struct.unpack("I",socket.inet_aton(str(str_ip)))[0]))

def to_str_ip(int_ip):
    if not str(int_ip).isdigit():
        return ""
    else:
        int_ip = int(int_ip)
    return socket.inet_ntoa(struct.pack("I", socket.htonl(int_ip)))

def get_bcrypt_str(bcrypt_str):
    hashed = bcrypt.hashpw(str(bcrypt_str), bcrypt.gensalt(10))
    return hashed

def check_bcrypt_str(plain_str, bcrypt_str):
    if bcrypt.hashpw(str(plain_str), str(bcrypt_str)) == str(bcrypt_str):
        return True
    else:
        return False

def del_sessionid(user_id):
    if redis_ctl.redis_db.check_connect():
        redis_ctl.redis_db.db.delete('%s_Sid_%s' % 
                (conf.service_name, user_id))
        mylog.logger.debug("redis del key: %s_Sid_%s" % 
                (conf.service_name, user_id))
        return True
    else:
        mylog.logger.error("redis del key: %s_Sid_%s error" % 
                (conf.service_name, user_id))
        return False


def check_sessionid(sessionid, user_id):
    if user_id == -1 or sessionid == "":
        return False
    if redis_ctl.redis_db.check_connect():
        sid = redis_ctl.redis_db.db.get('%s_Sid_%s' % 
                (conf.service_name, user_id))
        mylog.logger.debug("redis get key: %s_Sid_%s, values: %s" % 
                (conf.service_name, user_id, sid))
        if sid is None:
            return False
        if str(sessionid) == str(sid):
            return True
        else:
            mylog.logger.error("err login %s" % user_id)
    return False

def create_sessionid(user_id):
    sessionid = mmhash.get_unsigned_hash("%s+session+%d" % 
            (user_id, time.time()))
    if redis_ctl.redis_db.check_connect():
        redis_ctl.redis_db.db.setex('%s_Sid_%s' % 
                (conf.service_name, user_id), conf.session_timeout, sessionid)
        mylog.logger.debug("redis set key: Sid_%s, values: %s, timeout: 86400" % 
                (user_id, sessionid))
        return sessionid
    else:
        mylog.logger.error("redis disconnect")
        return None

def get_uright(user_id):
    uright = redis_ctl.redis_db.db.get("%s_uright_%s" % 
            (conf.service_name, user_id))
    if uright != None:
        return int(uright)
    else:
        return None

def get_utf8_param(input, name, default=""):
    return input.get(name, default).encode("utf8")

def get_int_param(input, name, default=-1):
    return int(input.get(name, default))

def get_float_param(input, name, default=-1):
    return float(input.get(name, default))

def get_purchase_summary_id():
    key = "%s_purchase_order_id" % conf.service_name
    id = get_today_order_id(key)
    return "CG%s" % id

def get_return_purchase_summary_id():
    key = "%s_return_purchase_order_id" % conf.service_name
    id = get_today_order_id(key)
    return "TCG%s" % id

def get_sale_summary_id():
    key = "%s_sale_order_id" % conf.service_name
    id = get_today_order_id(key)
    return "XS%s" % id

def get_return_sale_summary_id():
    key = "%s_return_sale_order_id" % conf.service_name
    id = get_today_order_id(key)
    return "TXS%s" % id

def get_inventory_summary_id():
    key = "%s_inventory_order_id" % conf.service_name
    id = get_today_order_id(key)
    return "PD%s" % id

def get_payment_summary_id():
    key = "%s_payment_order_id" % conf.service_name
    id = get_today_order_id(key)
    return "FK%s" % id

def get_today_order_id(key):
    prefix = time.strftime('%Y%m%d',time.localtime(time.time()))
    if redis_ctl.redis_db.check_connect():
        if int(redis_ctl.redis_db.db.exists(key)) == 1:
            value = redis_ctl.redis_db.db.incr(key)
        else:
            tomorrow = time.mktime(time.strptime(str(datetime.date.today()+datetime.timedelta(days=1)), "%Y-%m-%d"))
            diff_time = int(int(tomorrow) - int(time.time()))
            redis_ctl.redis_db.db.setex(key, diff_time, 1)
            value = 1
        mylog.logger.debug("redis get key: %s, values: %s" % (key, value))
        if int(value) < 100:
            return int("%s%02d" % (prefix, int(value)))
        else:
            return None
    else:
        return None
