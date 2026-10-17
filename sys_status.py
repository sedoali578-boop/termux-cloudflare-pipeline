import os, subprocess

print("🔍 --- SYSTEM STATUS & HEALTH CHECK ---")
cf_check = subprocess.run("pgrep -x cloudflared", shell=True, stdout=subprocess.PIPE)
py_check = subprocess.run("pgrep -f main_engine.py", shell=True, stdout=subprocess.PIPE)

print(f"🌐 Cloudflare Tunnel: {'[RUNNING]' if cf_check.returncode == 0 else '[STOPPED]'}")
print(f"⚙️ Flask Engine:      {'[RUNNING]' if py_check.returncode == 0 else '[STOPPED]'}")
print("-" * 40)
