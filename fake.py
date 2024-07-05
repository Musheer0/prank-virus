import ctypes
import pyautogui
import random
import time
import winsound
import subprocess
import webbrowser
import threading
from tkinter import Tk, Canvas

# Function to display a fake virus alert
def fake_virus_alert():
    ctypes.windll.user32.MessageBoxW(0, "A virus has been detected on your computer!", "Virus Alert", 1)

# Function to move the mouse cursor randomly
def crazy_mouse():
    end_time = time.time() + 4  # Run for 10 seconds
    while time.time() < end_time:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.1)

# Function to play random beeps
def annoying_beeps():
    end_time = time.time() + 10  # Run for 10 seconds
    while time.time() < end_time:
        winsound.Beep(random.randint(1000, 2000), 500)
        time.sleep(.1)

# Function to run commands in terminal
def run_terminal_commands():
    commands = [
        "ipconfig",
        "ping 127.0.0.1 -n 5",
        "netstat -an",
        "tracert www.google.com"
    ]
    for cmd in commands:
        subprocess.Popen(["start", "cmd", "/k", cmd], shell=True)
# Function to run multiple instances of crazy_mouse to simulate multiple cursors
def multiple_cursors(n):
    threads = []
    for _ in range(n):
        t = threading.Thread(target=crazy_mouse)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

# Function to display full-screen colors with text "HACKING"
def display_full_screen_colors():
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "teal", "lavender", "brown", "black", "white"]
    
    for color in colors:
        root = Tk()
        root.attributes('-fullscreen', True)
        canvas = Canvas(root, bg=color)
        canvas.pack(fill="both", expand=True)
        canvas.create_text(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2, text="HACKING", font=("Arial", 50), fill="white" if color != "white" else "black")
        root.update()
        time.sleep(.1)
        root.destroy()

# Execute the pranks in sequence
fake_virus_alert()
multiple_cursors(5)  # Run 5 instances of the crazy_mouse function
annoying_beeps()
for i in range(3):
    run_terminal_commands()
    display_full_screen_colors()
