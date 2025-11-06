import socket
import threading
import hashlib
import sys

class EncryptedProxy:
    def __init__(self, password):
        self.password = password
    
    def encrypt(self, data):
        return bytes(a ^ b for a, b in zip(data, hashlib.sha256(self.password.encode()).digest() * len(data)))
    
    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(4096)
            encrypted_request = self.encrypt(request)
            
            # Подключаемся к целевому серверу
            target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target_socket.connect(('trusted-server.com', 8080))
            target_socket.send(encrypted_request)
            
            response = target_socket.recv(4096)
            client_socket.send(self.encrypt(response))
        except:
            pass

    def start(self, port=1080):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(5)
        print(f"[+] Proxy started on port {port}")
        
        while True:
            client, addr = server.accept()
            threading.Thread(target=self.handle_client, args=(client,)).start()

if __name__ == "__main__":
    proxy = EncryptedProxy("OnelifeOnedeath")  # Пароль изменен
    proxy.start()
