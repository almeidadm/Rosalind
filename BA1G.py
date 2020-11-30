def HammingDistance(p, q):
    count = 0
    for i, j in zip(p, q):
        if i != j:
            count += 1
    return count

if __name__ == "__main__":
  p, q, _ = open("./rosalind_ba1g.txt", "r").read().split("\n")
  print(HammingDistance(p,q))
