from pynput.mouse import Listener
from tinydb import TinyDB, Query
import os
import time


# Settings
session = time.perf_counter_ns()
db_path = os.path.join('output',f'{session}.json')


# Init database
def db_init():
    db = TinyDB(db_path)
    res = db.insert({'session': session, 'count': 0})
    return res

# Save in database
def save_click():
    db = TinyDB(db_path)
    counted = db.search(Query().session == session)[0]['count']
    res = db.update({'count': counted+1}, Query().session == session) 
    return res

# Get mouse event
def on_click(x, y, button, pressed):
    if pressed:
        save_click()
        print(f'Mouse clicked at ({x}, {y})')


if __name__ == '__main__':
    print(db_init())
    try:
        with Listener(on_click=on_click) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('\nLog finished!')

