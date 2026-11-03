"""Tests for the Patient model."""

from inflammation.models import Patient

def test_create_patient():
    """Check that a patient keeps the name passed to its constructor."""

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name
