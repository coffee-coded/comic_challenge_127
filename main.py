if __name__=="__main__":
    n = int(input("Amount vinay can spend on comics : "))
    c = int(input("Cost of each comic : "))
    b = int(input("comic covers to receive another comic : "))
    comics = n//c
    covers_remain = comics
    while covers_remain>=b:
        comics=comics+1
        covers_remain=covers_remain-b
        covers_remain=covers_remain+1
    print(comics)
