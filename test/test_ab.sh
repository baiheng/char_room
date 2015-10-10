#!/bin/bash
#===============================================================================
#
#          FILE:  test_ab.sh
# 
#         USAGE:  ./test_ab.sh 
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
#       CREATED:  06/21/2015 11:27:40 PM CST
#      REVISION:  ---
#===============================================================================

ab -n 10 -c 5 http://127.0.0.1:8888/
