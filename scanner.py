import socket
target = input("\nenter the target ip address or domain name:")
ports = [21, 22, 23, 25, 53, 80, 443]
port_names = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}
print(f"\nscanning  {target}........\n")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} ({port_names[port]}) is open")
    else:
        print(f"Port {port} ({port_names[port]}) is closed")
    s.close()
