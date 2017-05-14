import re
import json
str = '''
Obtaining JSON from switch...
Done
Control utility for runtime P4 table manipulation
RuntimeCmd: dmac                           [implementation=None, mk=ethernet.dstAddr(exact, 48),	ethernet.srcAddr(exact, 48)]
********************************************************************************
_nop                           []
mac_learn                      [port(9)]
RuntimeCmd:
'''

matchObj = re.findall('mk=(.*)\(.*\,\s*(.*)\(.*\)', str, re.M | re.I)

print matchObj[0]

matchObj1 = re.findall('[\n](\S+)(?=[\s]*\[(.*)\])', str, re.M | re.I)

print matchObj1