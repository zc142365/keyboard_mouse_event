from pynput.keyboard import Listener
from pynput.mouse import Listener
import pynput.keyboard as key
import pynput.mouse as mouse

def on_release(*key):
    print(str(key))
    if  str(key).find("Key.esc") != -1:
        m_listener.stop()
        return False


def on_click(*mouse):
    print(mouse)

with key.Listener(on_release=on_release) as k_listener, \
        mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()
