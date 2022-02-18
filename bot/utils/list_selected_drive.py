from telethon.tl.types import KeyboardButtonCallback
from bot.core.getVars import get_val
import asyncio
import json
import logging

log = logging.getLogger(__name__)
yes = "✅"
folder = "📁"

async def list_selected_drive(drive_base, drive_name, conf_path, rclone_dir, data_cb, menu):
    prev="" 
    if get_val("BASE_DIR") == "/":
        prev= yes
    menu.append([KeyboardButtonCallback(f"{prev} Seleccione esta Carpeta", f"settings {data_cb} / )".encode("UTF-8"))])

    cmd = ["rclone", "lsjson", f'--config={conf_path}', f"{drive_name}:{drive_base}"]

    # piping only stdout
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE
    )

    stdout, _ = await process.communicate()
    stdout = stdout.decode().strip()

    try:
        data = json.loads(stdout)
        log.info(data)
        for i in data:
            path = i["Path"]
            path == path.strip()
            mime_type= i['MimeType']
            prev2= ""   
            folder1= folder
            zip= ""
            if len(path) <= 20: 
                if path == rclone_dir:
                    prev2= yes
                    folder1= ""
                if mime_type == 'application/zip':  
                    zip= "🗄"  
                    folder1= ""
                if " " in path:
                    continue    
                menu.append(
                    [KeyboardButtonCallback(f"{prev2} {folder1} {zip} {path}", f"settings {data_cb} {path}".encode("UTF-8"))])
    except Exception as e:
        log.info(e)
