from ursina import *
from table import BPiece, WPiece

def pieces():
    modelos = [ 'cube',
               'assets/fichas/rook/scene.gltf',
               'assets/fichas/bishop/scene.gltf',
               'assets/fichas/knight/scene.gltf',
               'assets/fichas/king/scene.gltf',
               'assets/fichas/queen/scene.gltf',
               'assets/fichas/pawn/scene.gltf']
    model = modelos[0]

    lista1 =[(1,1),(0,1),
             (1,2),(0,2),
             (1,3),(0,3),
             (1,4),(0,4),
             (1,5),(0,5),
             (1,6),(0,6),
             (1,7),(0,7),
             (1,0),(0,0)]
    def numero(lista1):
        hola = random.choice(lista1)
        lista1.remove(hola)
        return hola
    
    def pos():
                t = numero(lista1)
                if t[0] == 0:
                        w = 7
                else:
                        w = 5
                pieza = WPiece(model= x, position = (t[1],y,t[0]))
                pieza = BPiece(model= x, position = (t[1] ,y,t[0] + w))
           
    y = 1.35
    z= 0
    for x in modelos:       
        if z == 1:
            pos()
            pos()
        if z == 2:
           pos()
           pos()
        if z ==3:
           pos()
           pos()
        if z ==4:
           pos()
        if z ==5:
          pos()
        if z == 6:
            for i in range(8):
                pos()
        z += 1