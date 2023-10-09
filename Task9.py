def sum(a, b):
  n = len(a)
  c = [0] * (n + 1)
  k = 0
  for i in range(n - 1, -1, -1):
    sum = a[i] + b[i] + k
    c[i + 1] = sum % 2
    k = sum // 2

  c[0] = k
  return c


def main():
  with open("input9.txt", "r") as f:
    a, b = f.readline().split()

  c = sum(list(map(int, a)), list(map(int, b)))
  with open("output9.txt", "w") as f:
    f.write("".join(map(str, c)))

if __name__ == "__main__":
  main()