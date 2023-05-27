# -

# Facebook  : -
# Instagram : -
# Github    : -
# Telegram  : -

import os
import subprocess

if __name__ == "__main__":
	os.system('git pull')
	os.system('clear')
	try:
		result = subprocess.run(["uname", "-m"], capture_output=True, text=True)
		if result.returncode == 0:
			architecture = result.stdout.strip()
			if architecture == "aarch64":
				__import__("HunterNblz").main()
			else:
				print("[!] Perangkat Harus 64 Bit [!]\n")
	except Exception as e:
		exit(str(e))
