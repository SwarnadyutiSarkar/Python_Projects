import numpy as np

class PolynomialSolver:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def solve(self):
        roots = np.roots(self.coefficients)
        return roots

def parse_polynomial(equation):
    # Remove spaces and split by '+'
    equation = equation.replace(" ", "")
    terms = equation.split('+')
    degree = max([int(term.split('x^')[1]) if 'x^' in term else 1 for term in terms if 'x' in term] + [0])
    coefficients = [0] * (degree + 1)
    
    for term in terms:
        if 'x^' in term:
            coef, power = term.split('x^')
            coefficients[int(power)] = float(coef) if coef else 1
        elif 'x' in term:
            coef = term.split('x')[0]
            coefficients[1] = float(coef) if coef else 1
        else:
            coefficients[0] = float(term)
    
    return coefficients[::-1]

def main():
    print("Welcome to the Polynomial Solver!")
    equation = input("Enter a polynomial equation (e.g., 2x^3 + 4x^2 - 3x + 6): ")
    coefficients = parse_polynomial(equation)
    
    solver = PolynomialSolver(coefficients)
    roots = solver.solve()
    
    print("The roots of the polynomial are:", roots)

if __name__ == "__main__":
    main()
