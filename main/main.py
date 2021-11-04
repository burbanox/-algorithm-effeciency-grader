from bokeh.models import Range1d
from bokeh.plotting import figure,output_file,show
import random
import time
import algoritmos


def getCordinates(originalList,cordinates) :

    for i in range(len(originalList)) :
        cordinates["x"].append(originalList[i][0])
        cordinates["y"].append(originalList[i][1])

def graficarArreglos(bubble,insertion,merge,filename) :

    bubbleCords = {
        "x" : [],
        "y" : []
    }
    insertionCords = {
        "x" : [],
        "y" : []
    }
    mergeCords = {
        "x" : [],
        "y" : []
    }

    getCordinates(bubble,bubbleCords)
    getCordinates(insertion,insertionCords)
    getCordinates(merge,mergeCords)

    output_file(filename)
    graph = figure()
    graph.circle(bubbleCords["x"],bubbleCords["y"],color = "red")
    graph.circle(insertionCords["x"],insertionCords["y"],color = "green")
    graph.circle(mergeCords["x"],mergeCords["y"],color = "blue")
    show(graph)


def obtenerCordenadas(lista,funcion,arregloComplejidad,arregloTiempo) :

    l = len(lista)
    tiempoInicial = time.time()
    contador = funcion(lista)
    tiempoFinal = time.time()
    arregloComplejidad.append([l,contador])
    arregloTiempo.append([l,tiempoFinal - tiempoInicial])    


def main() :
    MAX = int(input("Rango maximo de los numeros = "))
    numeroDeListas = int(input("Numero de listas a ordenar = "))
    print("**********************")
    print("* Rojo = burbuja     *")
    print("* verde = insercion  *")
    print("* azul = merge       *")
    print("**********************")
    complexBubble = []
    complexInsertion = []
    complexMerge = []
    timeBubble = []
    timeInsertion = []
    timeMerge = []
    arr = []
    objeto = algoritmos.Algoritmos()

    for i in range(numeroDeListas) :

        arr  = [random.randint(0,MAX) for j in range(i)]

        obtenerCordenadas(arr.copy(),objeto.bubbleSort,complexBubble,timeBubble)
        obtenerCordenadas(arr.copy(),objeto.insertionSort,complexInsertion,timeInsertion)
        obtenerCordenadas(arr.copy(),objeto.mergeSort,complexMerge,timeMerge)


    graficarArreglos(complexBubble,complexInsertion,complexMerge,"complexity.html")
    graficarArreglos(timeBubble,timeInsertion,timeMerge,"time.html")

if __name__ == "__main__" :
    main()