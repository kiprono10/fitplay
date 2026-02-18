import multiprocessing
import os

# Server configuration
bind = f"0.0.0.0:{os.environ.get('PORT', 10000)}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 60
keepalive = 2

# Process naming
proc_name = "fitplay"

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Server mechanics
daemon = False
pidfile = None
umask = 0
tmp_upload_dir = None

# SSL (if needed, set via environment variables)
keyfile = os.environ.get("GUNICORN_KEYFILE")
certfile = os.environ.get("GUNICORN_CERTFILE")

# Server hooks
def post_fork(server, worker):
    """Called after a worker has been forked."""
    pass

def when_ready(server):
    """Called when the server is ready."""
    print("FitPlay server is ready. Spawning workers")
