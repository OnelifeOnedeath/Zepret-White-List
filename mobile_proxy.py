import socket
import threading
import hashlib
import time

class MobileProxy:
    def __init__(self, key="OnelifeOnedeath"):
        self.key = key
        self.whitelist = ["gosuslugi.ru", "vk.com", "yandex.ru"]
    
    def encrypt(self, data):
        key_hash = hashlib.sha256(self.key.encode()).digest()
        return bytes(a ^ b for a, b in zip(data, key_hash * (len(data)//32 + 1)))
    
    def disguise_domain(self, original_domain):
        # Маскируем запрещенные домены под разрешенные
        domain_map = {
            "youtube.com": "rutube.ru",
            "discord.com": "vk.com", 
            "google.com": "yandex.ru"
        }
        return domain_map.get(original_domain, original_domain)
    
    def handle_mobile_client(self, client_socket):
        try:
            # Принимаем запрос от мобильного клиента
            encrypted_request = client_socket.recv(8192)
            request = self.encrypt(encrypted_request)
            
            # Извлекаем целевой домен и маскируем
            host = self.extract_host(request)
            disguised_host = self.disguise_domain(host)
            
            # Подключаемся к целевому серверу через маскировку
            target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target_socket.connect((disguised_host, 80))
            
            # Модифицируем запрос с подмененным Host header
            modified_request = request.replace(
                f"Host: {host}".encode(),
                f"Host: {disguised_host}".encode()
            )
            
            target_socket.send(self.encrypt(modified_request))
            response = target_socket.recv(8192)
            client_socket.send(self.encrypt(response))
            
        except Exception as e:
            pass

    def extract_host(self, request):
        # Парсим Host из HTTP запроса
        lines = request.decode().split('\n')
        for line in lines:
            if line.startswith('Host:'):
                return line.split(' ')[1].strip()
        return ""

    def start_mobile_proxy(self, port=8080):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', port))
        server.listen(10)
        print(f"[+] Mobile proxy started on port {port}")
        
        while True:
            client, addr = server.accept()
            threading.Thread(target=self.handle_mobile_client, args=(client,)).start()

if __name__ == "__main__":
    proxy = MobileProxy()
    proxy.start_mobile_proxy()
