class Versenyzok():
    def __init__(self, list1, list2):
        self.name = list1[0]
        self.birth = list1[1]
        self.birth_y = int(list1[1].split(".")[0])
        self.birth_m = int(list1[1].split(".")[1])
        self.birth_d = int(list1[1].split(".")[2])
        self.gender = list1[2]
        self.points = float(list2[1])
        
    def __str__(self):
        return f"Name: {self.name}, Birth: {self.birth}, Birth_y: {self.birth_y}, Birth_m: {self.birth_m}, Birth_d: {self.birth_d}, Gender: {self.gender}, Points: {self.points}"

def beolvas():
    temp_list = []
    f = open("start.txt", "r", encoding="utf8").read().strip().split("\n")
    g = open("final.txt", "r", encoding="utf8").read().strip().split("\n")
    for i in range(len(f)):
        if i == 0:
            pass
        else:
            if g[i] != [] or g[i] != None and f[i] != [] or f[i] != None:
                temp_list.append(Versenyzok(f[i].split("\t"), g[i].split("\t")))
    return temp_list

def partition(lista, low, high):
    pivot = lista[high]
    i = low - 1
    for j in range(low, high):
        if lista[j] <= pivot:
            i = i + 1
            (lista[i], lista[j]) = (lista[j], lista[i])
    (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
    return i + 1
 
 
def quickSort(lista, low, high):
    if low < high:
        pi = partition(lista, low, high)
        quickSort(lista, low, pi - 1)
        quickSort(lista, pi + 1, high)

def findF(lista):
    temp = []
    for i in lista:
        if i.gender == "n":
            temp.append(i)
    return temp


def genRankList(lista, place):
    size = len(lista)
    temp = lista
    quickSort(lista, 0, size - 1)
    return temp[place]

def fel1(lista):
    return len(lista)

def fel2(lista):
    return len(findF(lista))

def fel3(lista, y, m, d):
    temp = 0
    for i in lista:
        if i.birth_y > y-14 or i.birth_y == y-14 and i.birth_m > m or i.birth_y == y-14 and i.birth_m == m and i.birth_d > d:
            temp += 1
    return temp

def fel4(lista):
    g_points = 0
    for i in findF(lista):
        g_points += i.points
    if list[genRankList(lista, 0)].points < g_points:
        return f"lányoknak"
    return f"bajnoknak"

def fel5(lista):
    for i in range(0, 2, 1):
        print(genRankList(lista, i).name)

def main():
    main_list = beolvas()
    print(f"1. feladat: {fel1(main_list)}")
    print(f"2. feladat: {fel2(main_list)}")
    print(f"3. feladat: {fel3(main_list, 2023, 4, 30)}")
    print(f"4. feladat: A {fel4(main_list)} van több pontja")
main()