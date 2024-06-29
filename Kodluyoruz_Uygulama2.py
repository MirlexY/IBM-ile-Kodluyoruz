import math

#1-Noktaların Tanımlanması:
points = [(1, 2), (3, 5), (-1, 0), (4, 2), (0, 0)]

#2-Öklid Mesafesi İçin Bir Fonksiyon Yazma:
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#3-Mesafelerin hesaplanması ve distances listesine eklenmesi:
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

#4-Minimum mesafenin bulunması:
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
