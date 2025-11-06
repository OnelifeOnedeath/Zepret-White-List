import socket
import threading
import hashlib

class WhiteListProxy:
    def __init__(self, key="OnelifeOnedeath"):
        self.key = key
        self.whitelist = ["gosuslugi.ru", "vk.com", "yandex.ru"]
    
    def encrypt(self, data):
        key_hash = hashlib.sha256(self.key.encode()).digest()
        return bytes(a ^ b for a, b in zip(data, key_hash * (len(data)//32 + 1)))
    
    def handle_client(self, client_socket):
        try:
            encrypted_request = client_socket.recv(8192)
            request = self.encrypt(encrypted_request)
            
            # Маскируем домены под белый список
            domain_map = {
                "youtube.com": "rutube.ru",
                "discord.com": "vk.com",
                "twitter.com": "telegram.org"
            }
            
            # Подменяем домен
            for blocked, allowed in domain_map.items():
                request = request.replace(blocked.encode(), allowed.encode())
            
            # Отправляем через легальный прокси
            target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target_socket.connect(('trusted-server.com', 80))
            target_socket.send(self.encrypt(request))
            
            response = target_socket.recv(8192)
            client_socket.send(self.encrypt(response))
            
        except Exception:
            pass

    def start_proxy(self, port=8080):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(10)
        print(f"[+] WhiteList 1.0 proxy started on port {port}")
        
        while True:
            client, addr = server.accept()
            threading.Thread(target=self.handle_client, args=(client,)).start()

if __name__ == "__main__":
    proxy = WhiteListProxy()
    proxy.start_proxy()
