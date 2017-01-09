import ipaddress
import random

def get_random_ip():
    '''
    Get a random IP address
    :return: rand_ip
    '''

    rand_ip = []
    begin_ip = ["10", "172", "198"]
    # Random Number between 1 and 255
    rand_ip.insert(0, random.choice(begin_ip))

    if rand_ip[0] == "10":
        rand_insert
        for i in range(1, 2):
            rand_ip.insert(i, str(0))

    rand_ip.insert(3, "0")
    return ".".join(rand_ip)



def get_subnet(ip_addr):
    """
    Get the subnet mask
    :return: subnet
    """
    if ip_addr.startswith("10."):
        return str(random.randrange(5, 13))
    elif ip_addr.startswith("172."):
        return str(random.randrange(13,23))
    elif ip_addr.startswith("192."):
        return str(random.randrange(19, 31))

def subnetcalc(ip):
    """
    Calcuate the subnet mask given the network address and subnet mask
    :param ip:
    :param sub:
    :return:
    """
    hosts = list(ipaddress.ip_network(ip).hosts())
    print(hosts)


def validate(answer):
    """
    Validates whether the right answer was given
    :param answer:
    :return:
    """


def ask_question():
    """
    Ask the user the subnet question
    :return:
    """
    ip_addr = get_random_ip()
    subnet = get_subnet(ip_addr)
    print(subnet)
    question = ip_addr + "/" + subnet
    print(question)

    """
    print("Hello, your question is: %s" % question)
    answer = input("\nWhat is the first address in the second subnet?")

    """
    correct_response = subnetcalc(question)
    print(correct_response)

ask_question()



