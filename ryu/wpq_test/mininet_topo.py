from mininet.topo import Topo


class MyTopo(Topo):
    def __init__(self):
        # initilaize topology
        Topo.__init__(self)

        # add hosts and switches
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        # add links
        self.addLink(host1, switch1, 1, 1)
        self.addLink(host2, switch1, 1, 2)
        self.addLink(host3, switch2, 1, 1)
        self.addLink(host4, switch2, 1, 2)


topos = {'mytopo': (lambda: MyTopo())}