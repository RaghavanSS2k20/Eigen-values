import socket

# Get the hostname
def get_ip():
    hostname = socket.gethostname()

    # Get the IP address
    ip_address = socket.gethostbyname(hostname)

    return {'ip':ip_address}
