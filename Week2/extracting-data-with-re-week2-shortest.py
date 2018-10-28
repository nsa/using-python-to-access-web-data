#!/usr/bin/env python3
import re

print( sum( [ int(i) for i in re.findall('[0-9]+', open('regex_sum_151417.txt','r').read())  ] ) )
