# Author: Sambuddha Basu
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink

switches = []
hosts = []
even_hosts = []
odd_hosts = []

class MyTopo(Topo):
	def __init__(self, **opts):
		Topo.__init__(self, **opts)
		num_switches = input('Enter number of switches: ')
		total_hosts = 0
		for x in range(num_switches):
			switch = self.addSwitch('s' + str(x))
			switches.append(switch)
			num_hosts = input('Enter number of hosts for switch(s' + str(x) + '): ')
			temp_hosts = []
			for y in range(num_hosts):
				if total_hosts % 2 == 0:
					# 10.0.0.1/24 subnet for even hosts
					host = self.addHost('h' + str(total_hosts), ip='10.0.0.' + str(total_hosts/2 + 1))
					even_hosts.append(host)
				else:
					# 192.168.0.1/24 subnet for odd hosts
					host = self.addHost('h' + str(total_hosts), ip='192.168.0.' + str(total_hosts/2 + 1))
					odd_hosts.append(host)
				temp_hosts.append(host)
				total_hosts += 1
			hosts.append(temp_hosts)

		for x in range(len(switches)):
			for y in range(len(hosts[x])):
				host_num = int(hosts[x][y][1:])
				if host_num % 2 == 0:
					self.addLink(hosts[x][y], switches[x], bw=2)
				else:
					self.addLink(hosts[x][y], switches[x], bw=1)

		for x in range(len(switches)-1):
			self.addLink(switches[x], switches[x+1])


if __name__ == '__main__':
	topo = MyTopo()
	net = Mininet(topo=topo, controller=OVSController, link=TCLink)
	net.start()
	net.pingAll()
	if len(even_hosts) > 1:
		print "Testing bandwidth for even hosts...(should be 2.00 Mbits/sec)"
		check_even_hosts = []
		for x in even_hosts:
			check_even_hosts.append(net.getNodeByName(x))
		h0 = check_even_hosts[0]
		h2 = check_even_hosts[1]
		net.iperf((h0, h2))
	if len(odd_hosts) > 1:
		print "Testing bandwidth for odd hosts...(should be 1.00 Mbits/sec)"
		check_odd_hosts = []
		for x in odd_hosts:
			check_odd_hosts.append(net.getNodeByName(x))
		h1 = check_odd_hosts[0]
		h3 = check_odd_hosts[1]
		net.iperf((h1, h3))
	net.stop()
