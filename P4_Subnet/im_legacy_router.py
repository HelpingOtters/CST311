#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo

def myNetwork():
        net = Mininet( topo=None, build=False, ipBase='0.0.0.0')
        info( '*** Adding controller\n' )

        info( '*** Add switches\n')
        r1 = net.addHost('r1', cls=Node, ip='192.168.1.1/24')
        r1.cmd('sysctl -w net.ipv4.ip_forward=1')

        info( '*** Add hosts\n')
        h1 = net.addHost('h1', ip='192.168.1.100/24', defaultRoute='via 192.168.1.1')
        h2 = net.addHost('h2', ip='172.16.0.100/12', defaultRoute='via 172.16.0.1')

        info( '*** Add links\n')
        net.addLink(h1, r1, intfName2='r0-eth1', params2={ 'ip' : '192.168.1.1/24' } )
        net.addLink(h2, r1, intfName2='r0-eth2', params2={ 'ip' : '172.16.0.1/12' } )

        net.addLink(h1,r1)
        net.addLink(h2,r1)

        info( '*** Starting network\n')
        net.build()

        CLI(net)
        net.stop()

if __name__ == '__main__':
        setLogLevel( 'info' )
        myNetwork()