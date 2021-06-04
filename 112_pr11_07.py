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
        if(len(self.vec) == len(vec1.vec)):
            newVector = []
            for i in range(len(self.vec)):
                newVector.append(self.vec[i] + vec1.vec[i])
            return f'Sum of two vector is {Vector(newVector)}'
        else:
            return 'Length of both vectors are not same.'

    def __mul__(self, vec1):
        if(len(self.vec) == len(vec1.vec)):
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec1.vec[i]
            return f'Dot product of two vector is {sum}'
        else:
            return 'Length of both vectors are not same.'

    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 4])
v2 = Vector([4, 1, 9, 5])
print (v1 + v2)
print (v1 * v2)
print (len(v1))
print (len(v2))