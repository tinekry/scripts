def extended_gcd(a, b):
    """
    Returns a tuple (gcd, x, y) such that a*x + b*y = gcd
    """
    old_x, x = 1, 0
    old_y, y = 0, 1
    
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
        
    return a, old_x, old_y

# Example Usage:
gcd, x, y = extended_gcd(612, 58)
print(f"gcdE: {gcd}, x: {x}, y: {y}")