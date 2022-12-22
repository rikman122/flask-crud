from dotenv import load_dotenv
load_dotenv()

import os

ip = os.environ.get('SERVER_IP')
port = os.environ.get('SERVER_PORT')

bind = f"{ip}:{port}"
workers = 2
