#!/usr/bin/env python3
import requests

## fire at the location 51 times

cnt = 1

while cnt <52:
  requests.get("http://10.4.10.44:2224/fast")
  cnt += 1
