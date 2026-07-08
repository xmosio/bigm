import json
import subprocess
from datetime import datetime
 
users = {
    "Sofi": "https://bigo.tv/user/798484012",
    "Shabnam": "https://bigo.tv/user/boqzepiano", 
    "prMarian": "https://bigo.tv/user/314614931",
    "Katrina": "https://bigo.tv/user/imkatrina",
    "Taniya": "https://bigo.tv/user/tanitantan",
    "Farimah": "https://bigo.tv/user/1042333738",
    "Zespina": "https://bigo.tv/user/695331268",
    "Elsa": "https://bigo.tv/user/elsa2222",
    "Suzan": "https://bigo.tv/user/suzan11",
    "Lara": "https://bigo.tv/user/onlylara",
    "Sahar": "https://bigo.tv/user/437072862",
    "Farimah juju": "https://bigo.tv/user/1079875463",
    "Parisa": "https://bigo.tv/user/691136946",
    "Blueberry": "https://bigo.tv/user/1042070957",
    "Hooriya": "https://bigo.tv/user/Hori.91",
    "Naz ahwaz": "https://bigo.tv/user/731627313",
    "Sahel": "https://bigo.tv/user/katrina00527",
    "Mira": "https://bigo.tv/user/857791870l",
    "Maral": "https://bigo.tv/user/1038185688",
    "Roya": "https://bigo.tv/user/roya72",
    "Nozhan": "https://bigo.tv/user/nozhanes",
    "Sernay": "https://bigo.tv/user/968395214",
    "Elnaz": "https://bigo.tv/user/bahaneh",
    "Sadaf": "https://bigo.tv/user/992242250",
    "oos Shaboon": "https://bigo.tv/user/717280198"
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
    status["users"][name] = "online" if is_live(url) else "__"

with open("status.json", "w") as f:
    json.dump(status, f, indent=2)
  
