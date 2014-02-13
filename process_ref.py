# -*- coding:utf-8 -*-
import sys
import re
 
'''\BOOKMARK [1][-]{section.0.1}{bookmark string}{}'''
uniprefix = '\\376\\377'
 
f = open(sys.argv[1])
data = f.read()
f.close()
data = data.decode('UTF-8')
lines = data.split('\n')
 
ARG_BOOKMARK_STRING = 4
pattern_bookmark = r'(\\BOOKMARK)' + r' ' + \
        r'\[(.*)\]' + \
        r'\[(.*)\]' + \
        r'\{(.*)\}' + \
        r'\{(.*)\}' + \
        r'\{(.*)\}'
regex_bookmark = re.compile(pattern_bookmark)
 
fmt_bookmark = '%s' + ' ' + \
        '[%s]' + \
        '[%s]' + \
        '{%s}' + \
        '{%s}' + \
        '{%s}'
 
def conv_ucs2(s):
    lst_chars = []
    for c in s:
        d = ord(c)
        tmp = '\\%03o' % ((d >> 8) & 0xFF)
        lst_chars.append(tmp)
        tmp = '\\%03o' % (d & 0xFF)
        lst_chars.append(tmp)
 
    return lst_chars
 
lst_result = []
for line in lines:
    res = regex_bookmark.search(line)
    if res:
        lst_args = list(res.groups())
        lst_chars = conv_ucs2(lst_args[ARG_BOOKMARK_STRING])
        lst_chars.insert(0, uniprefix)
        lst_args[ARG_BOOKMARK_STRING] = ''.join(lst_chars)
        lst_result.append(fmt_bookmark % tuple(lst_args))
    else:
        lst_result.append(line)
 
f = open(sys.argv[1], 'w')
f.write('\n'.join(lst_result))
f.close()
