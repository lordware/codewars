import ipaddress
ips_between = lambda x, y: int(ipaddress.IPv4Address(y)) - int(ipaddress.IPv4Address(x))