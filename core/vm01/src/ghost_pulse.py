import threading
import time
import random
import os
import subprocess
import shutil

def setup_virtual_display():
    """Initializes a virtual framebuffer (Xvfb) for headless keystroke synthesis."""
    print("[*] Setting up Virtual Display (Xvfb)...")
    
    # Check if Xvfb is already installed before trying to use apt-get
    if shutil.which("Xvfb") is None:
        print("[*] Xvfb not found. Installing...")
        # Install xvfb if not present (requires sudo/root)
        install_cmd = "sudo apt-get update -qq && sudo apt-get install -y xvfb -qq" if os.geteuid() != 0 else "apt-get update -qq && apt-get install -y xvfb -qq"
        os.system(install_cmd)
    else:
        print("[*] Xvfb is already installed. Skipping installation.")
    
    # Set the display environment variable
    os.environ["DISPLAY"] = ":99"
    
    # Start Xvfb in the background
    subprocess.Popen(["Xvfb", ":99", "-screen", "0", "1024x768x16"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2) # Give the virtual display time to boot

def ghost_pulse():
    """
    Synthesizes benign hardware interrupts with stochastic delays.
    Import is delayed until the virtual display is active.
    """
    # Import pynput *after* Xvfb is running
    from pynput.keyboard import Controller, Key
    keyboard = Controller()
    
    while True:
        # Stochastic delay between 15 and 25 minutes
        delay_seconds = random.randint(900, 1500)
        time.sleep(delay_seconds)
        
        # Alternate between modifiers to avoid static pattern detection
        modifier = random.choice([Key.shift, Key.ctrl, Key.alt])
        
        keyboard.press(modifier)
        keyboard.release(modifier)
        print(f"[Ghost Pulse] Synthesized interaction. Next pulse in {delay_seconds} seconds.")

if __name__ == "__main__":
    print("[Ghost Pulse] Daemon initializing. Bypassing idle timeout...")
    setup_virtual_display()
    
    pulse_thread = threading.Thread(target=ghost_pulse, daemon=True)
    pulse_thread.start()
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("[Ghost Pulse] Terminating daemon.")

