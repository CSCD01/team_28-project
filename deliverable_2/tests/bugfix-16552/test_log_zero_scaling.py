import numpy as np
import pytest
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison, check_figures_equal

@check_figures_equal()
def test_scatter_autoscaling_w_zero_xy(fig_test, fig_ref):
    x_vals = [0, 4.38462e-06, 5.54929e-06, 7.02332e-06, 8.88889e-06]
    y_vals = [0, 0.10000000000000002, 0.182, 0.332, 0.604]
    
    pts = np.array(list(itertools.product(x_vals, y_vals))) # This converts the values to a numpy array

    ax_test = fig_test.gca()
    ax_test.set_yscale('log')
    ax_test.plot(pts[:,0], pts[:,1], marker="o", ls="")

    ax_ref = fig_ref.gca()
    ax_ref.set_yscale('log')
    ax_ref.plot(pts[:,0], pts[:,1], marker="o", ls="")

@check_figures_equal()
def test_scatter_autoscaling_w_zero_x(fig_test, fig_ref):
    x_vals = [0, 4.38462e-06, 5.54929e-06, 7.02332e-06, 8.88889e-06]
    y_vals = [0.10000000000000002, 0.182, 0.332, 0.604]
    
    pts = np.array(list(itertools.product(x_vals, y_vals))) # This converts the values to a numpy array

    ax_test = fig_test.gca()
    ax_test.set_yscale('log')
    ax_test.plot(pts[:,0], pts[:,1], marker="o", ls="")

    ax_ref = fig_ref.gca()
    ax_ref.set_yscale('log')
    ax_ref.plot(pts[:,0], pts[:,1], marker="o", ls="")

@check_figures_equal()
def test_scatter_autoscaling_w_zero_y(fig_test, fig_ref):
    x_vals = [4.38462e-06, 5.54929e-06, 7.02332e-06, 8.88889e-06]
    y_vals = [0, 0.10000000000000002, 0.182, 0.332, 0.604]
    
    pts = np.array(list(itertools.product(x_vals, y_vals))) # This converts the values to a numpy array

    ax_test = fig_test.gca()
    ax_test.set_yscale('log')
    ax_test.plot(pts[:,0], pts[:,1], marker="o", ls="")

    ax_ref = fig_ref.gca()
    ax_ref.set_yscale('log')
    ax_ref.plot(pts[:,0], pts[:,1], marker="o", ls="")

@check_figures_equal()
def test_scatter_autoscaling_wo_zero(fig_test, fig_ref):
    x_vals = [4.38462e-06, 5.54929e-06, 7.02332e-06, 8.88889e-06]
    y_vals = [0.10000000000000002, 0.182, 0.332, 0.604]
    
    pts = np.array(list(itertools.product(x_vals, y_vals))) # This converts the values to a numpy array

    ax_test = fig_test.gca()
    ax_test.set_yscale('log')
    ax_test.plot(pts[:,0], pts[:,1], marker="o", ls="")

    ax_ref = fig_ref.gca()
    ax_ref.set_yscale('log')
    ax_ref.plot(pts[:,0], pts[:,1], marker="o", ls="")