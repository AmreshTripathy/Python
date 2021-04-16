

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        runningtotal = 0
        for i in range(1, n+1):
            if n%i == 0:
                runningtotal += i
        return runningtotal

