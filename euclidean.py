def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
gcd = euclidean_algorithm(a, b)
print(f"\nEuclidean Algorithm:")
print(f"GCD of {a} and {b} is: {gcd}")
# Extended Euclidean Algorithm to find GCD and coefficients
gcd, x, y = extended_euclidean_algorithm(a, b)
print(f"\nExtended Euclidean Algorithm:")
print(f"GCD of {a} and {b} is: {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Verification: {a}*{x} + {b}*{y} = {gcd}")