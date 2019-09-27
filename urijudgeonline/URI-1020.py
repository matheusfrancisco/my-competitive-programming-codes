# -*- coding: utf-8 -*-

import os
import sys

N = int(input())
r = int(N/365)
N = int(N-(365*r))
m = int(N/30)
N = int(N-(m*30))

print("%s ano(s)" % (r))
print("%s mes(es)" % (m))
print("%s dia(s)" % (N))
