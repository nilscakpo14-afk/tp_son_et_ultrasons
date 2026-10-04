import numpy as np
import math as m
import sympy as sp

def uncertainty_A(A): 
    """
    calcul of the uncertity of a quantity with multiple mesurements in array A

    A (array)

    mean_A (float): mean of the array A

    sigma_A (float): standard deviation of the arry A

    u_A (float): uncertity of the mean_A
    """
    mean_A = np.mean(A)

    sigma_A = np.std(A, ddof = 1)

    u_A = sigma_A/m.sqrt(len(A))

    return mean_A, sigma_A, u_A

def relative_difference(A_th, A_exp):
    """
    calcul of the relative difference between theorical and experimental value of A 
    
    A_th (float): theorical value of A

    A_exp (float): experimental value of A
    """
    return abs(A_exp-A_th)/A_th

def undirect_uncertainty(expression, variables, values, uncertainties):
    """
    expression: expression of the fonction made with sympy

    variables (list): with the variable

    values (list or numpy array): values of each variable

    uncertainty (list or numpy array): uncertainty of each value
    """

    sum = 0
    substitution = dict(zip(variables, values)) # dictionnaire association de la variable a la valeur pour le calcul de la derievee en un point 

    for variable, uncertainty in zip(variables, uncertainties):

        derivative = sp.diff(expression, variable) # derivative with respect to variable

        derivative_value = derivative.subs(substitution) # replace each variable by the value

        sum = sum + (derivative_value * uncertainty)**2 # calcul of final uncertainty
    
    return float(sp.sqrt(sum))



