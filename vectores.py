import operaciones as lc
def multescalarvector(c,v):
    tamano=len(v)
    mult=[(0,0) for i in range(tamano)]
    j=0
    while j<tamano:
        mult[j]= lc.productolineal(c,v[j])
        j=j+1
    return mult

def adicionvectorescomplejos(c,v):
    tamano=len(v)
    mult=[(0,0) for i in range(tamano)]
    j=0
    while j<tamano:
        mult[j]= lc.suma(c[j],v[j])
        j=j+1
    return mult
def inversoAditivovector(v):
    tamano=len(v)
    mult=[(0,0) for i in range(tamano)]
    j=0
    while j<tamano:
        mult[j]= lc.productolineal((-1,-1),v[j])
        j=j+1
    return mult



def producto_matrices(m1,m2):
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append((0, 0))
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    f = m1[i][k]
                    m = m2[k][j]

                    p = lc.producto(f, m)

                    m3[i][j] = lc.suma(m3[i][j], p)

        return m3


def main():
    # vector
    a= [(5, 0), (2, -1), (6, -4)]
    b = [(5, 0), (2, -1), (6, -4)]

    # matriz
    e = [[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1), (0, 0), (4, 0)]]
    w = [[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4), (2, 7), (0, 0)]]

    print(adicionvectorescomplejos(a,b))
    print(inversoAditivovector(b))
    print(multescalarvector((2, 3),a))
    print(producto_matrices(e,w))

main()
