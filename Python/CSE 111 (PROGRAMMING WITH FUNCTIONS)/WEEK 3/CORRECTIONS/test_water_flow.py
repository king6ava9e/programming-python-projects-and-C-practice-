# test_water_flow.py

from pytest import approx
import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0, abs=0.001)
    assert water_column_height(0.0, 10.0) == approx(7.5, abs=0.001)
    assert water_column_height(25.0, 0.0) == approx(25.0, abs=0.001)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.001)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(5, 1.75) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.05, 1.75) == approx(87371.814, abs=0.001)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.10, 0.05, 1.75) == approx(-1.688, abs=0.001)

def test_kpa_to_psi():
    assert kpa_to_psi(100) == approx(14.5038, abs=0.0001)
    assert kpa_to_psi(50) == approx(7.2519, abs=0.0001)

pytest.main(["-v", "--tb=line", "-rN", __file__])
