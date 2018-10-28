#!/usr/bin/env python3
import re
import itertools

numbers = []

text_file = open('regex_sum_151417.txt','r')
for line in text_file:
    match = re.findall('[0-9]+', line)
    if len(match) == 0:
        continue
    else:
        numbers.append(match)

merged_numbers = itertools.chain(*numbers)
merged_numbers = list(merged_numbers)

total = 0

for i in merged_numbers:
    total += int(i)

print(total)
