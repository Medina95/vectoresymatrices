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

def sumamatrices(m1,m2):
    if len(m1[0]) == len(m2[0])  and len(m1) == len(m2) :
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append((0, 0))
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                m3[i][j]=lc.suma(m1[i][j],m2[i][j])

        return m3


def producto_matrices(m1,m2):
    if len(m1[0]) == len(m2[0])  and len(m1) == len(m2):
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


def TraspuestaMatriz(m1):
    if len(m1[0]) == len(m1):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append((0, 0))
        for i in range(len(m1)):
            for j in range(len(m1[0])):


                m3[i][j]= m1[j][i]
                m3[j][i]=m1[i][j]
        return m3
def inversamatriz(m1):
    m3=[]
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append((0, 0))
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            real=m1[i][j][0]
            imaginario=m1[i][j][1]
            m3[i][j]=lc.conjugado(real,imaginario)
    return m3

def mulescalarMatriz(c,m1):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append((0, 0))
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            p=m1[i][j]
            m3[i][j] = lc.producto(c,p )
    return m3

def conjugadamatriz(m1):
    m3=[]
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append((0, 0))
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            real=m1[i][j][0]
            imaginario=m1[i][j][1]
            m3[i][j]=lc.conjugado(real,imaginario)
    return m3
def main():
    # vector
    a= [(5, 0), (2, -1), (6, -4)]
    b = [(5, 0), (2, -1), (6, -4)]

    # matriz
    e = [[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1), (0, 0), (4, 0)]]
    w = [[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4), (2, 7), (0, 0)]]

    r = [[(1, 1), (1, -1)],[(1, -1), (1, 1)]]
    t = [[(1, -1), (1, 1)],[(1, 1), (1, -1)]]

    print(adicionvectorescomplejos(a,b))
    print(inversoAditivovector(b))
    print(multescalarvector((2, 3),a))
    print(sumamatrices(e, w))
    print (inversamatriz(e))
    print(mulescalarMatriz((2, 3), e))
    print(TraspuestaMatriz(e))
    print(conjugadamatriz(r))
    print(producto_matrices(e, w))




main()
