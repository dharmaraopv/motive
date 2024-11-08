def is_valid_subnet(subnet):
    if len(subnet) == 0:
        return False
    if subnet[0] == '0' and len(subnet) > 1:
        return False
    if int(subnet) > 255:
        return False
    return True
def get_possible_subnets(level, substring):
    if level == 3:
        if len(substring) > 3:
            return []
        else:
            if is_valid_subnet(substring):
                return [substring]
            else:
                return []
    else:
        result = []
        for i in range(1,4):
            if is_valid_subnet(substring[:i]):
                result += [substring[:i] + '.' + x for x in get_possible_subnets(level + 1, substring[i:])]
        return result

def possible_ips(s):
    return get_possible_subnets(0, s)


valid_ips = ['19216811',
 '17216255255',
 '1250255',
 '19202',
 '1011001',
 '1921681010',
 '1234',
 '100254254',
 '172161616',
 '1921681254',
 '12711',
 '255255255255',
 '192168100100',
 '12811',
 '19851100200',
 '3444',
 '30016811',
 '1921682561',
 '1921681256',
 '192168110',
 '16811',
 '1256256'
]

invalid_ips = [
 ''
 '10000001',
 '1920128000',
 '888',
 '11',
 '192168300300',
 '256256256256',
 '999999999999',
 '19216255256',
 '123456789012',
 '10256256256',
 '50000001',
 '3400500',
 '1025625600',
 '192000192192',
 '9991681680',
 '500500500500',
 '1256256256',
 '192169192256'
]

print("Valid IPs")
for ip in valid_ips:
    print(possible_ips(ip))
print("Invalid IPs")
for ip in invalid_ips:
    print(possible_ips(ip))
