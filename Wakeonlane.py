import socket
import binascii
import subprocess
import platform
import wakeonlan

def check_device_status(ip_address):
    """
    Check the status of a device by pinging it.
    """
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        response = subprocess.check_output(['ping', param, '1', ip_address], timeout=5)
        return True  # Device is reachable (on)
    except subprocess.CalledProcessError:
        return False  # Device is not reachable (off)
    except Exception as e:
        # Assume device is off if an error occurs
        print(f"Error occurred while checking device status: {e}")
        return False  

def send_wake_packet(server_address, mac_address):
    """
    Send a Wake-on-LAN (WoL) magic packet to wake up a device if it's off.
    """
    if not check_device_status(server_address):
        try:
            mac_address = mac_address.replace(':', '').replace('-', '').replace('.', '').replace(' ', '').upper()
            if len(mac_address) % 2 != 0:
                raise ValueError("Invalid MAC address: Odd-length string")
            soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            mac_bytes = binascii.unhexlify(mac_address)
            magic_packet = b'\xff' * 6 + mac_bytes * 16   
            soc.sendto(magic_packet, (server_address, 9))
            print("Wake-on-LAN magic packet sent to server.")
        except Exception as e:
            print(f"An error occurred while sending the Wake-on-LAN magic packet: {e}")
        finally:
            if soc:
                soc.close()
    else:
        print("Device is already on. No need to send magic packet.")

def main():
    # Configuration is required to run this script 
    server_ip = 'please enter ip address'  
    target_mac = 'please enter mac address'
    
    # Check device status
    if not check_device_status(server_ip):
        # If the device is off, send wake packet
        send_wake_packet(server_ip, target_mac)
    else:
        print("Device is already on. No need to send magic packet.")

if __name__ == "__main__":
    main()
