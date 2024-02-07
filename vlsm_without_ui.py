import math
import ipaddress

def calculate_vlsm(networkAddress , hosts):
        networkAddress , prefix = networkAddress.split("/")

        networkIP = ipaddress.IPv4Address(networkAddress)

        ip = list(map(int ,networkAddress.split(".")))

        hosts = list(map(int ,hosts.split(",")))
        number_of_subents = len(hosts)

        # sort the number of hosts from the highest to the lowest 
        hosts.sort(reverse = True)

        # make a table to save values (the 4 well known ips)
        # (Network_IP , First_Usable_IP , Last_Usable_IP, broadcastIP)
        table = []

        for host in hosts:
            
            number_of_bits = math.ceil(math.log2(host + 2))
            
            first_usable_ip_add = networkIP + 1
                
            broadcast_ip_add = networkIP + 2 ** number_of_bits  - 1
            last_usable_ip_add = broadcast_ip_add - 1

            wasted_addresses = 2 ** number_of_bits - host
            IPs = [host , networkIP , first_usable_ip_add , last_usable_ip_add , broadcast_ip_add , 32 - number_of_bits , wasted_addresses]

            table.append(IPs)
            networkIP += 2 ** number_of_bits
            
            print(IPs)

calculate_vlsm("192.168.1.0/24" , "15,68,45")
