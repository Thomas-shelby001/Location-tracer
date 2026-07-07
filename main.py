#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████  ██░ ██  ▒█████   ███▄    █  ▒███████▒             ║
║   ▒██    ▒ ▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▒ ▒ ▒ ▄▀░             ║
║   ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒░ ▒ ▄▀▒░              ║
║     ▒   ██▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒  ▄▀▒   ░             ║
║   ▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██░   ▓██░▒███████▒             ║
║   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒▒ ▓░▒░             ║
║   ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ▒ ░ ░             ║
║   ░  ░  ░   ░  ░░ ░░ ░ ░ ▒     ░   ░ ░ ░ ░   ░             ║
║         ░   ░  ░  ░    ░ ░           ░     ░                ║
║                                                              ║
║   ████████ ██▀███   ▄▄▄       ▄████▄  ██ ▄█▀ ███████       ║
║   ╚══██    ▓██ ▒ ██▒████▄    ▒██▀ ▀█  ██▄█▒ ▒██             ║
║      ██    ▓██ ░▄█ ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ███            ║
║      ██    ▒██▀▀█▄ ▒██▄▄▄█▄ ▒▓▓▄ ▄██▒▓██ █▄ ▓██             ║
║      ██    ░██▓ ▒██▒░ ▒░▒░▒░ ▒ ▓███▀ ░▒██▒ █▄░ ███████      ║
║      ░░    ░ ▒▓ ░▒▓░  ░ ▒ ▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒░ ░░      ║
║           ░▒ ░ ▒░  ░ ░ ▒    ░  ▒    ░ ░▒ ▒░ ░ ░  ░      ║
║           ░░   ░     ░ ░  ░        ░ ░░ ░    ░         ║
║            ░                    ░          ░    ░         ║
║                                                              ║
║                  📍 PHONE NUMBER TRACKER                     ║
║                     Version 2.0.0                           ║
║                                                              ║
║              🔒 Use Responsibly & With Consent               ║
║                                                              ║
║                   Made with ❤️ by Mr Lee                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

import phonenumbers
import folium
import os
import sys
import webbrowser
import time
import platform
import json
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
from datetime import datetime
from pathlib import Path


API_KEY = "8ee962a0b6af4c848bf4b0bf3669ea8c"

VERSION = "1.0.0"
AUTHOR = "Mr Lee"
GITHUB = "https://github.com/Thomas-shelby001/Location-tracer"


class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    WHITE = '\033[97m'

    @staticmethod
    def disable():
        if platform.system() == "Windows":
            Colors.GREEN = Colors.YELLOW = Colors.RED = Colors.BLUE = ""
            Colors.CYAN = Colors.PURPLE = Colors.BOLD = Colors.RESET = ""
            Colors.WHITE = ""

if platform.system() == "Windows":
    Colors.disable()

# ===== FUNCTIONS =====

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██████  ██░ ██  ▒█████   ███▄    █  ▒███████▒                 ║
║   ▒██    ▒ ▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▒ ▒ ▒ ▄▀░                 ║
║   ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒░ ▒ ▄▀▒░                  ║
║     ▒   ██▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒  ▄▀▒   ░                 ║
║   ▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██░   ▓██░▒███████▒                 ║
║   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒▒ ▓░▒░                 ║
║   ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ▒ ░ ░                 ║
║   ░  ░  ░   ░  ░░ ░░ ░ ░ ▒     ░   ░ ░ ░ ░   ░                 ║
║         ░   ░  ░  ░    ░ ░           ░     ░                    ║
║                                                                  ║
║   ████████ ██▀███   ▄▄▄       ▄████▄  ██ ▄█▀ ███████           ║
║   ╚══██    ▓██ ▒ ██▒████▄    ▒██▀ ▀█  ██▄█▒ ▒██                 ║
║      ██    ▓██ ░▄█ ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ███                ║
║      ██    ▒██▀▀█▄ ▒██▄▄▄█▄ ▒▓▓▄ ▄██▒▓██ █▄ ▓██                 ║
║      ██    ░██▓ ▒██▒░ ▒░▒░▒░ ▒ ▓███▀ ░▒██▒ █▄░ ███████          ║
║      ░░    ░ ▒▓ ░▒▓░  ░ ▒ ▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒░ ░░          ║
║           ░▒ ░ ▒░  ░ ░ ▒    ░  ▒    ░ ░▒ ▒░ ░ ░  ░          ║
║           ░░   ░     ░ ░  ░        ░ ░░ ░    ░             ║
║            ░                    ░          ░    ░             ║
║                                                                  ║
║{Colors.YELLOW}                  📍 PHONE NUMBER TRACKER                     {Colors.CYAN}║
║{Colors.WHITE}                     Version {VERSION}                           {Colors.CYAN}║
║                                                                  ║
║{Colors.RED}              🔒 Use Responsibly & With Consent               {Colors.CYAN}║
║                                                                  ║
║{Colors.GREEN}                   Made with ❤️ by {AUTHOR}                     {Colors.CYAN}║
║{Colors.PURPLE}                   GitHub: {GITHUB}                         {Colors.CYAN}║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def loading_animation(message="Processing", duration=1):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for i in range(int(duration * 10)):
        sys.stdout.write(f'\r{Colors.CYAN}{chars[i % len(chars)]} {message}...{Colors.RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\r' + ' ' * 50 + '\r', end='')

def select_save_location():
    """Let user select where to save the map file"""
    print(f"\n{Colors.YELLOW}📁 SELECT SAVE LOCATION:{Colors.RESET}")
    print(f"{Colors.CYAN}1.{Colors.RESET} Current directory (./)")
    print(f"{Colors.CYAN}2.{Colors.RESET} Documents folder")
    print(f"{Colors.CYAN}3.{Colors.RESET} Downloads folder")
    print(f"{Colors.CYAN}4.{Colors.RESET} Desktop")
    print(f"{Colors.CYAN}5.{Colors.RESET} Custom path")
    
    choice = input(f"\n{Colors.GREEN}Enter your choice (1-5): {Colors.RESET}").strip()
    
    if choice == '1':
        return os.getcwd()
    elif choice == '2':
        return str(Path.home() / "Documents")
    elif choice == '3':
        return str(Path.home() / "Downloads")
    elif choice == '4':
        return str(Path.home() / "Desktop")
    elif choice == '5':
        custom = input(f"{Colors.GREEN}Enter full path: {Colors.RESET}").strip()
        if os.path.exists(custom):
            return custom
        else:
            print(f"{Colors.RED}❌ Path doesn't exist! Using current directory.{Colors.RESET}")
            return os.getcwd()
    else:
        print(f"{Colors.YELLOW}⚠️  Invalid choice! Using current directory.{Colors.RESET}")
        return os.getcwd()

def validate_phone(number):
    try:
        parsed = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(parsed):
            return None, f"{Colors.RED}❌ Invalid phone number{Colors.RESET}"
        return parsed, None
    except phonenumbers.NumberParseException:
        return None, f"{Colors.RED}❌ Invalid format! Use: +[countrycode][number]{Colors.RESET}"
    except Exception as e:
        return None, f"{Colors.RED}❌ Error: {e}{Colors.RESET}"

def get_location_info(parsed_number):
    try:
        loading_animation("Getting location info", 1.5)
        
        location = geocoder.description_for_number(parsed_number, "en")
        if not location:
            location = "Unknown location"
        
        carrier_name = carrier.name_for_number(parsed_number, "en")
        if not carrier_name:
            carrier_name = "Unknown carrier"
        
        country = geocoder.region_name_for_number(parsed_number, "en")
        if not country:
            country = "Unknown country"
        
        return {
            'location': location,
            'carrier': carrier_name,
            'country': country,
            'valid': True,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, None
        
    except Exception as e:
        return None, f"{Colors.RED}❌ Error getting info: {e}{Colors.RESET}"

def get_coordinates(location):
    try:
        loading_animation("Fetching coordinates", 1.5)
        
        geocoder_api = OpenCageGeocode(API_KEY)
        results = geocoder_api.geocode(location)
        
        if not results:
            return None, None, f"{Colors.RED}❌ Could not find coordinates{Colors.RESET}"
        
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return lat, lng, None
        
    except Exception as e:
        return None, None, f"{Colors.RED}❌ Geocoding error: {e}{Colors.RESET}"

def create_map(lat, lng, location, phone_number, carrier_name, save_path):
    try:
        loading_animation("Creating map", 1)
        
        my_map = folium.Map(
            location=[lat, lng],
            zoom_start=13,
            tiles='OpenStreetMap'
        )
        
        popup_html = f"""
        <div style="font-family: 'Segoe UI', Arial; padding: 15px; min-width: 250px;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; padding: 10px; border-radius: 8px; margin-bottom: 10px;">
                <h4 style="margin: 0;">📍 Location Found!</h4>
            </div>
            <div style="padding: 5px 0;">
                <p><b>📱 Number:</b><br> <span style="color: #667eea;">{phone_number}</span></p>
                <p><b>📍 Location:</b><br> {location}</p>
                <p><b>📡 Carrier:</b><br> {carrier_name}</p>
                <p><b>🌍 Coordinates:</b><br> {lat:.6f}, {lng:.6f}</p>
                <hr>
                <small style="color: #999;">🔒 For educational purposes only</small>
            </div>
        </div>
        """
        
        folium.Marker(
            [lat, lng],
            popup=folium.Popup(popup_html, max_width=350),
            icon=folium.Icon(color='red', icon='phone-alt', prefix='fa')
        ).add_to(my_map)
        
        folium.Circle(
            radius=1500,
            location=[lat, lng],
            popup='📍 Approximate Area',
            color='#667eea',
            fill=True,
            fill_color='#667eea',
            fill_opacity=0.2
        ).add_to(my_map)
        
        folium.plugins.Fullscreen().add_to(my_map)
        folium.plugins.MousePosition().add_to(my_map)
        
        filename = "location_tracker.html"
        full_path = os.path.join(save_path, filename)
        my_map.save(full_path)
        return full_path, None
        
    except Exception as e:
        return None, f"{Colors.RED}❌ Error creating map: {e}{Colors.RESET}"

def open_map(filepath):
    try:
        if platform.system() == 'Windows':
            os.startfile(filepath)
        else:
            webbrowser.open(f'file://{filepath}')
        return True, None
    except Exception as e:
        return False, f"{Colors.RED}❌ Could not open browser: {e}{Colors.RESET}"

def display_info(info, phone_number):
    print(f"\n{Colors.YELLOW}{'='*50}{Colors.RESET}")
    print(f"{Colors.GREEN}📍 LOCATION INFORMATION{Colors.RESET}")
    print(f"{Colors.YELLOW}{'='*50}{Colors.RESET}")
    print(f"{Colors.CYAN}📱 Number:{Colors.RESET} {Colors.WHITE}{phone_number}{Colors.RESET}")
    print(f"{Colors.CYAN}📍 Location:{Colors.RESET} {Colors.WHITE}{info['location']}{Colors.RESET}")
    print(f"{Colors.CYAN}🌍 Country:{Colors.RESET} {Colors.WHITE}{info['country']}{Colors.RESET}")
    print(f"{Colors.CYAN}📡 Carrier:{Colors.RESET} {Colors.WHITE}{info['carrier']}{Colors.RESET}")
    print(f"{Colors.CYAN}🕐 Time:{Colors.RESET} {Colors.WHITE}{info['timestamp']}{Colors.RESET}")
    print(f"{Colors.YELLOW}{'='*50}{Colors.RESET}")

def save_history(data):
    try:
        history_file = "tracking_history.json"
        history = []
        
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
        
        history.append(data)
        
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=2)
            
        return True
    except:
        return False

def view_history():
    try:
        history_file = "tracking_history.json"
        if not os.path.exists(history_file):
            print(f"{Colors.YELLOW}No history found{Colors.RESET}")
            return
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        print(f"\n{Colors.GREEN}📜 TRACKING HISTORY ({len(history)} records){Colors.RESET}")
        print(f"{Colors.YELLOW}{'='*50}{Colors.RESET}")
        
        for i, entry in enumerate(history[-10:], 1):
            print(f"{Colors.CYAN}{i}. {entry.get('timestamp', 'Unknown')}{Colors.RESET}")
            print(f"   📱 {entry.get('number', 'Unknown')}")
            print(f"   📍 {entry.get('location', 'Unknown')}")
            print()
            
        if len(history) > 10:
            print(f"{Colors.YELLOW}Showing last 10 of {len(history)} records{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}Error reading history: {e}{Colors.RESET}")

# ===== MAIN PROGRAM =====

def main():
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}📌 INSTRUCTIONS:{Colors.RESET}")
    print("   • Enter phone number with country code")
    print("   • Example: +1234567890 (US)")
    print("   • Example: +447911123456 (UK)")
    print("   • Example: +919876543210 (India)")
    print("   • Type 'history' to view past searches")
    print("   • Type 'q' or 'quit' to exit")
    print(f"{Colors.YELLOW}{'-'*50}{Colors.RESET}")
    
    # Select save location once at start
    save_path = select_save_location()
    print(f"{Colors.GREEN}✅ Files will be saved to: {save_path}{Colors.RESET}")
    
    while True:
        try:
            # Get phone number from user
            print(f"\n{Colors.CYAN}📱 Enter phone number:{Colors.RESET} ", end='')
            phone_number = input().strip()
            
            # Check for special commands
            if phone_number.lower() in ['q', 'quit', 'exit']:
                print(f"\n{Colors.GREEN}👋 Goodbye! Thanks for using!{Colors.RESET}")
                print(f"{Colors.PURPLE}Made with ❤️ by {AUTHOR}{Colors.RESET}")
                sys.exit(0)
            
            if phone_number.lower() == 'history':
                view_history()
                continue
            
            if not phone_number:
                print(f"{Colors.RED}❌ Please enter a phone number!{Colors.RESET}")
                continue
            
            # Validate number
            parsed_number, error = validate_phone(phone_number)
            if error:
                print(error)
                continue
            
            # Get location info
            info, error = get_location_info(parsed_number)
            if error:
                print(error)
                continue
            
            # Display info
            display_info(info, phone_number)
            
            # Get coordinates
            lat, lng, error = get_coordinates(info['location'])
            if error:
                print(error)
                continue
            
            print(f"{Colors.GREEN}✅ Coordinates found: {Colors.WHITE}{lat:.6f}, {lng:.6f}{Colors.RESET}")
            
            # Create map
            filepath, error = create_map(lat, lng, info['location'], phone_number, info['carrier'], save_path)
            if error:
                print(error)
                continue
            
            print(f"{Colors.GREEN}✅ Map saved: {Colors.WHITE}{filepath}{Colors.RESET}")
            
            # Save to history
            history_data = {
                'number': phone_number,
                'location': info['location'],
                'country': info['country'],
                'carrier': info['carrier'],
                'coordinates': f"{lat:.6f}, {lng:.6f}",
                'timestamp': info['timestamp']
            }
            save_history(history_data)
            
            # Ask to open map
            print(f"\n{Colors.CYAN}🌐 Open map in browser? (y/n):{Colors.RESET} ", end='')
            open_now = input().strip().lower()
            if open_now in ['y', 'yes']:
                success, error = open_map(filepath)
                if success:
                    print(f"{Colors.GREEN}✅ Map opened in browser{Colors.RESET}")
                else:
                    print(error)
                    print(f"{Colors.YELLOW}📁 Open '{filepath}' manually{Colors.RESET}")
            
            # Ask to continue or exit
            print(f"\n{Colors.CYAN}🔄 Track another number? (y/n):{Colors.RESET} ", end='')
            again = input().strip().lower()
            if again not in ['y', 'yes']:
                print(f"\n{Colors.GREEN}👋 Thanks for using!{Colors.RESET}")
                print(f"{Colors.GREEN}Made with ❤️ by {AUTHOR}{Colors.RESET}")
                break
            
            clear_screen()
            print_banner()
            print(f"{Colors.GREEN}📁 Files saved to: {save_path}{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.GREEN}👋 Goodbye!{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.RED}❌ Unexpected error: {e}{Colors.RESET}")
            print(f"{Colors.YELLOW}Try again or report on GitHub{Colors.RESET}")

# ===== DEPENDENCY CHECK =====

def check_dependencies():
    missing = []
    packages = ['phonenumbers', 'folium', 'opencage']
    
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    
    if missing:
        print(f"{Colors.RED}❌ Missing dependencies: {', '.join(missing)}{Colors.RESET}")
        print(f"\n{Colors.YELLOW}📦 Install with:{Colors.RESET}")
        print(f"   pip install {' '.join(missing)}")
        print(f"\n{Colors.YELLOW}For Termux:{Colors.RESET}")
        print("   pkg install python")
        print(f"   pip install {' '.join(missing)}")
        sys.exit(1)
    
    return True

# ===== RUN PROGRAM =====

if __name__ == "__main__":
    try:
        check_dependencies()
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}👋 Goodbye!{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        sys.exit(1)
