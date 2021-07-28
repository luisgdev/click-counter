from os import path
from pynput.mouse import Listener
from tinydb import TinyDB


def on_click(x, y, button, pressed):
    if pressed:
        db = TinyDB(path.join('..', 'output','clicks.json'))
        db.insert({'_x': x, '_y': y})
        print(f'Clicked at ({x}, {y})')


if __name__ == '__main__':
    try:
        with Listener(on_click=on_click) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('\nLog finished!')
