import psutil
import requests
import socket
import platform
import time
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except:
        return "Unknown"


def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unknown"


def check_internet():
    try:
        requests.get("https://google.com", timeout=5)
        return "Online"
    except:
        return "Offline"


def get_ping():
    try:
        start = time.time()
        requests.get("https://google.com", timeout=5)
        end = time.time()
        return round((end - start) * 1000)
    except:
        return "N/A"


def device_info():
    clear()

    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("=== DEVICE INFO ===\n")

    print(f"System       : {platform.system()}")
    print(f"Release      : {platform.release()}")
    print(f"Machine      : {platform.machine()}")
    print(f"CPU Cores    : {psutil.cpu_count()}")
    print(f"RAM Total    : {ram.total / (1024**3):.2f} GB")
    print(f"RAM Used     : {ram.used / (1024**3):.2f} GB")
    print(f"Storage Free : {disk.free / (1024**3):.2f} GB")

    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery      : {battery.percent}%")

    input("\nPress Enter...")


def network_info():
    clear()

    print("=== NETWORK INFO ===\n")

    print(f"Internet  : {check_internet()}")
    print(f"Local IP  : {get_local_ip()}")
    print(f"Public IP : {get_public_ip()}")
    print(f"Ping      : {get_ping()} ms")

    input("\nPress Enter...")


def live_monitor():
    try:
        while True:
            clear()

            ram = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            print("=== LIVE MONITOR ===\n")

            battery = psutil.sensors_battery()
            if battery:
                print(f"Battery : {battery.percent}%")

            print(f"RAM     : {ram.used / (1024**3):.2f}/{ram.total / (1024**3):.2f} GB")
            print(f"Storage : {disk.free / (1024**3):.2f} GB Free")
            print(f"Internet: {check_internet()}")
            print(f"Ping    : {get_ping()} ms")

            time.sleep(3)

    except KeyboardInterrupt:
        pass


while True:
    clear()

    print("""
╔══════════════════╗
║   AKE Monitor    ║
╚══════════════════╝

1. Device Info
2. Network Info
3. Live Monitor
0. Exit
""")

    choice = input("Select: ")

    if choice == "1":
        device_info()

    elif choice == "2":
        network_info()

    elif choice == "3":
        live_monitor()

    elif choice == "0":
        break