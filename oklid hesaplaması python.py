from math import sqrt

def euclideanDistance(points):
    distance = sqrt(((points[0][0] - points[1][0]) ** 2) + ((points[1][1] - points[0][1]) ** 2))
    return distance
def minimundistace(distances):
    min=distances[0]
    for i in range(len(distances)):
     if min>distances[i]:
      min = distances[i]
    return min


option = int(input("0 dersen döngü son bulur: "))
distances = []  # Boş bir liste oluşturun

while option != 0:
    x1 = input("Birinci noktanın x değerini giriniz: ")
    y1 = input("Birinci noktanın y değerini giriniz: ")
    x2 = input("İkinci noktanın x değerini giriniz: ")
    y2 = input("İkinci noktanın y değerini giriniz: ")

    points = [(float(x1), float(y1)), (float(x2), float(y2))]

    print("Öklid değeri:", euclideanDistance(points))
    distances.append(euclideanDistance(points))  # Listeye yeni değeri ekleyin
    print("Öklid en küçük değeri:", minimundistace(distances))
    option = int(input("0 dersen döngü son bulur: "))

print("Tüm Öklid değerleri:", distances)



