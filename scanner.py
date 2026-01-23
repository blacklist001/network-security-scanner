import nmap

scanner = nmap.PortScanner()

target = input("Enter target IP: ")
print("Scanning target...")

scanner.scan(target, '1-1024', arguments='-sV')


risky_ports = {
    21: "FTP - Often insecure",
    22: "SSH - Brute force risk",
    23: "Telnet - Very insecure",
    80: "HTTP - Unencrypted traffic",
    445: "SMB - Common attack target"
}

for host in scanner.all_hosts():
    print(f"\nHost: {host}")

    for proto in scanner[host].all_protocols():
        for port in scanner[host][proto]:
            state = scanner[host][proto][port]['state']
            print(f"Port {port}: {state}")

            if port in risky_ports and state == "open":
                print(f" ⚠ Risk: {risky_ports[port]}")
