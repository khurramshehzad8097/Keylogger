 keylogger.py ARch internship task # 02

import tkinter as tk
from datetime import datetime

def on_key(event):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} | keysym={event.keysym!r} char={event.char!r}\n"
    output.insert("end", line)
    output.see("end")

root = tk.Tk()
root.title("Consent-Based Input Tester")

label = tk.Label(root, text="Type in this window only. Events are shown below.")
label.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60)
entry.pack(padx=10, pady=10)
entry.bind("<Key>", on_key)

output = tk.Text(root, width=80, height=20)
output.pack(padx=10, pady=10)

root.mainloop()