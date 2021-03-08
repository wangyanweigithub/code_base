import fcntl
import os

with open("w", "w") as f:
    flags = fcntl.fcntl(f.fileno(), fcntl.F_GETFL)
    fcntl.fcntl(f.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK)

    res  = f.write("hell")

print(res)
