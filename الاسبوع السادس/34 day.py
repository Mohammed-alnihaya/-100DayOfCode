def e_function(*name):
    print(name[1])



e_function('ali','mohammed','abudalh','linus')



def tri_recu(k):
    if(k>0):
        r=k+tri_recu(k-1)
        print(r)
    else:
        r=0
    return r

tri_recu(5)