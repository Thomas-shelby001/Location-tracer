# 📍 Phone Number Tracker

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-lightgrey)
![Version](https://img.shields.io/badge/Version-2.0.0-brightgreen)

> **Track phone number locations with interactive maps**  
> *Made with ❤️ by Mr Lee*

</div>

---

## ⚠️ **DISCLAIMER**

> **IMPORTANT**: This tool is for **EDUCATIONAL PURPOSES ONLY**.  
> Tracking phone numbers without explicit consent is **ILLEGAL** in most countries.  
> **Use responsibly and only with permission!**

---

## ✨ Features

- 📍 **Location Tracking** - Get geographical location from phone numbers
- 📡 **Carrier Detection** - Identify mobile service providers
- 🗺️ **Interactive Maps** - Generate beautiful HTML maps with markers
- 💾 **Auto-Save** - Maps automatically saved to your chosen storage
- 🎨 **Colorful CLI** - Beautiful terminal output with colors
- 🔄 **Cross-Platform** - Works on Linux, Windows, macOS, and Termux
- 📱 **Storage Selection** - Choose where to save location.html
- 🔍 **History Log** - View all previous searches

---

## 📋 **Requirements**

- Python 3.6 or higher
- Internet connection (for OpenCage API)
- OpenCage API key (free from opencagedata.com)

---

## 🔑 **Getting API Key**

1. Go to [OpenCage Geocoder](https://opencagedata.com/)
2. Sign up for a **FREE** account
3. Get your API key from the dashboard
4. Replace `YOUR_API_KEY_HERE` in `main.py` with your key

---

## 🚀 **Installation Instructions**

### 📱 **Termux (Android)**

```bash
# Step 1: Update packages
pkg update && pkg upgrade

# Step 2: Install Python
pkg install python

# Step 3: Install required packages
pip install phonenumbers folium opencage geocoder

# Step 4: Download the script
curl -O https://raw.githubusercontent.com/mrlee/phone-tracker/main/main.py

# Step 5: Run the script
python main.py
