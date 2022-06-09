from rich.live_render import LiveRender
from rich.console import Console
from rich.panel import Panel
import os, shutil
import sys

console = Console()
def hata (text):
    console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")    
    sys.exit()
def myscript ():
    return "ZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IENvbnNvbGUNCmZyb20gcmljaC5wYW5lbCBpbXBvcnQgUGFuZWwNCg0KaW1wb3J0IHN5cw0KY29uc29sZSA9IENvbnNvbGUoKQ0KZGVmIGJpbGdpICh0ZXh0KToNCiAgICBjb25zb2xlLnByaW50KFBhbmVsKGYnW2JsdWVde3RleHR9Wy9dJyx3aWR0aD03MCksanVzdGlmeT0iY2VudGVyIikgIA0KZGVmIHNvcnUgKHNvcnUpOg0KICAgIGNvbnNvbGUucHJpbnQoUGFuZWwoZidbYm9sZCB5ZWxsb3dde3NvcnV9Wy9dJyx3aWR0aD03MCksanVzdGlmeT0iY2VudGVyIikgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgcmV0dXJuIGNvbnNvbGUuaW5wdXQoZiJbYm9sZCB5ZWxsb3ddPj4gWy9dIikNCmRlZiBoYXRhICh0ZXh0KToNCiAgICBjb25zb2xlLnByaW50KFBhbmVsKGYnW2JvbGQgcmVkXXt0ZXh0fVsvXScsd2lkdGg9NzApLGp1c3RpZnk9ImNlbnRlciIpICAgIA0KICAgIHN5cy5leGl0KCkNCg0KYmlsZ2koIlBhc3N3b3JkIGRlY29kaW5nLi4uIikNCmRvZ3J1cGFzcz0gNDU3Nw0KICAgIA0Kc2lmcmUgPSBzb3J1KCJNZXJoYWJhISDFnmlmcmU6IikNCnRyeToNCiAgICBkb2dydXBhc3M9IGludChkb2dydXBhc3MpDQogICAgaWYgaW50KHNpZnJlKSAhPSBkb2dydXBhc3M6DQogICAgICAgIGhhdGEoIllhbmzEscWfIMWfaWZyZSIpDQpleGNlcHQgVHlwZUVycm9yOg0KICAgIGhhdGEoIllhbmzEscWfIMWfaWZyZSIpDQpleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgaGF0YSgiSGF0YTogIitzdHIoZSkp"                 
def bilgi (text):
    console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")  
def passed (text):
    console.print(Panel(f'[yellow]{text}[/]',width=70),justify="center") 
def noadded (text):
    console.print(Panel(f'[pink]{text}[/]',width=70),justify="center")  
def basarili (text):
    console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
    console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")                         
def soru (soru):
    console.print(Panel(f'[bold yellow]{soru}[/]',width=70),justify="center")                         
    return console.input(f"[bold yellow]>> [/]")
def logo (satirbırak=False):
    text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█"
    if satirbırak:
        for i in range(25):
            console.print("\n")
        console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center")
    else:
        console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center")
