import json
import subprocess
from datetime import datetime

users = {
    "Sofi": "https://bigo.tv/user/798484012",
    "Shaboon": "https://bigo.tv/user/717280198"
}

def is_live(url):
    try:
        result = subprocess.run(
            ["yt-dlp", "-j", url],
            capture_output=True,
            text=True
        )
        data = json.loads(result.stdout)
        return data.get("is_live", False)
    except:
        return False

status = {
    "updated": datetime.utcnow().isoformat() + "Z",
    "users": {}
}

for name, url in users.items():
    status["users"][name] = "online" if is_live(url) else "offline"

with open("status.json", "w") as f:
    json.dump(status, f, indent=2)
  
