"""Skeleton for supplemental AC tests, to be downloaded and overwritten with implemented tests from hidden Gitlab
by ac_download.py."""


__author__ = "Maarten de Jeu"
__copyright__ = "Copyright 2022, Hogeschool Utrecht"


import unittest as tst


def make_empty_test():
    """Create an empty TestCase.

    Returns:
        A TestCase which contains 0 tests."""

    class _EmptyTest(tst.TestCase):
        pass

    return _EmptyTest


def test_vector_addition(vector_addition):
    return make_empty_test()


def test_negative_of_vector(negative_of_vector, vector_addition):
    return make_empty_test()


def test_scalar_product(scalar_product, vector_addition):
    return make_empty_test()


def test_inner_product(inner_product, scalar_product):
    return make_empty_test()


def test_vector_matrix_product(matrix_product):
    return make_empty_test()


def test_matrix_product(matrix_product):
    return make_empty_test()


def test_neural_network(read_network, run_network, matrix_product):
    return make_empty_test()


def test_determinant(determinant_2, determinant_3, determinant):
    return make_empty_test()


def test_inverse_2(inverse_matrix_2):
    return make_empty_test()


def test_inverse_(inverse_matrix, transpose):
    return make_empty_test()


def test_magisch_vierkant(magisch_vierkant):
    return make_empty_test()


def test_limit(limit_left, limit_right, limit):
    return make_empty_test()


def test_numeric_derivative(get_derivative_at):
    return make_empty_test()


def test_verkeer_snelheden(get_data, bereken_deltas):
    return make_empty_test()


def test_polynomial_derivative(get_derivative):
    return make_empty_test()


def test_matrix_derivative(deriv_matrix):
    return make_empty_test()


# deriv_message() is here, but I suppose that's a helper function and not a test?


def test_symbolic_differentiation_alfa(Constant, Variable, Sum, Product, Power):
    return make_empty_test()


def test_symbolic_differentiation_bravo(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan):
    return make_empty_test()


def test_symbolic_differentiation_charlie(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan, E, Exponent, Ln, Log):
    return make_empty_test()


def test_symbolic_differentiation_charlie_eq(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan, E, Exponent, Ln, Log):
    return make_empty_test()



def test_symbolic_differentiation_delta(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan, E, Exponent, Ln, Log):
    return make_empty_test()


def test_symbolic_differentiation_delta_eq(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan, E, Exponent, Ln, Log):
    return make_empty_test()


def test_regressie(train, gradient, cost, data):
    return make_empty_test()


def test_verkeer_posities(get_data, bereken_posities, vind_botsing):
    return make_empty_test()


def test_numeric_integral(get_integral_between):
    return make_empty_test()


def test_polynomial_integral(get_integral):
    return make_empty_test()


# Integrate_message()


def test_symbolic_integration_alfa(Constant, Variable, Sum, Product, Power):
    return make_empty_test()


def test_symbolic_integration_alfa_eq(Constant, Variable, Sum, Product, Power):
    return make_empty_test()


def test_symbolic_integration_bravo(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan, E, Exponent, Ln, Log):
    return make_empty_test()


def test_symbolic_integration_bravo_eq(Constant, Variable, Sum, Product, Power, Sin, Cos, Tan, E, Exponent, Ln, Log):
    return make_empty_test()


def test_euler(afgeleide_functie, euler):
    return make_empty_test()
