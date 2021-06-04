class Vector:
    def __init__(self, vec):
       self.vec = vec

    def __str__(self):
       str1 = ""
       index = 0
       for i in self.vec:
           str1 += f' {i} a{index} +'
           index += 1
       return str1[:-1]
    
    def __add__(self, vec1):
        newVector = []
        for i in range(len(self.vec)):
            newVector.append(self.vec[i] + vec1.vec[i])
        return Vector(newVector)

    def __mul__(self, vec1):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec1.vec[i]
        return sum

v1 = Vector([1, 4, 6])
v2 = Vector([4, 1, 9])
print (v1 + v2)
print (v1 * v2)
