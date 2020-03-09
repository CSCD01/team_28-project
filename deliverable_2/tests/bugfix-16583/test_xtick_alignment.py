import numpy as np
import pytest
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison, check_figures_equal

# Test cases for Issue 16583
def test_xtickalign_validation_rcparams():
    with pytest.raises(ValueError):
        mpl.rcParams['xtick.alignment'] = 'top'
        
@check_figures_equal(extensions=['png'])
def test_left_xtick(fig_test, fig_ref):
    labels = range(0, 100, 10)
    fig_test.subplots()
    ax1 = fig_test.axes
    ax1[0].set_xticklabels(labels, ha='left')
    mpl.rcParams['xtick.alignment'] = 'left'
    fig_ref.subplots()
    ax2 = fig_ref.axes
    ax2[0].set_xticklabels(labels)
    
@check_figures_equal(extensions=['png'])
def test_right_xtick(fig_test, fig_ref):
    labels = range(0, 100, 10)
    fig_test.subplots()
    ax1 = fig_test.axes
    ax1[0].set_xticklabels(labels, ha='right')
    mpl.rcParams['xtick.alignment'] = 'right'
    fig_ref.subplots()
    ax2 = fig_ref.axes
    ax2[0].set_xticklabels(labels)
    
@check_figures_equal(extensions=['png'])
def test_center_xtick(fig_test, fig_ref):
    labels = range(0, 100, 10)
    fig_test.subplots()
    ax1 = fig_test.axes
    ax1[0].set_xticklabels(labels, ha='center')
    mpl.rcParams['xtick.alignment'] = 'center'
    fig_ref.subplots()
    ax2 = fig_ref.axes
    ax2[0].set_xticklabels(labels)

@pytest.mark.xfail
@check_figures_equal(extensions=['png'])
def test_center_left_xtick_alignment(fig_test, fig_ref):
    mpl.rcParams['xtick.alignment'] = 'center'
    fig_test.subplots().plot([1, 2, 3])
    mpl.rcParams['xtick.alignment'] = 'left'
    fig_ref.subplots().plot([1, 2, 3])

@pytest.mark.xfail
@check_figures_equal(extensions=['png'])
def test_center_right_xtick_alignment(fig_test, fig_ref):
    mpl.rcParams['xtick.alignment'] = 'center'
    fig_test.subplots().plot([1, 2, 3])
    mpl.rcParams['xtick.alignment'] = 'right'
    fig_ref.subplots().plot([1, 2, 3])

@pytest.mark.xfail
@check_figures_equal(extensions=['png'])
def test_left_right_xtick_alignment(fig_test, fig_ref):
    mpl.rcParams['xtick.alignment'] = 'left'
    fig_test.subplots().plot([1, 2, 3])
    mpl.rcParams['xtick.alignment'] = 'right'
    fig_ref.subplots().plot([1, 2, 3])

