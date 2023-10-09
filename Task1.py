with open("input.txt", "r") as f:
  n = int(f.readline())
  mas = [int(x) for x in f.readline().split()]

for i in range(1, len(mas)):
  for j in range(i - 1, -1, -1):
    if mas[j] > mas[j + 1]:
      mas[j], mas[j + 1] = mas[j + 1], mas[j]

with open("output.txt", "w") as f:
  f.write(" ".join([str(x) for x in mas]))