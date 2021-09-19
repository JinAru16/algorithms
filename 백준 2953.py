maxGrade = 0
maxIndex = 0

for i in range(5):
    g1, g2, g3, g4 = map(int, input().split())
    grade = (g1 + g2 + g3 + g4)
    if grade > maxGrade:
        maxGrade = grade
        maxIndex = i + 1

print(maxIndex, maxGrade)
