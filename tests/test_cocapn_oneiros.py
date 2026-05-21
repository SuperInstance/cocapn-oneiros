"""Tests for cocapn-oneiros."""

import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import cocapn_oneiros


def test_version():
    assert cocapn_oneiros.__version__ == "0.2.0"


def test_module_importable():
    import cocapn_oneiros
    assert cocapn_oneiros is not None
