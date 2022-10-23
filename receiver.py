"""Klient prijimajici multicast notifikace o prubehu zvoneni"""
from MulticastHelper import MulticastHelper

if __name__ == '__main__':
    # Choose an arbitrary multicast IP and port.
    # 239.255.0.0 - 239.255.255.255 are for local network multicast use.
    # Remember, you subscribe to a multicast IP, not a port. All data from all ports
    # sent to that multicast IP will be echoed to any subscribed machine.
    multicast_address = "239.0.0.0"
    multicast_port = 6138

    # When launching this example, you can choose to put it in listen or announce mode.
    # Announcing doesn't require binding to a port, but we do it here just to reuse code.
    # It binds to the requested port + 1, allowing you to run the announce and listen modes
    # on the same machine at the same time.

    # In a real case, you'll most likely send and receive from the same port using Gevent or Twisted,
    # so the code in create_socket() will apply more directly.

    helper = MulticastHelper(multicast_address, multicast_port)
    helper.listen_loop()
