# 📍 Phone Number Tracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A simple Python application that analyzes phone numbers and displays their approximate geographical region on an interactive map.

Built with ❤️ by **Mr Lee**

</div>

---

# ⚠ Disclaimer

This project is intended for **educational and learning purposes only**.

It **does not track the live location** of a phone or person. It only retrieves publicly available information associated with a phone number (such as country, region, and carrier) and can display an approximate location on a map.

Always respect privacy laws and obtain permission before using this software.

---

# ✨ Features

- 📱 Analyze international phone numbers
- 🌍 Detect country and region
- 📡 Detect mobile carrier
- 🗺 Generate interactive HTML maps
- 💾 Save maps anywhere you choose
- 📜 Search history
- 🎨 Colorful terminal interface
- ⚡ Fast and lightweight
- 🖥 Works on Linux, Windows, macOS and Termux

---

# 📦 Requirements

- Python 3.8 or newer
- Git
- Internet connection

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer
```

Install dependencies

```bash
pip install phonenumbers folium opencage geocoder
```

Run

Linux/macOS

```bash
python3 main.py
```

Windows

```bash
python main.py
```

---

# 📱 Termux Installation

Update packages

```bash
pkg update && pkg upgrade
```

Install Git and Python

```bash
pkg install python git
```

Clone

```bash
git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer
```

Install dependencies

```bash
pip install phonenumbers folium opencage geocoder
```

Run

```bash
python main.py
```

---

# 🐧 Ubuntu/Debian

```bash
sudo apt update

sudo apt install python3 python3-pip git

git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer

pip3 install phonenumbers folium opencage geocoder

python3 main.py
```

---

# 🎩 Fedora/RHEL

```bash
sudo dnf install python3 python3-pip git

git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer

pip3 install phonenumbers folium opencage geocoder

python3 main.py
```

---

# 🏹 Arch Linux

```bash
sudo pacman -S python python-pip git

git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer

pip install phonenumbers folium opencage geocoder

python main.py
```

---

# 🍎 macOS

Install Homebrew if needed.

```bash
brew install python git
```

Clone

```bash
git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer
```

Install packages

```bash
pip3 install phonenumbers folium opencage geocoder
```

Run

```bash
python3 main.py
```

---

# 🪟 Windows

Install

- Python
- Git

Open Command Prompt

Clone

```bash
git clone https://github.com/Thomas-shelby001/Location-tracer.git

cd Location-tracer
```

Install dependencies

```bash
pip install phonenumbers folium opencage geocoder
```

Run

```bash
python main.py
```

---

# 📖 Usage

Launch the application.

Enter a phone number using international format.

Example

```
+14155552671

+447911123456

+254712345678
```

The program will display:

- Country
- Region
- Carrier
- Approximate coordinates
- Interactive map

---

# 💾 Saving Maps

Choose where to save your generated HTML map.

Available options:

- Current Folder
- Desktop
- Downloads
- Documents
- Custom Location

---

# 📂 Project Structure

```
Location-tracer/

├── main.py

├── README.md

├── tracking_history.json

└── location_tracker.html
```

---

# 🛠 Troubleshooting

## Module not found

```bash
pip install phonenumbers folium opencage geocoder
```

---

## Git not found

Install Git.

Linux

```bash
sudo apt install git
```

Windows

Download Git from the official website.

---

## Permission denied

```bash
chmod +x main.py
```

---

## Invalid phone number

Use the international format.

Correct

```
+254712345678
```

Wrong

```
0712345678
```

---

## Cannot open map

Linux

```bash
xdg-open location_tracker.html
```

macOS

```bash
open location_tracker.html
```

Windows

```cmd
start location_tracker.html
```

Termux

```bash
termux-open location_tracker.html
```

---

# 🔒 Privacy

- No live GPS tracking
- Data remains on your device
- History stored locally
- Open source
- No analytics

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the project

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

Licensed under the MIT License.

---

# 👨‍💻 Author

**Mr Lee**

GitHub:
https://github.com/Thomas-shelby001

---

# ⭐ Support

If you enjoyed this project,

⭐ Star the repository.

Share it with others.

Contributions are always welcome.

---

# ❓ FAQ

### Does this track live locations?

No.

It only displays information associated with the phone number.

---

### Does it work on Termux?

Yes.

---

### Does it work on Windows?

Yes.

---

### Does it work on macOS?

Yes.

---

### Does it work on Linux?

Yes.

---

### Do I need an internet connection?

Yes.

---

### Where is the map saved?

Wherever you choose.

---

### Is this project free?

Yes.

---

<div align="center">

Made with ❤️ by **Mr Lee**

</div>
