# Wake-on-LAN Automation Tool

A Python-based **Wake-on-LAN (WoL) automation tool** with **enhanced security** features, including **AES-CBC encryption** and **VPN-secured** transmission.

## Features
- ✅ Remotely power on network devices using **WoL protocol**
- 🔒 **AES-CBC encryption** for secure transmission of magic packets
- 🌐 **VPN support** for additional security
- 🔍 **Device status check** to prevent unnecessary wake-up attempts
- 🖥️ **User-friendly CLI** for easy operation

## Technologies Used
- **Python**
- **Socket Programming**
- **Cryptography Library** (for AES encryption)
- **Wake-on-LAN Module**
- **subprocess Module** (for system interaction)

## Installation
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo/wake-on-lan-tool.git
   cd wake-on-lan-tool
2. Install Dependencies : Ensure Python is installed on your system.
   
### Usage
1. **Standard Wake-on-LAN**
Run the Wakeonlane.py script to send a WoL magic packet to a target device.
NOTE: Before running, update the script with your device details:
server_ip = 'ENTER_DEVICE_IP'
target_mac = 'ENTER_DEVICE_MAC
2.**Secure Wake-on-LAN over VPN**
Run the WakeonLane_VPN.py script for encrypted and VPN-secured transmission.
NOTE: Before running, update the script with your network details:
server_ip = 'ENTER_DEVICE_IP'
target_mac = 'ENTER_DEVICE_MAC'
key = b'YOUR_ENCRYPTION_KEY'
destination_ip = 'VPN_DESTINATION_IP'
destination_port = 9

**Notes**
The target device must support Wake-on-LAN (WoL) in BIOS settings.
Ensure WoL is enabled in the OS network adapter settings.
If using VPN, configure it before running the script.
**Disclaimer**
This project is for educational and demonstration purposes only.
Use responsibly and only on authorized devices.
