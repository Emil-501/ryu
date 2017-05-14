import re

str = '''Obtaining JSON from switch...
Done
Control utility for runtime P4 table manipulation
RuntimeCmd: dmac                           [implementation=None, mk=ethernet.dstAddr(exact, 48)]
mcast_src_pruning              [implementation=None, mk=standard_metadata.instance_type(exact, 32)]
smac                           [implementation=None, mk=ethernet.srcAddr(exact, 48)]
sad                            [implementation=None, mk=ethernet.srcAddr(exact, 48)]
RuntimeCmd: '''
# flag = 0
# table_name = []
# name = ''
# for i in str:
#     if i == 'R':
#         flag = 1
#         print flag
#     elif i == ' ' and flag == 1:
#         flag = 2
#         print flag
#     elif flag == 2 and i != ' ':
#         name = name + i
#         print flag
#     elif flag == 2 and i == ' ':
#         table_name.append(name)
#         name = ''
#         flag = 3
#         print flag
#     elif flag == 3 and i == '\n':
#         flag = 2
    # print i
# print table_name


matchObj = re.findall('(\S+)(?=[\s]*\[.*\])', str, re.M | re.I)

print matchObj