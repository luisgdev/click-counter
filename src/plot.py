from os import path
from matplotlib import colors
from tinydb import TinyDB
import matplotlib.pyplot as plt
import numpy as np


def _get_points():
    db_path = path.join('output','clicks.json')
    db = TinyDB(db_path)
    return db.all()


def gen_axis():
    nax = np.array([])
    nay = np.array([])
    for item in _get_points():
        nax = np.append(nax, item['_x'])
        nay = np.append(nay, item['_y'])
    # Turn Y axis negative to start from top to bottom
    nay = nay * -1
    return nax, nay


if __name__ == '__main__':
    ax, ay = gen_axis()
    # Edit rcParams to place X axis on top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.scatter(ax, ay)
    plt.show()
