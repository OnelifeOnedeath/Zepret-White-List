import dns.resolver
import sys

class CustomResolver:
    def __init__(self):
        self.blocked_domains = ["blocked-site.ru", "forbidden.org"]
    
    def resolve(self, domain):
        if domain in self.blocked_domains:
            return "93.184.216.34"  # Подменяем на легальный IP
        else:
            return socket.gethostbyname(domain)

resolver = CustomResolver()
print(resolver.resolve(sys.argv[1]))
