import os
import urllib.request
import socket

# Set a timeout so we don't hang
socket.setdefaulttimeout(10)

# All icons from ShizukuIchi/winXP GitHub repo (small PNGs, fast to download)
BASE = "https://raw.githubusercontent.com/ShizukuIchi/winXP/master/src/assets/windowsIcons/"

icons = {
    # 32x32 Desktop icons
    "computer.png": BASE + "318(32x32).png",
    "notepad.png": BASE + "327(32x32).png",
    "ie.png": BASE + "220(32x32).png",
    "minesweeper.png": BASE + "309(32x32).png",
    "sudoku.png": BASE + "315(32x32).png",
    "doom.png": BASE + "912(32x32).png",
    "network.png": BASE + "894(32x32).png",
    "avatar.png": BASE + "853(32x32).png",
    "log_off.png": BASE + "313(32x32).png",
    "turn_off.png": BASE + "312(32x32).png",
    "my_documents.png": BASE + "302(32x32).png",
    "my_pictures.png": BASE + "147(32x32).png",

    # 16x16 for title bars and tray
    "computer_16.png": BASE + "318(16x16).png",
    "notepad_16.png": BASE + "327(16x16).png",
    "ie_16.png": BASE + "220(16x16).png",
    "minesweeper_16.png": BASE + "309(16x16).png",
    "sudoku_16.png": BASE + "315(16x16).png",
    "doom_16.png": BASE + "912(16x16).png",
    "network_16.png": BASE + "894(16x16).png",
    "security_16.png": BASE + "74(16x16).png",
    "projects_16.png": BASE + "318(16x16).png",
    "tech_stack_16.png": BASE + "227(16x16).png",
    "all_programs_16.png": BASE + "354(16x16).png",
    "control_panel_16.png": BASE + "227(16x16).png",
    "printers_16.png": BASE + "128(16x16).png",
    "help_16.png": BASE + "300(16x16).png",
    "search_16.png": BASE + "890(16x16).png",
    "run_16.png": BASE + "234(16x16).png",
    "my_documents_16.png": BASE + "302(16x16).png",
    "my_pictures_16.png": BASE + "147(16x16).png",
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

os.makedirs('xp-icons', exist_ok=True)

success = 0
fail = 0
for name, url in icons.items():
    path = os.path.join('xp-icons', name)
    if os.path.exists(path) and os.path.getsize(path) > 100:
        print(f"SKIP {name} (already exists)")
        success += 1
        continue
    print(f"GET  {name}...", end=" ", flush=True)
    try:
        urllib.request.urlretrieve(url, path)
        size = os.path.getsize(path)
        print(f"OK ({size} bytes)")
        success += 1
    except Exception as e:
        print(f"FAIL: {e}")
        fail += 1

print(f"\nDone! {success} ok, {fail} failed")
