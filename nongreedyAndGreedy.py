#!/urs/bin/env python3

import re


nongreedy = re.compile(r'<.*?>')
mo = nongreedy.search('<To serve man> for dinner.>')
print("nongreedy: " + mo.group())

greedy = re.compile(r'<.*>')
mo = greedy.search('<To serve man> for dinner.>')
print("greedy: " + mo.group())


