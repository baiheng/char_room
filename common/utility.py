#!/bin/env python
#-*- coding: UTF-8 -*-

import socket
import struct
import mmhash
import datetime
import time

import mylog


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

def get_utf8_param(input, name, default=""):
    return input.get(name, default).encode("utf8")

def get_int_param(input, name, default=-1):
    return int(input.get(name, default))

def get_float_param(input, name, default=-1):
    return float(input.get(name, default))

