def read_obj(filename):
    vs = []
    qfs = []
    fs = []
    with open(filename,"rt") as f:
        for line in f:
            if line.startswith('v '):
                vs.append([float(x) for x in line.split()[1:]])
            if line.startswith('f '):
                qfs = [int(x.split('/')[0])-1 for x in line.split()[1:]]
                if len(qfs) == 3: # c'est un triangle
                    fs.append(qfs)
                elif len(qfs) == 4: # c'est un quad, on en fait 2 triangles
                    fs.append([qfs[0], qfs[1], qfs[2]])
                    fs.append([qfs[2], qfs[3], qfs[0]])
                #faces.append([int(x.split('/')[0])-1 for x in line.split()[1:]])

    return vs, fs


def center_origin(vertices):
    # calcule le centre de gravité des vertices
    center = [sum([v[i] for v in vertices])/len(vertices) for i in range(3)]
    # translate les vertices pour les recentrer
    return [[v[i]-center[i] for i in range(3)] for v in vertices]