#!/data/data/com.termux/files/usr/bin/bash

# Protect CPU from Android Doze Mode
termux-wake-lock

# Terminate previous conflicting processes cleanly
pkill -9 cloudflared 2>/dev/null
pkill -9 python3 2>/dev/null
pkill -9 proot-distro 2>/dev/null
sleep 2

# Launch Advanced Flask Engine in Background
nohup python3 ~/main_engine.py > ~/engine.log 2>&1 &

# Launch Cloudflare Tunnel with QUIC Protocol & Token
nohup cloudflared tunnel --edge-ip-version 4 --protocol quic run --token eyJhIjoiZDZiMzI5MTkxODQxODcwY2Q2MDU4ODAyZTkwM2E1NmEiLCJ0IjoiMmRjMDZiMDYtODdmNC00NDFjLWI3ZmItMTUxMGJlYTRlMDFkIiwicyI6Ik1qQXhabUZoTnpNdFpEZ3hPUzAwWTJWa0xUbG1ZamN0Wmpsa1ptVmhOemsyWkdJNE9EZzBPVEJsTTJVdFlqWXhaQzAwT0dSbExXSTBZelV0WVdaaU0ySmtPRFkxTkRZMyJ9 > ~/tunnel.log 2>&1 &

# Synchronize Ubuntu Environment in Background
if command -v proot-distro &> /dev/null; then
    proot-distro login ubuntu --shared-tmp -- /bin/true 2>/dev/null
fi

sleep 3
echo "[✓] Ultimate Pipeline initialized and synchronized successfully!"
