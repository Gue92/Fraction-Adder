from Fraction_Adder_Application import add_frac

def add_frac_test(Zaehler1,Nenner1,Zaehler2,Nenner2):
  
    Liste = [Zaehler1,Nenner1,Zaehler2,Nenner2]
    Nen1=Nenner1
    Nen2=Nenner2
    Counter=1
    ggt=1
    if Nenner1 == 0 or Nenner2 == 0:
        print("!!! Error : Division by ZERO !!!")
    else:                
        if Nenner1 > Nenner2:     # Nenner1 Erweiterung auf Nenner2 - Vielfaches
            while Nenner1 % Nenner2 != 0:
                Nenner1 = Nenner1 + Nen1
                Counter = Counter + 1
        if Nenner1 > Nenner2 and Nenner1 % Nenner2 == 0:
            Faktor = int(Nenner1/Nenner2)  #  Zähler2 Anpassung
            Zaehlerneu = int(Liste[0] + Liste[2] * Faktor)
            Nennerneu = int(Nenner1)
            
        if Nenner1 >Nenner2 and Nenner1 % Nenner2 == 0 and Counter!= 1:
            Faktor = int(Nenner1/Nenner2)  #  Addition wenn Nenner1 ist bereits Vielfaches
            Zaehlerneu = int(Liste[0] * Counter + Liste[2] * Faktor)
            Nennerneu = int(Nenner1)
        
        
        if Nenner2 > Nenner1:  # Nenner2 Erweiterung auf Nenner1 - Vielfaches
            while Nenner2 % Nenner1 != 0:
                Nenner2 = Nenner2 + Nen2
                Counter = Counter + 1
        if Nenner2 > Nenner1 and Nenner2 % Nenner1 == 0 and Counter == 1:
            Faktor = int(Nenner2/Nenner1)  #  Zähler1 Anpassung
            Zaehlerneu = int(Liste[0] * Faktor + Liste[2])
            Nennerneu = int(Nenner2)
            
        if Nenner2 > Nenner1 and Nenner2 % Nenner1 == 0 and Counter!= 1:
            Faktor = Nenner2/Nenner1   #  Addition wenn Nenner1 ist bereits Vielfaches
            Zaehlerneu = int(Liste[0] * Faktor + Liste[2] * Counter)
            Nennerneu = int(Nenner2)
            
        if Nenner2 == Nenner1:  #  Zähler-Addition wenn Nenner bereits gleich 
            Zaehlerneu = int(Liste[0] + Liste[2])
            Nennerneu = int(Nenner1)
       
        # Ergebnis Vereinfachung
        if Zaehlerneu == 0:
            print("(",Zaehler1,"/" ,Nen1,") + (",Zaehler2,"/",Nen2,") = ",0)
        else:  
            if Nennerneu != 0 and Zaehlerneu != 0:
                   # Gemeinsamen Teiler finden ggt  
                if Zaehlerneu>Nennerneu:
                    for i in range(Nennerneu,1,-1 ):
                        #print("01=",i)
                        z = Zaehlerneu % i
                        z2 = Nennerneu % i
                        if z == 0 and z2 == 0:
                            ggt = i
                            #print("02=",ggt)
                            break    
                if Zaehlerneu<Nennerneu:
                    for i in range(Zaehlerneu,1,-1 ):
                        #print("03=",i)
                        z = Zaehlerneu % i
                        z2 = Nennerneu % i
                        if z == 0 and z2 == 0:
                            ggt = i
                            #print("04",ggt)
                            break      
                
                    #Zähler und Nenner kürzen
            Z_short = int (Zaehlerneu/ggt)
            N_short = int (Nennerneu/ggt)
            
            if N_short == 1:
                print("(",Zaehler1,"/" ,Nen1,") + (",Zaehler2,"/",Nen2,") = ",Z_short)
            
            elif Z_short == N_short:
                print("(",Zaehler1,"/" ,Nen1,") + (",Zaehler2,"/",Nen2,") = 1")
            
            else:
                print("(",Zaehler1,"/" ,Nen1,") + (",Zaehler2,"/",Nen2,") = (",Z_short,"/",N_short,")" )
                

		
assert add_frac(33,7,6,125) == assert add_frac_test(33,7,6,125)
		


    
