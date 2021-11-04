
class Algoritmos :

    def __init__(self):
        pass

    def bubbleSort(self,lista) :

        n = len(lista)
        contador = 0

        for i in range(n) :
            for j in range(n - i - 1) :
                contador+=1
                if lista[j] > lista[j + 1] :
                    lista[j],lista[j +1] = lista[j+1],lista[j]

        return contador

    def insertionSort(self,arr):
        contador = 0
        for i in range(1, len(arr)): 
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                contador+=1
            arr[j+1] = key

        return contador

    def mergeSort(self,lista) :
        if len(lista) > 1 :

            medium = len(lista)//2
            left = lista[:medium]
            rigth = lista[medium:]

            contador=self.mergeSort(left)
            contador+=self.mergeSort(rigth)

            i = 0
            j = 0
            k = 0

            while(i<len(left) and j<len(rigth)) :
                if left[i] <= rigth[i] :
                    lista[k] = left[i] 
                    i+=1
                else :
                    lista[k] = rigth[j]
                    j += 1
                k+=1

            while i<len(left) :
                lista[k] = left[i]
                i+=1
                k+=1

            while j<len(rigth) :
                lista[k] = rigth[j]
                j+=1
                k+=1

            return contador + k
            
        return 1


