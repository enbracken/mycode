#!/usr/bin/env python3
""" Shebang lint to run program in python 3"""

# Define lists
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

# Print list for confirmation
print(proto)

# Append "dns" to each list
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

# Demonstrate difference between extend and append of sub-list
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

