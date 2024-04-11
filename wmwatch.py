import os
import hyprwatcher

instance_signature = os.getenv("HYPRLAND_INSTANCE_SIGNATURE")
if not instance_signature:
    raise ValueError("HYPRLAND_INSTANCE_SIGNATURE environment variable is not set.")

socket_path = f"/tmp/hypr/{instance_signature}/.socket2.sock"
log_path = os.path.expanduser("~/.hyprwatcher.log")

hyprwatcher.watch_socket(socket_path, log_path)

