#!/bin/bash
# 🛡️ GHOST-MATRIX: OBFUSCATION SHIELD INITIALIZATION
# Target Environment: Kaggle / Debian 12 Base

# 1. Update package repositories and install dependencies silently
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq tor obfs4proxy torsocks curl

# 2. Construct the hardened routing configuration
# Note: systemd is usually inactive in Docker, so we run tor directly
cat << 'EOF' > /etc/tor/torrc
RunAsDaemon 1
ExcludeExitNodes {US},{GB},{CA}
StrictNodes 1
EOF

# 3. Initialize the daemon with the new bridge parameters
echo ">>> Starting Tor Daemon..."
tor -f /etc/tor/torrc &

# 4. Verify circuit establishment (Background loop)
echo "Awaiting circuit confirmation..."
# Wait for the log file to be created
while [ ! -f /var/log/tor/log ]; do
  sleep 1
done

while ! grep -q "Bootstrapped 100%" /var/log/tor/log; do
  sleep 2
done
echo "Obfuscation Shield Active."
