def outer(num1):
    def inner(num2):
        # Les variables des fonctions externes doivent être modifiées
        # à l'aide du mot-clé nonlocal avant de pouvoir être modifiées
        # dans les fonctions internes
        nonlocal num1
        num1 += num2
        print(num1)
    return inner


fn = outer(10)
fn(10)
fn(10)
