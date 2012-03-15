"""
This module defines Tengolo's core classes for models, views, logs, and batches
"""

import time
import matplotlib.pyplot as pyl

class TengoloModel(object):
    def set_param(self, param, value ):
        self.__dict__[param] = value

    def get_param(self, param ):
        return self.__dict__[param]


class TengoloView(object):
    def __init__(self, model):
        self.controls = []
        self.observers = []
        self.model = model
        self.ax_count = 0

    def set_param(self, param, val):
        self.model.set_param(param, val)
        self.update()

    def update(self):
        self.model.update()
        for (i, obj) in enumerate(self.observers):
            obj['render_function'](obj["ax"], self.model, obj["args"])
        pyl.draw()

    def render(self):
        self.update()
        pyl.show()

    def add_observer(self, render_function, location, args):
        ax = pyl.axes(location)
        self.observers.append({
            "render_function": render_function,
            "ax": ax,
            "args": args,
        })
        self.ax_count += 1

    def add_control(self, render_function, param, location, args ):
        ax  = pyl.axes(location)
        self.controls.append( render_function(ax, self, param, args) )
        self.ax_count += 1


class TengoloLog(object):
    pass


class TengoloBatch(object):
    pass


