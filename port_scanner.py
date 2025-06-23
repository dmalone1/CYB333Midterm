import socket
import time

def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
    except socket.gaierror:
        print(f"[ERROR] Hostname '{host}' could not be resolved.")
        return None
    except Exception as e:
        print(f"[ERROR] Exception occurred while scanning port {port}: {e}")
        return None

def scan_ports():
    print("🔍 Simple Python Port Scanner")
    host = input("Enter host to scan (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()
    
    try:
        choice = input("Scan common ports (21, 22, 80, 443)? (y/n): ").strip().lower()
        if choice == 'y':
            ports = [21, 22, 80, 443]
        else:
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            if start_port < 0 or end_port > 65535 or start_port > end_port:
                raise ValueError("Invalid port range.")
            ports = range(start_port, end_port + 1)
    except ValueError as ve:
        print(f"[ERROR] Invalid input: {ve}")
        return
    
    print(f"\nScanning {host} on ports: {list(ports)}\n")
    time.sleep(1)

    for port in ports:
        status = scan_port(host, port)
        if status is True:
            print(f"[OPEN] Port {port} is open.")
        elif status is False:
            print(f"[CLOSED] Port {port} is closed.")
        else:
            print(f"[SKIPPED] Port {port} could not be scanned.")

        time.sleep(0.2)  # Ethical delay between scans

if __name__ == "__main__":
    scan_ports()



      