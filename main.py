
def O(a, b, c):
    v = b ** 2 - 4 * a * c
    if v> 0:
        root1 = (-b + v ** 0.5) / (2 * a)
        root2 = (+b + v ** 0.5) / (2 * a)

        return 2, (root1, root2)
    elif v== 0:
        root = -b / (2 * a)
        return 1, (root)
    else:
        return 0, None

def f():
    print("Now let solve the ax^2+bx+c")

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if a == 0:
        print("This is not a quadratic equation.")
        return

    num_roots, roots = O(a, b, c)

    if num_roots == 2:
        print("The equation has 2 real roots: {roots[0]} and {roots[1]}")
    elif num_roots == 1:
        print("The equation has 1 real root: {roots[0]}")
    else:
        print("The equation has no real roots.")


f()
