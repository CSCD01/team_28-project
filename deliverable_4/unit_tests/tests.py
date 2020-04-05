from types import SimpleNamespace

import matplotlib.widgets as widgets
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison

from numpy.testing import assert_allclose

import pytest

# create and return an axes object
def get_ax():
    fig, ax = plt.subplots(1, 1)
    ax.plot([0, 200], [0, 200])
    ax.set_aspect(1.0)
    ax.figure.canvas.draw()
    return ax

# trigger an event (keypress, click) programatically
def do_event(tool, etype, button=1, xdata=0, ydata=0, key=None, step=1):
    """
     *name*
        the event name

    *canvas*
        the FigureCanvas instance generating the event

    *guiEvent*
        the GUI event that triggered the matplotlib event

    *x*
        x position - pixels from left of canvas

    *y*
        y position - pixels from bottom of canvas

    *inaxes*
        the :class:`~matplotlib.axes.Axes` instance if mouse is over axes

    *xdata*
        x coord of mouse in data coords

    *ydata*
        y coord of mouse in data coords

     *button*
        button pressed None, 1, 2, 3, 'up', 'down' (up and down are used
        for scroll events)

    *key*
        the key depressed when the mouse event triggered (see
        :class:`KeyEvent`)

    *step*
        number of scroll steps (positive for 'up', negative for 'down')
    """
    event = SimpleNamespace()
    event.button = button
    ax = tool.ax
    event.x, event.y = ax.transData.transform([(xdata, ydata),
                                               (xdata, ydata)])[00]
    event.xdata, event.ydata = xdata, ydata
    event.inaxes = ax
    event.canvas = ax.figure.canvas
    event.key = key
    event.step = step
    event.guiEvent = None
    event.name = 'Custom'

    func = getattr(tool, etype)
    func(event)

# create a plot with the legend showing
def create_plt_with_legend_on():
    ax = get_ax()
    ax.legend(["test"])
    legend = ax.get_legend()
    legend.set_visible(False)

    return (ax, legend)

# create a plot with the legend hidden
def create_plt_with_legend_off():
    ax = get_ax()
    ax.legend(["test"])
    legend = ax.get_legend()
    legend.set_visible(True)

    return (ax, legend)

# using a plot with no legend set, pressing the "t" key should not do anything
# i.e. the legend should still be None
def test_no_legend():
    """For ellipse, test out the key modifiers"""
    ax = get_ax()

    def onselect(epress, erelease):
        pass

    tool = widgets.EllipseSelector(ax, onselect=onselect,
                                   maxdist=10, interactive=True)
    tool.extents = (100, 150, 100, 150)

    do_event(tool, 'on_key_press', xdata=100, ydata=100, button=1,
             key='t')
    do_event(tool, 'on_key_release', xdata=100, ydata=100, button=1,
             key='t')
    legend = ax.get_legend()
    assert legend == None

# using a plot with the legend set to visible, pressing the "t" key should
# set the visibilty of the legend to false
def test_legend_on():
    """For ellipse, test out the key modifiers"""
    (ax, legend) = create_plt_with_legend_on()

    def onselect(epress, erelease):
        pass

    tool = widgets.RectangleSelector(ax, onselect)

    do_event(tool, 'on_key_press', xdata=100, ydata=100, button=1,
             key='t')
    do_event(tool, 'on_key_release', xdata=100, ydata=100, button=1,
             key='t')
    assert legend.get_visible() == False

# using a plot with the legend set to hidden, pressing the "t" key should
# set the visibilty of the legend to True
def test_legend_off():
    """For ellipse, test out the key modifiers"""
    (ax, legend) = create_plt_with_legend_off()

    def onselect(epress, erelease):
        pass

    tool = widgets.RectangleSelector(ax, onselect)

    do_event(tool, 'on_key_press', xdata=100, ydata=100, button=1,
             key='t')
    do_event(tool, 'on_key_release', xdata=100, ydata=100, button=1,
             key='t')
    assert legend.get_visible() == True
