import math

def suma(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def producto(c1, c2):
    return (((c1[0] * c2[0]) - (c2[1] * c1[1])), ((c1[0] * c2[1]) + (c2[0] * c1[1])))
def productolineal (c1,c2):
    return (c1[0]*c2[0],c1[1]*c2[1])


def resta(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def division(c1, c2):
    real = (((c1[0] * c2[0]) + (c1[1] * c2[1])) / (c2[0] ** 2 + c2[1] ** 2))

    imag = (((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[1] ** 2) + (c2[0] ** 2)))

    return real, imag


def modulo(c1, c2):
    return (c1 ** 2 + c2 ** 2) ** 0.5


def conjugado(c1, c2):
    return c1, (c2 * -1)


def fase(c1, c2):
    theta = math.atan(c2 / c1)
    return theta


def polarCartesiano(c1, c2):
    a = int(c1 * math.cos(c2))
    b = int(c1 * math.sin(c2))
    return (a, b)

def multescalar(c,v):
    tamano=len(v)
    mult=[(0,0) for i in range(tamano)]
    j=0
    while j<tamano:
        mult[j]=producto(c.v[j])
        j=j+1
    return mult
        



if __name__ == '__main__':
    
    print(suma((3.5, 7), (4.2, 8)))
    print(producto((3, 2), (5, 0)))
    print(resta((1, 2), (2, 3)))
    print(division((2, 1), (5, 0)))
    print(modulo(1, 1))
    print(conjugado(2, 3))
    print(fase(1, 1))
    print(polarCartesiano(2 ** 0.5, 0.7853981633974483))


