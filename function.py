def listele(database,listele):
        imlec=database.cursor()
        kmt=listele
        imlec.execute(kmt)
        return  imlec
        


def parametreliSorgular(database,sorgu):
    imlec=database.cursor()
    kmt=sorgu
    imlec.execute(kmt)
    return imlec

def parametreliSorgular2(database,sorgu2):
    imlec=database.cursor()
    kmt=sorgu2
    
    return imlec
