# 2021-06-09
# Use this to send raw packets with python
# $ printf "somebytes" | sudo python3 sendframe.py
# https://twitter.com/netspooky/status/1402647501090459653

from socket import *
import sys

interface = "ens33" # Change

data = sys.stdin.buffer.read()
s = socket(AF_PACKET, SOCK_RAW)
s.bind((interface, 0))
s.send(data)
