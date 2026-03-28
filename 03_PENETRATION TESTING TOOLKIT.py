import socket
import threading

# ------------------ PORT SCANNER ------------------ #
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"✅ Port {port} is OPEN")
        
        sock.close()
    except:
        pass


def port_scanner():
    target = input("Enter target IP (example: 127.0.0.1): ")

    print("\nScanning common ports...\n")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

    threads = []

    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✔ Scan completed\n")


# ------------------ BRUTE FORCE DEMO ------------------ #
def brute_force():
    print("\n[+] Starting Brute Force Demo\n")

    correct_password = "admin123"
    password_list = ["1234", "admin", "password", "root", "admin123"]

    for password in password_list:
        print(f"Trying password: {password}")

        if password == correct_password:
            print(f"\n✅ Password found: {password}")
            return

    print("\n❌ Password not found")


# ------------------ MAIN MENU ------------------ #
def main():
    while True:
        print("\n===== PENETRATION TESTING TOOLKIT =====")
        print("1. Port Scanner")
        print("2. Brute Force Demo")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_force()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()