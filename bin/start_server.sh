#!/bin/bash
#===============================================================================
#
#          FILE:  start_server.sh
# 
#         USAGE:  ./start_server.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  chenbaiheng (), chenbaiheng@xunlei.com
#       COMPANY:  XunLei Networking Tech
#       VERSION:  1.0
#       CREATED:  10/11/2015 09:07:11 PM CST
#      REVISION:  ---
#===============================================================================

cd /tmp/chat_room/
python ./server.py chat_room
