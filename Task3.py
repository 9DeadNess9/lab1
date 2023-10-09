with open("input3.txt", "r") as f:
  n = int(f.readline())
  mas = [int(x) for x in f.readline().split()]
def insertion_sort(mas):
  for i in range(1, len(mas)):
    key = mas[i]
    j = i - 1

    while j >= 0 and mas[j] < key:
      swap(mas, j, j + 1)
      j -= 1

    if j >= 0:
      mas[j + 1] = key

def swap(mas, i, j):
  temp = mas[i]
  mas[i] = mas[j]
  mas[j] = temp

insertion_sort(mas)
with open("output3.txt", "w") as f:
  f.write(" ".join([str(x) for x in mas]))