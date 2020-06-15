#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo

def myNetwork():
        
        # topology constructor
        # initializes empty topology with no build or ip address 
        net = Mininet( topo=None, build=False, ipBase='0.0.0.0')
        info( '*** Adding controller\n' )
        
        info( '*** Add switches\n')
        # Creates router for host 1 and host 2 to connect; sets its IP address 
        # cls=Node inherets all node class members, and public attributes
        # CIDR to IP Range of 192.168.1.1 - 192.168.1.255 (256 possible hosts)
        r1 = net.addHost('r1', cls=Node, ip='192.168.1.1/24')
        # Sends a command from r1 (host / router), waits for its ouput, and then returns it 
        r1.cmd('sysctl -w net.ipv4.ip_forward=1') 

        info( '*** Add hosts\n')
        # Creates host 1 and 2 and sets their IP adresses and the route to access them
        h1 = net.addHost('h1', ip='192.168.1.100/24', defaultRoute='via 192.168.1.1')
        h2 = net.addHost('h2', ip='192.168.2.100/24', defaultRoute='via 192.168.2.1')

        info( '*** Add links\n')
        # Creates a link between r1(router) to host h1
        net.addLink(h1, r1, intfName2='r0-eth1', params2={ 'ip' : '192.168.1.1/24' } )
        # Creates a link between r1(router) to host h2
        net.addLink(h2, r1, intfName2='r0-eth2', params2={ 'ip' : '192.168.2.1/24' } )


        info( '*** Starting network\n')
        # Runs the topology and starts the network 
        net.build()

        # List of commands
        CLI(net)
        # Stops running topology
        net.stop()

# sets verbosity level for log message
if __name__ == '__main__':
        setLogLevel( 'info' )
        myNetwork()