import socket

def get_router_ip():
    # Specify the DNS server you want to query
    dns_server = 'http://190.104.12.43/'  # Google's Public DNS server

    # Specify the hostname of your router
    router_hostname = 'hitronhub.home'  # Replace with your router's hostname

    # Query the DNS server for the IP address of the router's hostname
    try:
        router_ip = socket.gethostbyname(router_hostname)
        return router_ip
    except socket.gaierror as e:
        print("Failed to resolve hostname. Error:", e)
        return None

if __name__ == "__main__":
    router_ip = get_router_ip()
    if router_ip:
        print("Router IP Address:", router_ip)
    else:
        print("Failed to retrieve the router's IP address.")
