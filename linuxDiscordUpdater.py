import sys

try:
    import requests
    from fake_useragent import UserAgent
except:
    raise Exception("Make sure you installed the requirements.txt file, or that you ran the command like so:\n"
                    "sudo .venv/bin/python3 linuxDiscordUpdater.py")
import os

if sys.platform == ("linux" or "linux2"):  # If Linux is so good, why haven't they made Linux 2?
    if os.geteuid() != 0:  # This tells us if the user is sudo apparently
        raise Exception("This script needs to be run with sudo privileges\n"
                        "Run `sudo .venv/bin/python3 linuxDiscordUpdater.py`")
    ua = UserAgent().firefox
    url = "https://discord.com/api/download/stable?platform=linux&format=deb"
    filename = "discord_update.deb"
    response = requests.get(url, headers={"User-Agent": ua}, stream=True)

    # I hate dealing with websites
    if response.status_code == 200:
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("File downloaded successfully")
    else:
        raise Exception(f"Failed to download file. {response.status_code}")

    os.system(f"sudo dpkg -i {filename}")
else:
    raise Exception("This program is for Linux only.")