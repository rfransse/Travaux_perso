from math import sin, pi

g = lambda x:x*2+2*x+4

def integral(f, a, b, delta):
    """calcule une intégrale définie

    Args:
        f (function): fonction à intégrer
        a (float): borne inférieure
        b (float): borne supérieure
        delta (float): précision
        
    Returns:
        float: intégrale de f entre a et b avec une précision delta
    """
    x = a
    I = 0
    while x < b:
        I += f(x)*delta
        x += delta
    print(I)

integral(sin, 0, pi, 0.0000001)


    
