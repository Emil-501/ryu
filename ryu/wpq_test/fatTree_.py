# conding=utf-8
#!/usr/bin/env python
"""Custom topology example
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)
        L1 = 2
        L2 = L1 * 2
        L3 = L2
        c = []
        a = []
        e = []

        # 核心层交换机
        for i in range(L1):
            # datapath = '000000000000000' + str(i)
            # print datapath
            sw = self.addSwitch('s{}'.format(i + 1), dpid=str('000000000000000'+str(i+1)))
            c.append(sw)


        # 汇聚层交换机
        for i in range(L2):
            sw = self.addSwitch('a{}'.format(i + 1), dpid=str('000000000000001'+str(i+1)))  # L1 + i + 1 ) )
            a.append(sw)

        # 接入层交换机
        for i in range(L3):
            sw = self.addSwitch('e{}'.format(i + 1), dpid=str('000000000000002'+str(i+1)))  # L1 + L2 + i + 1 ) )
            e.append(sw)

        # 汇聚层交换机与核心层交换机的对接
        for i in range(L1):
            sw1 = c[i]
            for sw2 in a[i / 2::L1 / 2]:
                self.addLink(sw2, sw1)

        # 汇聚层交换机与接入层交换机的对接
        for i in range(0, L2, 2):
            for sw1 in a[i:i + 2]:
                for sw2 in e[i:i + 2]:
                    self.addLink(sw2, sw1)

        # 加入主机并与接入层交换机对接
        count = 1
        for sw1 in e:
            for i in range(2):
                host = self.addHost('h{}'.format(count))
                self.addLink(sw1, host)
                count += 1


topos = {'mytopo': (lambda: MyTopo())}
