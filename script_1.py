import os
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {host}"
    return os.system(command)

host = input(f'Which host would you like to ping? ')

#host = "google.com"
ping(host)
