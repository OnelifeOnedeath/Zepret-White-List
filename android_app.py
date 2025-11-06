import requests
import subprocess
import time

class AndroidTunnel:
    def __init__(self, server_ip, key="OnelifeOnedeath"):
        self.server_ip = server_ip
        self.key = key
        self.port = 8080
    
    def setup_tunnel(self):
        # Настройка HTTP прокси через ADB
        subprocess.run(["settings", "put", "global", "http_proxy", f"{self.server_ip}:{self.port}"])
        print("[+] Mobile proxy configured")
    
    def test_connection(self):
        try:
            response = requests.get(f"http://{self.server_ip}:{self.port}/test", 
                                  headers={"Host": "youtube.com"})
            return response.status_code == 200
        except:
            return False

# Использование
tunnel = AndroidTunnel("your-server-ip")
tunnel.setup_tunnel()
