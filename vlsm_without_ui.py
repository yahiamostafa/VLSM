import math
import ipaddress

def calculate_vlsm(networkAddress , hosts):
        # get network address and prefix
        networkAddress , prefix = networkAddress.split("/")

        # network address as an ip Object
        networkIP = ipaddress.IPv4Address(networkAddress)

        # get the four octets in the network address
        ip = list(map(int ,networkAddress.split(".")))

        # get hosts 
        hosts = list(map(int ,hosts.split(",")))

        # get the number of subnets required
        number_of_subents = len(hosts)

        # sort the number of hosts from the highest to the lowest 
        hosts.sort(reverse = True)

        # make a table to save values (the 4 well known ips)
        table = []

        for host in hosts:
            
            # get the number of bits required for this subnet
            number_of_bits = math.ceil(math.log2(host + 2))
            
            # get the first Usable IP Address
            first_usable_ip_add = networkIP + 1

            # get the broadcast ip Address
            broadcast_ip_add = networkIP + 2 ** number_of_bits  - 1

            # get the last Usable IP Address
            last_usable_ip_add = broadcast_ip_add - 1

            # wasted IP addresses
            wasted_addresses = 2 ** number_of_bits - host

            # create a list contains the 4 famous IPs
            IPs = [host , networkIP , first_usable_ip_add , last_usable_ip_add , broadcast_ip_add , 32 - number_of_bits , wasted_addresses]

            # add the IPs to the table
            table.append(IPs)

            # update the network IP
            networkIP += 2 ** number_of_bits
            
            print(IPs)

calculate_vlsm("192.168.1.0/24" , "15,68,45")
