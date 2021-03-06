"""
This module provides functions to render specific plots and widgets.
"""

from matplotlib.contour import QuadContourSet
from matplotlib.widgets import Slider

import matplotlib.pyplot as pyl


def contour(ax, model, args):
    ax.cla()
    obj = QuadContourSet(ax, model.get_param(args["x"]), model.get_param(args["y"]), model.get_param(args["z"]), 100)

    if 'title' in args:
        ax.set_title(args['title'])

    if 'xlabel' in args:
        ax.set_xlabel(args['xlabel'])

    if 'ylabel' in args:
        ax.set_ylabel(args['ylabel'])

    #! hack:
    ax.plot( model.get_param("v_star"), model.get_param("w_star"), 'r+' )
    ax.plot( model.get_param("v_bar"), 2, 'r+' )

    return obj


def slider(ax, view, param, args):
    my_slider = Slider(ax, param, args["range_min"], args["range_max"], valinit=view.model.get_param(param))
    my_slider.on_changed(lambda val: view.set_param( param, val ))
    return my_slider

def timer(ax, view, param, args):
#    my_slider = Slider(ax, param, args["min_inc"], args["max_inc"], valinit=view.model.get_param(param))

    timer = ax.figure.canvas.new_timer(interval=200)
    timer.add_callback(view.update)
    timer.start()

    return timer
