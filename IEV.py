if __name__ == "__main__":
    file = open('rosalind_iev.txt', 'r').read()[:-1].split(' ')
    file = [ int(file[i]) for i in range(6)]
    ans = file[0] + file[1] + file[2] + 0.75*file[3] + 0.5*file[4]
    print(ans*2)
