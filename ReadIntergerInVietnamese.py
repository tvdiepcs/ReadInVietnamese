DonVi=["Khong","Mot","Hai","Ba","Bon","Nam","Sau","Bay","Tam","Chin"]
motNghin=1000
motTrieu=1000000
motTy=1000000000
def hangChuc(n):
    if(n<20):
        if(n==15):
            return "Muoi"+" Lam"
        if(n==10):
            return "Muoi "
        return "Muoi "+DonVi[n-10]
    if(n<100):
        if(n%10==5):
            return DonVi[int(n/10)]+" Muoi Lam"
        if(n%10==0):
            return DonVi[int(n/10)]+" Muoi"
        return DonVi[int(n/10)]+" Muoi "+DonVi[n%10]
def hangTram(n):
    if(n>=10 and n<=99):
            return "Khong Tram " + hangChuc(n)
    if(n%100==0):
        return DonVi[int(n/100)]+" Tram "
    if(n%100<10):
        return DonVi[int(n/100)]+" Tram Le "+DonVi[n%10]
    elif(n<1000):
        return DonVi[int(n/100)]+" Tram "+hangChuc(n%100)
def hangNghin(n):
    if(n%1000==0):
        if(int(n/1000)<10):
            return DonVi[int(n/1000)]+ " Nghin "
        elif(int(n/1000)<100):
            return hangChuc(int(n/1000))+ " Nghin "
        elif(int(n/1000)<1000):
            return hangTram(int(n/1000))+" Nghin "
    if(n<1010):
        return DonVi[int(n/1000)]+" Nghin Le "+DonVi[n%1000]
    elif(n<1100):
        return DonVi[int(n/1000)]+" Nghin "+hangTram(n%100)
    elif(n<10000):
        return DonVi[int(n/1000)]+" Nghin "+hangTram(n%1000)
    elif(n<100000):
        return hangChuc(int(n/1000))+" Nghin "+hangTram(n%1000)
    elif(n<1000000):
            return hangTram(int(n/1000))+ " Nghin "+hangTram(n%1000)
def hangTrieu(n):
    if(n%1000000==0):
        if(int(n/1000000)<10):
            return DonVi[int(n/1000000)]+ " Trieu "
        elif(int(n/1000000)<100):
            return hangChuc(int(n/1000000))+ " Trieu "
        elif(int(n/1000000)<1000):
            return hangTram(int(n/1000000))+" Trieu "
    elif(n<10*motTrieu):
        if(n%1000000<1000):
            return DonVi[int(n/1000000)]+" Trieu "+hangTram(n%1000000)
        else:
            return DonVi[int(n/1000000)]+" Trieu "+hangNghin(n%1000000)
    elif(n<100*motTrieu):
        if(n%1000000<1000):
            return hangChuc(int(n/1000000))+" Trieu "+hangTram(n%1000000)
        else:
            return hangChuc(int(n/1000000))+" Trieu "+hangNghin(n%1000000)
    elif(n<motTy):
        if(n%motTrieu<1000):
            return hangTram(int(n/1000000))+" Trieu "+hangTram(n%1000000)
        else:
            return hangTram(int(n/1000000))+" Trieu "+hangNghin(n%1000000)
def hangTy(n):
    soTy=int(n/motTy)
    if(n%motTy==0):
        if(soTy<10):
            return DonVi[soTy]+" Ty "
        elif(soTy<100):
            return hangChuc(soTy)+ " Ty "
        elif(soTy<1000):
            return hangTram(soTy)+ " Ty "
        elif(soTy<motTrieu):
            return hangNghin(soTy)+" Ty "
        elif(soTy<motTy):
            return hangTrieu(soTy)+" Ty "
    elif(n<10*motTy):
        if(n%motTy<1000):
            return DonVi[soTy]+" Ty "+hangTram(n%motTy)
        elif(n%motTy<motTrieu):
            return DonVi[soTy]+" Ty "+hangNghin(n%motTy)
        else:
            return DonVi[soTy]+" Ty "+hangTrieu(n%motTy)
    elif(n<100*motTy):
        if(n%motTy<1000):
            return hangChuc(soTy)+" Ty "+hangTram(n%motTy)
        elif(n%motTy<motTrieu):
            return hangChuc(soTy)+" Ty "+hangNghin(n%motTy)
        else:
            return hangChuc(soTy)+" Ty "+hangTrieu(n%motTy)
    elif(n<1000*motTy):
        if(n%motTy<1000):
            return hangTram(soTy)+" Ty "+hangTram(n%motTy)
        elif(n%motTy<motTrieu):
            return hangTram(soTy)+" Ty "+hangNghin(n%motTy)
        else:
            return hangTram(soTy)+" Ty "+hangTrieu(n%motTy)
    elif(n<motTrieu*motTy):
        if(n%motTy<1000):
            return hangNghin(soTy)+" Ty "+hangTram(n%motTy)
        elif(n%motTy<motTrieu):
            return hangNghin(soTy)+" Ty "+hangNghin(n%motTy)
        else:
            return hangNghin(soTy)+" Ty "+hangTrieu(n%motTy)
    elif(n<motTy*motTy):
        if(n%motTy<1000):
            return hangTrieu(soTy)+" Ty "+hangTram(n%motTy)
        elif(n%motTy<motTrieu):
            return hangTrieu(soTy)+" Ty "+hangNghin(n%motTy)
        else:
            return hangTrieu(soTy)+" Ty "+hangTrieu(n%motTy)
def main():
    print("Nhap vao so can doc: ")
    n=int(input())
    print("So vua nhap duoc doc la: ")
    if(n<10):
        print(DonVi[n])
    elif(n<100):
        print(hangChuc(n))
    elif(n<1000):
        print(hangTram(n))
    elif(n<1000000):
        print(hangNghin(n))
    elif(n<1000000000):
        print(hangTrieu(n))
    else:
        print(hangTy(n))
if __name__ == "__main__":
    main()