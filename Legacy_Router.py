#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    r1 = net.addHost('r1', cls=Node, ip='180.120.100.5/16')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='180.120.1.1/16', defaultRoute='via 180.120.100.5')
    h2 = net.addHost('h2', cls=Host, ip='191.168.1.1/24', defaultRoute='via 191.168.1.5')
    

    info( '*** Add links\n')
    net.addLink(h1, r1, intfName2='r1-eth1',
                params2={ 'ip' : '180.120.100.5/16' } )
    net.addLink(h2, r1, intfName2='r1-eth2',
                params2={ 'ip' : '191.168.1.5/24' })

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

