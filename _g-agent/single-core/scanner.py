import os
import sys

def scan_core(conversation_id):
    base_path = os.path.expanduser("~/.gemini/antigravity/brain")
    log_path = os.path.join(base_path, conversation_id, ".system_generated/logs/overview.txt")
    
    if not os.path.exists(log_path):
        print("ERROR: Cognitive log not found. Ensure conversation ID is correct.")
        return

    # Get file size in bytes
    size_bytes = os.path.getsize(log_path)
    
    # Define arbitrary "Saturation Limit" (e.g., 1MB = ~250k tokens)
    # The system won't crash here, but it will start heavily truncating.
    MAX_CAPACITY_BYTES = 1048576  # 1 MB
    
    saturation_percent = (size_bytes / MAX_CAPACITY_BYTES) * 100
    
    # Terminal UI output
    print("="*40)
    print("🧠 CORE-SCANNER: COGNITIVE LOAD GAUGE")
    print("="*40)
    print(f"Target Session : {conversation_id[:8]}...")
    print(f"Log Size       : {size_bytes / 1024:.2f} KB")
    
    bar_length = 20
    filled_len = int(bar_length * saturation_percent // 100)
    filled_len = min(filled_len, bar_length) # Cap visual at 100%
    bar = '█' * filled_len + '-' * (bar_length - filled_len)
    
    print(f"Saturation     : [{bar}] {saturation_percent:.1f}%")
    
    if saturation_percent > 85:
        print("\n⚠️ WARNING: Critical Saturation. Truncation Imminent.")
        print("👉 ACTION REQUIRED: Execute the 'snapshot' tool now.")
    elif saturation_percent > 50:
        print("\n⚡ STATUS: Load increasing. Monitor context.")
    else:
        print("\n🟢 STATUS: Core is stable. High retention.")
    print("="*40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <conversation_id>")
    else:
        scan_core(sys.argv[1])
