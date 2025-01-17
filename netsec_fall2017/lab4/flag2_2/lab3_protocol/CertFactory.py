import os


key_dir = os.path.expanduser("~/NetSec_TeamProject/netsec_fall2017/lab4/flag2/sign/")
my_key_path = key_dir + "my.key"
cli_key_path = key_dir + "client.key"
server_key_path = key_dir + "server.key"
flag2_key_path = key_dir + "flag2.key" # 20174.1.11.2


cert_dir = os.path.expanduser("~/NetSec_TeamProject/netsec_fall2017/lab4/flag2/sign/")
root_cert_path = cert_dir + "root.crt" # 20174.1
my_cert_path = cert_dir + "my.crt" # 20174.1.11
cli_cert_path = cert_dir + "client.crt" # 20174.1.11.1
server_cert_path = cert_dir + "server.crt" # 20174.1.11.2
flag2_cert_path = cert_dir + "flag2.crt" # 20174.1.11.2

cert_dict = {
    "20174.1":root_cert_path,
    "20174.1.11":my_cert_path,
    "20174.1.11.1":cli_cert_path,
    "20174.1.11.2":server_cert_path,
    "20174.1.22.1":flag2_cert_path,
}

key_dict = {
    "20174.1.11":my_key_path,
    "20174.1.11.1":cli_key_path,
    "20174.1.11.2":server_key_path,
    "20174.1.22.1":flag2_key_path,
}


def getPrivateKeyForAddr(addr):
    addr = key_dict[addr]
    with open(addr) as fp:
        private_key_user = fp.read()
    return private_key_user.encode()

def getCertsForAddr(addr):
    #addr1 = cert_dict[addr]
    #addr1 = cert_dict["20174.1.22.1"]
    addr1 = None
    addr2 = None
    #addr2 = cert_dict["20174.1.11.1"]
    with open(addr1) as fp:
        certs_user1 = fp.read()
    with open(addr2) as fp:
        certs_user2 = fp.read()
    return [certs_user1.encode(), certs_user2.encode()]

def getRootCert(addr):
    addr = cert_dict[addr]
    with open(addr) as fp:
        root_cert_user = fp.read()
    return root_cert_user.encode()
