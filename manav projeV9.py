###########TOPTANCI#############
print("TOPTANCI")



meyvetoptanci = ["elma", 1000, "armut", 1000, "kiraz", 1000, "muz", 1000, "çilek", 1000]
sebzetoptanci = ["sarımsak", 1000, "domates", 1000, "patlıcan", 1000, "soğan", 1000, "patates", 1000]
meyvemanav = []
sebzemanav = []
meyvemusteri = []
sebzemusteri = []
while True:
    toptancisoru1 = input("Meyve mi istersiniz yoksa sebze mi?").lower().strip()
    if toptancisoru1 == "meyve":
        toptancisoru2 = input("Elma,armut,kiraz,muz,çilek hangisi?").lower().strip()
        if toptancisoru2 == "elma":
            if "elma" not in meyvemanav:
                meyvemanav.append("elma")
                toptancisoru3 = int(input("Kaç kilo?"))
                elmakg = meyvemanav.index("elma") + 1
                if toptancisoru3 == 0:
                    meyvemanav.remove("elma")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif meyvetoptanci[1] <= 0:
                    print("Elma tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[1]:
                    meyvemanav.remove("elma")
                    print("İstediğiniz kiloda elma elimizde yok!!")
                    continue
                meyvemanav.append(toptancisoru3)
                meyvetoptanci[1] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                elmakg = meyvemanav.index("elma")+1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif meyvetoptanci[1] <= 0:
                    print("Elma tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[1]:
                    meyvemanav.remove("elma")
                    print("İstediğiniz kiloda elma elimizde yok!!")
                    continue
                meyvemanav[elmakg] += toptancisoru3
                meyvetoptanci[1] -= toptancisoru3
        elif toptancisoru2 == "armut":
            if "armut" not in meyvemanav:
                meyvemanav.append("armut")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    meyvemanav.remove("armut")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif meyvetoptanci[3] <= 0:
                    print("Armut tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[3]:
                    meyvemanav.remove("armut")
                    print("İstediğiniz kiloda armut elimizde yok!!")
                    continue
                meyvemanav.append(toptancisoru3)
                meyvetoptanci[3] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                armutkg = meyvemanav.index("armut")+1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif meyvetoptanci[3] <= 0:
                    print("Armut tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[3]:
                    meyvemanav.remove("armut")
                    print("İstediğiniz kiloda armut elimizde yok!!")
                    continue
                meyvemanav[armutkg] += toptancisoru3
                meyvetoptanci[3] -= toptancisoru3
        elif toptancisoru2 == "kiraz":
            if "kiraz" not in meyvemanav:
                meyvemanav.append("kiraz")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    meyvemanav.remove("kiraz")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif meyvetoptanci[5] <= 0:
                    print("Kiraz tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[5]:
                    meyvemanav.remove("kiraz")
                    print("İstediğiniz kiloda kiraz elimizde yok!!")
                    continue
                meyvemanav.append(toptancisoru3)
                meyvetoptanci[5] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                kirazkg = meyvemanav.index("kiraz")+1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif meyvetoptanci[5] <= 0:
                    print("Kiraz tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[5]:
                    meyvemanav.remove("kiraz")
                    print("İstediğiniz kiloda kiraz elimizde yok!!")
                    continue
                meyvemanav[kirazkg] += toptancisoru3
                meyvetoptanci[5] -= toptancisoru3
        elif toptancisoru2 == "muz":
            if "muz" not in meyvemanav:
                meyvemanav.append("muz")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    meyvemanav.remove("muz")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif meyvetoptanci[7] <= 0:
                    print("Muz tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[7]:
                    meyvemanav.remove("muz")
                    print("İstediğiniz kiloda muz elimizde yok!!")
                    continue
                meyvemanav.append(toptancisoru3)
                meyvetoptanci[7] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                muzkg = meyvemanav.index("muz")+1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif meyvetoptanci[7] <= 0:
                    print("Muz tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[7]:
                    meyvemanav.remove("muz")
                    print("İstediğiniz kiloda muz elimizde yok!!")
                    continue
                meyvemanav[muzkg] += toptancisoru3
                meyvetoptanci[7] -= toptancisoru3
        elif toptancisoru2 == "çilek":
            if "çilek" not in meyvemanav:
                meyvemanav.append("çilek")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    meyvemanav.remove("çilek")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif meyvetoptanci[9] <= 0:
                    print("Çilek tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[9]:
                    meyvemanav.remove("çilek")
                    print("İstediğiniz kiloda çilek elimizde yok!!")
                    continue
                meyvemanav.append(toptancisoru3)
                meyvetoptanci[9] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                cilekkg = meyvemanav.index("çilek")+1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif meyvetoptanci[9] <= 0:
                    print("Çilek tükenmiştir")
                elif toptancisoru3 > meyvetoptanci[9]:
                    meyvemanav.remove("çilek")
                    print("İstediğiniz kiloda çilek elimizde yok!!")
                    continue
                meyvemanav[cilekkg] += toptancisoru3
                meyvetoptanci[9] -= toptancisoru3
        else:
            print("Hatalı giriş yaptınız!!!")
            continue
        toptancisoru4 = input("Başka bir aruzunuz var mı? Evet yada hayır:").lower().strip()
        if toptancisoru4 == "evet":
            continue
        elif toptancisoru4 == "hayır":
            break
        else:
            print("Hatalı giriş yaptınız!!!")
            continue
    elif toptancisoru1 == "sebze":
        toptancisoru2 = input("Sarımsak,domates,patlıcan,soğan,patates hangisi?").lower().strip()
        if toptancisoru2 == "sarımsak":
            if "sarımsak" not in sebzemanav:
                sebzemanav.append("sarımsak")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    sebzemanav.remove("sarımsak")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif sebzetoptanci[1] <= 0:
                    print("Sarımsak tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[1]:
                    print("İstediğiniz kiloda sarımsak elimizde yok!!")
                    sebzemanav.remove("sarımsak")
                    continue
                sebzemanav.append(toptancisoru3)
                sebzetoptanci[1] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                sarimsakkg = sebzemanav.index("sarımsak") + 1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif sebzetoptanci[1] <= 0:
                    print("Sarımsak tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[1]:
                    sebzemanav.remove("sarımsak")
                    print("İstediğiniz kiloda sarımsak elimizde yok!!")
                    continue
                sebzemanav[sarimsakkg] += toptancisoru3
                sebzetoptanci[1] -= toptancisoru3
        elif toptancisoru2 == "domates":
            if "domates" not in sebzemanav:
                sebzemanav.append("domates")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    sebzemanav.remove("domates")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif sebzetoptanci[3] <= 0:
                    print("Domates tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[3]:
                    sebzemanav.remove("domates")
                    print("İstediğiniz kiloda domates elimizde yok!!")
                    continue
                sebzemanav.append(toptancisoru3)
                sebzetoptanci[3] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                domateskg = sebzemanav.index("domates") + 1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif sebzetoptanci[3] <= 0:
                    print("Domates tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[3]:
                    sebzemanav.remove("domates")
                    print("İstediğiniz kiloda domates elimizde yok!!")
                    continue
                sebzemanav[domateskg] += toptancisoru3
                sebzetoptanci[3] -= toptancisoru3
        elif toptancisoru2 == "patlıcan":
            if "patlıcan" not in sebzemanav:
                sebzemanav.append("patlıcan")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    sebzemanav.remove("patlıcan")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif sebzetoptanci[5] <= 0:
                    print("Patlıcan tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[5]:
                    sebzemanav.remove("patlıcan")
                    print("İstediğiniz kiloda patlıcan elimizde yok!!")
                    continue
                sebzemanav.append(toptancisoru3)
                sebzetoptanci[5] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                patlicankg = sebzemanav.index("patlıcan") + 1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif sebzetoptanci[5] <= 0:
                    print("Patlıcan tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[5]:
                    sebzemanav.remove("patlıcan")
                    print("İstediğiniz kiloda patlıcan elimizde yok!!")
                    continue
                sebzemanav[patlicankg] += toptancisoru3
                sebzetoptanci[5] -= toptancisoru3
        elif toptancisoru2 == "soğan":
            if "soğan" not in sebzemanav:
                sebzemanav.append("soğan")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    sebzmanav.remove("soğan")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif sebzetoptanci[7] <= 0:
                    print("Soğan tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[7]:
                    sebzemanav.remove("soğan")
                    print("İstediğiniz kiloda soğan elimizde yok!!")
                    continue
                sebzemanav.append(toptancisoru3)
                sebzetoptanci[7] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                sogankg = sebzemanav.index("soğan") + 1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif sebzetoptanci[7] <= 0:
                    print("Soğan tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[7]:
                    sebzemanav.remove("soğan")
                    print("İstediğiniz kiloda soğan elimizde yok!!")
                    continue
                sebzemanav[sogankg] += toptancisoru3
                sebzetoptanci[7] -= toptancisoru3
        elif toptancisoru2 == "patates":
            if "patates" not in sebzemanav:
                sebzemanav.append("patates")
                toptancisoru3 = int(input("Kaç kilo?"))
                if toptancisoru3 == 0:
                    sebzemanav.remove("patates")
                    print("0 değerini giremezsiniz!!!")
                    continue
                elif sebzetoptanci[9] <= 0:
                    print("Patates tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[9]:
                    sebzemanav.remove("patates")
                    print("İstediğiniz kiloda patates elimizde yok!!")
                    continue
                sebzemanav.append(toptancisoru3)
                sebzetoptanci[9] -= toptancisoru3
            else:
                toptancisoru3 = int(input("Kaç kilo?"))
                patateskg = sebzemanav.index("patates") + 1
                if toptancisoru3 == 0:
                    print("0 değerini giremezsiniz!!!")
                elif sebzetoptanci[9] <= 0:
                    print("Patates tükenmiştir")
                elif toptancisoru3 > sebzetoptanci[9]:
                    sebzemanav.remove("patates")
                    print("İstediğiniz kiloda patates elimizde yok!!")
                    continue
                sebzemanav[patateskg] += toptancisoru3
                sebzetoptanci[9] -= toptancisoru3
    else:
        print("Hatalı giriş yaptınız!!!")
        continue
    toptancisoru4 = input("Başka bir aruzunuz var mı? Evet yada hayır:").lower().strip()
    if toptancisoru4 == "evet":
        continue
    elif toptancisoru4 == "hayır":
        break
    else:
        print("Hatalı giriş yaptınız!!!")
    continue



########MANAV#######
print("MANAV")



while True:
    manavsoru1 = input("Meyve mi istersiniz yoksa sebze mi?").lower().strip()
    if manavsoru1 == "meyve":
        print("Elimizde olanlar:", meyvemanav)
        if len(meyvemanav) == 0:
            print("Elimizde hiç meyve yok!!!")
            continue
        manavsoru2 = input("Hangi meyveyi istersiniz?").lower().strip()
        if manavsoru2 == "elma" and "elma" in meyvemanav:
            elmakg = meyvemanav.index("elma") + 1
            if meyvemanav[elmakg] == 0:
                del meyvemanav[elmakg]
                meyvemanav.remove("elma")
                print("Elma tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "elma" not in meyvemusteri:
                meyvemusteri.append("elma")
            if manavsoru3 > meyvemanav[elmakg]:
                print("İstediğiniz kiloda elma elimizde yok!!")
                print(meyvemanav)
                meyvemusteri.remove("elma")
                continue
            elif manavsoru3 <= meyvemanav[elmakg]:
                meyvemanav[elmakg] -= manavsoru3
                meyvemusteri.append(manavsoru3)
        elif manavsoru2 == "armut" and "armut" in meyvemanav:
            armutkg = meyvemanav.index("armut") + 1
            if meyvemanav[armutkg] == 0:
                del meyvemanav[armutkg]
                meyvemanav.remove("armut")
                meyvemusteri.remove("armut")
                print("Armut tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "armut" not in meyvemusteri:
                meyvemusteri.append("armut")
            if manavsoru3 > (meyvemanav[armutkg]):
                print("İstediğiniz kiloda armut elimizde yok!!")
                meyvemusteri.remove("armut")
                continue
            elif manavsoru3 <= meyvemanav[armutkg]:
                meyvemanav[armutkg] -= manavsoru3
                meyvemusteri.append(manavsoru3)
        elif manavsoru2 == "kiraz" and "kiraz" in meyvemanav:
            kirazkg = meyvemanav.index("kiraz") + 1
            if meyvemanav[kirazkg] == 0:
                del meyvemanav[kirazkg]
                meyvemanav.remove("kiraz")
                meyvemusteri.remove("kiraz")
                print("Kiraz tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "kiraz" not in meyvemusteri:
                meyvemusteri.append("kiraz")
            if manavsoru3 > (meyvemanav[kirazkg]):
                print("İstediğiniz kiloda kiraz elimizde yok!!")
                meyvemusteri.remove("kiraz")
                continue
            elif manavsoru3 <= meyvemanav[kirazkg]:
                meyvemanav[kirazkg] -= manavsoru3
                meyvemusteri.append(manavsoru3)
        elif manavsoru2 == "muz" and "muz" in meyvemanav:
            muzkg = meyvemanav.index("muz") + 1
            if meyvemanav[muzkg] == 0:
                del meyvemanav[muzkg]
                meyvemanav.remove("muz")
                meyvemusteri.remove("muz")
                print("Muz tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "muz" not in meyvemusteri:
                meyvemusteri.append("muz")
            if manavsoru3 > (meyvemanav[muzkg]):
                print("İstediğiniz kiloda muz elimizde yok!!")
                meyvemusteri.remove("muz")
                continue
            elif manavsoru3 <= meyvemanav[muzkg]:
                meyvemanav[muzkg] -= manavsoru3
                meyvemusteri.append(manavsoru3)
        elif manavsoru2 == "çilek" and "çilek" in meyvemanav:
            cilekkg = meyvemanav.index("çilek") + 1
            if meyvemanav[cilekkg] == 0:
                del meyvemanav[cilekkg]
                meyvemanav.remove("çilek")
                meyvemusteri.remove("çilek")
                print("Çilek tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "çilek" not in meyvemusteri:
                meyvemusteri.append("çilek")
            if manavsoru3 > (meyvemanav[cilekkg]):
                print("İstediğiniz kiloda çilek elimizde yok!!")
                meyvemusteri.remove("çilek")
                continue
            elif manavsoru3 <= meyvemanav[cilekkg]:
                meyvemanav[cilekkg] -= manavsoru3
                meyvemusteri.append(manavsoru3)
        elif manavsoru2 not in meyvemanav:
            print("Elimizde yok yada hatalı değer girdiniz!!!")
            continue
        manavsoru4 = input("Başka bir aruzunuz var mı? Evet yada hayır:").lower().strip()
        if manavsoru4 == "evet":
            continue
        elif manavsoru4 == "hayır":
            break
        else:
            print("Hatalı giriş yaptınız!!!")
            continue
    elif manavsoru1 == "sebze":
        print("Elimizde olanlar:", sebzemanav)
        if len(sebzemanav) == 0:
            print("Elimizde hiç sebze yok!!!")
            continue
        manavsoru2 = input("Hangi sebzeyi istersiniz?").lower().strip()
        if manavsoru2 == "sarımsak" and "sarımsak" in sebzemanav:
            sarimsakkg = sebzemanav.index("sarımsak") + 1
            if sebzemanav[sarimsakkg] == 0:
                del sebzemanav[sarimsakkg]
                meyvemanav.remove("sarımsak")
                meyvemusteri.remove("sarımsak")
                print("Sarımsak tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "sarımsak" not in sebzemusteri:
                sebzemusteri.append("sarımsak")
            if manavsoru3 > sebzemanav[sarimsakkg]:
                print("İstediğiniz kiloda sarımsak elimizde yok!!")
                sebzemusteri.remove("sarımsak")
                continue
            elif manavsoru3 <= sebzemanav[sarimsakkg]:
                sebzemanav[sarimsakkg] -= manavsoru3
                sebzemusteri.append(manavsoru3)

        elif manavsoru2 == "domates" and "domates" in sebzemanav:
            domateskg = sebzemanav.index("domates") + 1
            if sebzemanav[domateskg] == 0:
                del sebzemanav[domateskg]
                meyvemanav.remove("domates")
                meyvemusteri.remove("domates")
                print("Domates tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "domates" not in sebzemusteri:
                sebzemusteri.append("domates")
            if manavsoru3 > sebzemanav[domateskg]:
                print("İstediğiniz kiloda domates elimizde yok!!")
                sebzemusteri.remove("domates")
                continue
            elif manavsoru3 <= sebzemanav[domateskg]:
                sebzemanav[domateskg] -= manavsoru3
                sebzemusteri.append(manavsoru3)
        elif manavsoru2 == "patlıcan" and "patlıcan" in sebzemanav:
            patlicankg = sebzemanav.index("patlıcan") + 1
            if sebzemanav[patlicankg] == 0:
                del sebzemanav[patlicankg]
                meyvemanav.remove("patlıcan")
                meyvemusteri.remove("patlıcan")
                print("Patlıcan tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "patlıcan" not in sebzemusteri:
                sebzemusteri.append("patlıcan")
            if manavsoru3 > sebzemanav[patlicankg]:
                print("İstediğiniz kiloda patlıcan elimizde yok!!")
                sebzemusteri.remove("patlıcan")
                continue
            elif manavsoru3 <= sebzemanav[patlicankg]:
                sebzemanav[patlicankg] -= manavsoru3
                sebzemusteri.append(manavsoru3)
        elif manavsoru2 == "soğan" and "soğan" in sebzemanav:
            sogankg = sebzemanav.index("soğan") + 1
            if sebzemanav[sogankg] == 0:
                del sebzemanav[sogankg]
                meyvemanav.remove("sogan")
                meyvemusteri.remove("soğan")
                print("Soğan tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "soğan" not in sebzemusteri:
                sebzemusteri.append("soğan")
            if manavsoru3 > sebzemanav[sogankg]:
                print("İstediğiniz kiloda soğan elimizde yok!!")
                sebzemusteri.remove("soğan")
                continue
            elif manavsoru3 <= sebzemanav[sogankg]:
                sebzemanav[sogankg] -= manavsoru3
                sebzemusteri.append(manavsoru3)
        elif manavsoru2 == "patates" and "patates" in sebzemanav:
            patateskg = sebzemanav.index("patates") + 1
            if sebzemanav[patateskg] == 0:
                del sebzemanav[patateskg]
                meyvemanav.remove("patates")
                meyvemusteri.remove("patates")
                print("Patates tükenmiştir")
                continue
            manavsoru3 = int(input("Kaç kilo?"))
            if "patates" not in sebzemusteri:
                sebzemusteri.append("patates")
            if manavsoru3 > sebzemanav[patateskg]:
                print("İstediğiniz kiloda patates elimizde yok!!")
                sebzemusteri.remove("patates")
                continue
            elif manavsoru3 <= sebzemanav[patateskg]:
                sebzemanav[patateskg] -= manavsoru3
                sebzemusteri.append(manavsoru3)
            elif manavsoru2 not in sebzemanav:
                print("Elimizde yok yada hatalı değer girdiniz!!!")
                continue
        manavsoru4 = input("Başka bir aruzunuz var mı? Evet yada hayır:").lower().strip()
        if manavsoru4 == "evet":
            continue
        elif manavsoru4 == "hayır":
            break
        else:
            print("Hatalı giriş yaptınız!!!")
            continue
    else:
        print("Hatalı giriş yaptınız!!!")
        continue



######MÜŞTERİ#####
print("MÜŞTERİ")


print("Müşteri tarafından satın alınan meyveler:", meyvemusteri)
print("Müşteri tarafından satın alınan sebzeler:", sebzemusteri)