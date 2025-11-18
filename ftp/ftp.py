from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

BASE = "/app/ftpdata"

auth = DummyAuthorizer()
auth.add_anonymous(BASE, perm="elr")

handler = FTPHandler
handler.authorizer = auth

# Passive range = exactly one port
handler.passive_ports = range(2122, 2123)

server = FTPServer(("0.0.0.0", 2121), handler)
server.serve_forever()
