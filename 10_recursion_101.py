
def func(n,m):   
    if n > 5:
        return
    func(n+1,m)
    print("Hello n: ", n)
    print("m: ", m)

if __name__ == "__main__":
    func(1,4)
