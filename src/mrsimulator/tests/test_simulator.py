# -*- coding: utf-8 -*-
"""
Tests for the base Parseable pattern
"""
# import os.path
import pytest
from mrsimulator import Site, Isotopomer, Spectrum, Simulator


@pytest.fixture
def spectrum():
    return Spectrum(
        number_of_points=1024,
        spectral_width=100,
        reference_offset=0,
        magnetic_flux_density=9.4,
        rotor_frequency=0,
        rotor_angle=0.9553,  # 54.935 degrees in radians
        rotor_phase=0,
        isotope="1H",
        spin=1,
        natural_abundance=0.04683,
        gyromagnetic_ratio=-8.465,
    )


@pytest.fixture
def isotopomers():
    return [
        Isotopomer(
            sites=[Site(isotope="29Si", isotropic_chemical_shift=10)], abundance=10
        )
    ]


@pytest.fixture
def simulator(isotopomers, spectrum):
    return Simulator(isotopomers, spectrum)


def test_allowed_isotopes():
    assert set(Simulator.allowed_isotopes()) == {
        "19F",
        "31P",
        "129Xe",
        "1H",
        "57Fe",
        "13C",
        "15N",
        "29Si",
    }


def test_all_isotopes(simulator):
    assert set(simulator.all_isotopes) == {"29Si"}


def test_valid_isotope_list(simulator):
    assert set(simulator.valid_isotope_list) == {"29Si"}


def test_one_d_spectrum(simulator):
    simulator.one_d_spectrum
