import socket
import threading
import hashlib
import ssl

class WhiteListProxy:
    def __init__(self, key="OnelifeOnedeath"):
        self.key = key
        self.domain_map = {
            "youtube.com": "rutube.ru",
            "discord.com": "vk.com", 
            "twitter.com": "telegram.org",
            "github.com": "gitflic.ru"
        }
    
    def encrypt(self, data):
        key_hash = hashlib.sha256(self.key.encode()).digest()
        return bytes(a ^ b for a, b in zip(data, key_hash * (len(data)//32 + 1)))
    
    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(8192)
            decrypted_request = self.encrypt(request)
            
            # Маскируем домены
            for blocked, allowed in self.domain_map.items():
                decrypted_request = decrypted_request.replace(
                    blocked.encode(), 
                    allowed.encode()
                )
            
            # Отправляем через HTTPS для маскировки
            context = ssl.create_default_context()
            with socket.create_connection(('vk.com', 443)) as sock:
                with context.wrap_socket(sock, server_hostname='vk.com') as ssock:
                    ssock.send(decrypted_request)
                    response = ssock.recv(8192)
            
            encrypted_response = self.encrypt(response)
            client_socket.send(encrypted_response)
            
        except Exception as e:
            print(f"Error: {e}")
    
    def start_proxy(self, port=8080):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', port))
        server.listen(10)
        print(f"[+] WhiteList Proxy started on port {port}")
        
        while True:
            client, addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    proxy = WhiteListProxy()
    proxy.start_proxy()
