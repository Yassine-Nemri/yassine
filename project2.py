def menu():
    print("***********************************************")
    print(" *          1-Ajouter un contact          *")
    print(" *          2-modifier un contact         *")
    print(" *          3-supprimer un contact        *")
    print(" *          4-afficher tous les contacts  *")
    print(" *          5-affichier un contact        *")
    print("***********************************************")
    x = int(input("vote choix est"))
    if x==1:
        dict = {}
        dict['Nom'] = input('votre nom')
        dict['prenom'] = input('votre prenom')
        dict['Num tel:'] = input('write a number')
        dict['adress'] = input('write your adress')
        dict['Mail'] = input('write your mail')
        print (dict,'\n')
        print("ce contact a bien été enregistré.")
        fs=open('test.txt','a')
        fs.write(str(dict))
        fs.close
        print(menu())
    elif x==2:
        fs=open('test.txt','r')
        list=fs.readlines()
        for item in list:
            dict2 = {}
            m=input("write the user phone number")
        if m==item:
            print("***************************")
            print('ancien number=',x)
            dict2['Nom'] = input('votre nom')
            dict2['prenom'] = input('votre prenom')
            dict2['Num tel:'] = input('write a number')
            dict2['adress'] = input('write your adress')
            dict2['Mail'] = input('write your mail')
            print(dict2)
            fs.close()
            fs=(open("test.txt",'a'))
            fs.write(str(dict2))
            print(menu())
    elif x==3:
        N = False
        S = True
        import os
        fs=open('test.txt','r')
        list=fs.readlines()
        for item in list:
            m=input("write the user number")
            if m==x:
                print(x)
            print("taper",S, "pour supprimer si non taper",N)
            if S==True:
                os.system('cls')
        print('contact est supprimer taper',N, 'pour retourner')
        p = int(input("write a number"))
        if p == 0:
            print(menu())
        list.join(fs)
        fs.close()

    elif x==4:
        fs=open('test.txt','r')
        m=fs.readlines()
        fs.close()
        print("**********************")
        print(m)
        print("**********************")
    else:
        fs=open('test.txt','r')
        list=fs.readlines
        for item in list:
            x=input("write the contact number")
        if x==item:
            print('*******************')
            print(x)
            print('*******************')
        else:
            print('*******************')
            print('wrong number')
            print('*******************')
        list.join(fs)
        fs.close()
menu()


