def science():
	
   print("welcome to my measurement converter!")
   print("in this code you can convert")
   print("1. Celcius to fahrenheit 2. Fahrenheit to celcius")
   print("3. Metres to feet 4. Feet to metres ")
   print("5. Metres to centemetres 6. Centemetres to metres ")
   print("7. Kilometres to metres 8. Metres to kilometres ")
   print("9. Centemetres to kilometres 10. Kilometres to centemetres")
   print("11. Kilometres to miles 12. Miles to kilometres")
   print("12. Centemetres to inches 13. Inches to centemetres")
   print("14. kilograms to pounds 15. pounds to kilograms")
   print("16. Metric tonne to imperial ton 17. Imperial tonne to Metric tonnes")
   print("18. Inches to feet 19. Feet to inches")
   print("20. Feet to miles 21 Miles to feet")
   print("22. Inches to miles 23. Miles to inches ")
   print("24. Grams to kilograms 25. Kilograms to grams")
   print("25. Pounds to ounces 26. Ounces to pounds")
   temp=input("which number would you like to convert?")
 	
   #celcius to fahrenheit
   if temp=="1":
    a=input(" what temparature would you like to convert? ")
    a1=int(a)- 32
    a2=int(a1)* .5556
    print(str(a) + " degrees celcius is " +str(a2) + " degrees fahrenheit ")
  
   #fahrenheit to calcius
   elif temp=="2":
    b=input(" what temparature would you like to convert?")
    b1=int(b)+ 32
    b2=int(b1)* 1.8
    print(str(b) + " degrees fahrenheit is " +str(b2) + " degrees ceclius ")
	
   #metres to feet
   elif temp=="3":
    c=input("what distance would you like to convert?")
    c1=int(c)* 3.280824
    print(str(c) + " metres is " +str(c1) + " feet")
  
   #feet to metres
   elif temp=="4": 
    d=input("what distance would you like to convert?")
    d1=int(d)/ 3.2808
    print(str(d) + " feet is " +str(d1) + " metres ")
  	
   #metres to centemetres
   elif temp=="5":
    e=input("what distance would you like to convert")
    e1=int(e)* 100
    print(str(e) + " metres to " +str(e1) + "")
  	
   #centemetres to metres
   elif temp=="6":
    f=input("what distance would you like to convert")
    f1=int(f)/ 100
    print(str(f) + " centemetres is " +str(f1) + " metres ")
  
   #kilometres to metres
   elif temp=="7":
    g=input("what distance would you like to convert")
    g1=int(g)* 1000
    print(str(g) + " kilometres is " +str(g1) + " metres")
  
   #metres to kilometres
   elif temp=="8":
    h=input("what distance would you like to convert")
    h1=int(h)/ 1000
    print(str(h) + " metres  is " +str(h1) + " kilometres ")
  	
   #centemetres to kilometres
   elif temp=="9":
    i=input("what distance would you like to convert")
    i1=int(i)/ 100000
    print(str(i) + " centemetres is " +str(i1) + " kilometres ")
  	
   #kilometres to centemetres
   elif temp=="10":
    j=input("what distance would you like to convert")
    j1=int(j)* 100000
    print(str(j) + " kilometres is " +str(j1) + " centemetres ")
  	
   #kilometres to miles
   elif temp=="11":
    k=input("what distance would you like to convert?")
    k1=int(k)* 0.621371
    print(str(k) + " kilometres is " +str(k1) + " miles ")
   
   #miles to kilometres
   elif temp=="12":
    l=input("what distance would you like to convert?")
    l1=int(l)* 1.609344
    print(str(l) + " miles is " +str(l1) + " kilometres ")
    
   #centemetres to inches
   elif temp=="12":
    m=input("what distance would you like to convert")
    m1=int(m)* 0.393701
    print(str(m) + " centemetres is " +str(m1) + " inches ")
  	 
   #inches to centemetres
   elif temp=="13":
    n=input("what distance would you like to convert?")
    n1=int(n)* 2.54
    print(str(n) + " inches is " +str(n1) + " centemetres ")
 
   #kilograms to pounds
   elif temp=="14":
    o=input(" what weight would you like to convert?")
    o1=int(o)* 2.20463
    print(str(o) + " kikograms is " +str(o1) + " pounds ")
  
   #pounds to kilograms  
   elif temp=="15":
    p=input(" what weight would you like to convert?")
    p1=int(p)* .453592
    print(str(p) + " pounds is " +str(p1) + " kilograms ")
  	
   #metric tonne to imperial ton
   elif temp=="16":
    q=input(" what weight would you like to convert?")
    q1=int(q)* .984207
    print(str(q) + " metric tonnes is " +str(q1) + " imperial tons ")
  	
   #imperial ton to metric tonne
   elif temp=="17":
    r=input(" what weight you like to convert?")
    r1=int(r)* 1.01605
    print(str(r) + " imperial tons is " +str(r1) + " metric tonnes ")
  
   #inches to feet
   elif temp=="18":
    s=input(" what distance would you like to convert?")
    s1=int(s)/ 12
    print(str(s) + " inches is " +str(s1) + " feet ")
   
   #feet to inches
   elif temp=="19":
    t=input(" what distance would you like to convert?")
    t1=int(t)* 12
    print(str(t) + " feet is " +str(t1) + " inches ")
   	
   #feet to miles
   elif temp=="20":
    u=input(" what distance would you like to convert?")
    u1=int(u)/ 5280
    print(str(u) + " feet is " +str(u1) + " miles ")
   	
   #miles to feet
   elif temp=="21":
    v=input("what distance would you like to convert?")
    v1=int(v)* 5280
    print(str(v) + " miles is " +str(v1) + " feet ")
  
   #inches to miles 
   elif temp=="22":
    w=input("what distance would you like to convert?")
    w1=int(w)/ 63360
    print(str(w) + " inches is " +str(w1) + " miles ")
   	
   #miles to inches 
   elif temp=="23":
    x=input("what distance would you like to convert?")
    x1=int(x)
    print(str(x) + " miles is " +str(x1) + " inches ")
   	
   #grams to kilograms
   elif temp=="24":
    y=input("what weight would you like to convert?")
    y1=int(y)/ 1000
    print(str(y) + " grams is " +str(y1) + " kilograms ")
   	
   #kilograms to grams
   elif temp=="25":
    z=input("what weight would you like to convert?")
    z1=int(y)* 1000
    print(str(z) + " kilograms is " +str(z1) + " grams ")
   	
   #pounds to ounces
   elif temp=="26":
    aa=input("what weight would you like to convert?")
    aa1=int(z)* 16
    print(str(aa) + " pounds is " +str(aa1) + " ounces ")
   
   #ounces to pounds 
   elif temp=="27":
    bb=input("what weight would you like to convert?")
    bb1=int(aa)/ 16
    print(aa1)
    
   else:
    print("please choose a unit of measurement")
      
def money():
   
   print(" welcome to my currency converter!")
   print("disclaimer! this code my not be accurate depending on when you use this code")
   
   print(" would you like to convert")
   print("1. Euro to pound 2. Euro to us dollar")
   print("3. Euro to australian dollar 4. Euro to yen") 
   print("5. Euro to swiss franc 6. Euro to canadan dollar")
   print("7. Pound to euro 8. Pound to us dollar") 
   print("9. Pound to australian dollar 10. Pound to yen")
   print("11. Pound to swiss franc 12. Pound to canadian dollar")
   print("13. US dollar to euro 14. US dollar to pound")
   print("15. US dollar to australian dollar 16. US dollar to yen")
   print("17. US dollar to swiss franc 18. US dollar to canadian dollar ")
   print("19. Australian dollar to euro 20. Australian dollar to pound") 
   print("21. Australian dollar to us dollar 22. Australian dollar to yen")
   print("23. Australian dollar to swiss franc 24. Australian dollar to canadian dollar") 
   print("25. Yen to euro 26. Yen to pound")
   print("27. Yen to us dollar 28. Yen to australian dollar")
   print("29. Yen to swiss franc 30. Yen to canadian dollar") 
   print("31. Swiss franc to euro 32. Swiss franc to pound")
   print("33. Swiss franc to us dollar 34. Swiss franc to to australian dollar")
   print("35. Swiss franc to yen 36. Swiss franc to canadian dollar") 
   print("37. Canadian dollar to euro 38. Canadian dollar to pound")
   print("39. Canadian dollar to us dollar 40. Canadian dollar to australian dollar") 
   print("41. Canadian dollar to yen 42. Canadian dollar to Swiss franc.")
   
   cur=input(" which currency would you like to convert?")
 
    #euro to pound
   if cur=="1":
     a=input(" what amount would you like to convert?")
     a1=int(a)* .90
     print(str(a) + " euro is " + str(a1) + " pound")
    
    #euro to us dollar
   elif cur=="2":
     b=input(" what amount would you like to convert?")
     b1=int(b)* 1.10
     print(str(b) + " euro is " + str(b1) + " dollar ")
    
    #euro to australian dollar
   elif cur=="3":
     c=input(" what amount would you like to convert?")
     c1=int(c)* 1.43
     print(str(c) + " euro is " +str(c1) + " australian dollar ")
    
    #euro to yen
   elif cur=="4":
     d=input(" what amount would you like to convert?")
     d1=int(d)*114.42
     print(str(d) + " euro is " +str(d1) + " yen ")
   
    #euro to swiss franc
   elif cur=="5":
     e=input(" what amount would you like to convert?")
     e1=int(e)*1.09
     print(str(e) + " euro is " +str(e1) + " yen ")
   
    #euro to canadian dollar
   elif cur=="6":
     f=input(" what amount would you like to convert?")
     f1=int(f)*1.44
     print(str(f) + "'euro is " +str(f1) + " canadian dollar ")
       
    #pound to euro
   elif cur=="7":
     g=input(" what amount would you like to convert?")
     g1=int(g)*1.12
     print(str(g) + " pound is " +str(g1) + " euro ")
     
    #pound to us dollar
   elif cur=="8":
     h=input(" what amount would you like to convert?")
     h1=int(h)*1.23
     print(str(h) + " pound is " +str(h1) + " us dollar") 
     
    #pound to australian dollar
   elif cur=="9":
     i=input(" what amount would you like to convert?")
     i1=int(i)*1.59
     print(str(i) + " pound is " +str(i1) + " australian dollar")
     
    #pound to yen
   elif cur=="10":
     j=input(" what amount would you like to convert?")
     j1=int(j)*127.03
     print(str(j) + " pound is " +str(j1) + " yen")
   
    #pound to swiss franc
   elif cur=="11":
     k=input(" what amount would you like to convert?")
     k1=int(k)*1.22 
     print(str(k) + " pound is " +str(k1) + "swiss franc")
     
    #pound to canadian dollar
   elif cur=="12":
     l=input(" what amount would you like to convert?")
     l1=int(l)*1.61
     print(str(l) + " pround is " +str(l1) + " canadian dollar ")
     
    #us dollar to euro
   elif cur=="13":
     m=input(" what amount would you like to convert?")
     m1=int(m)*.91
     print(str(m) + " us dollars is " +str(m1) + " euro ")
   
    #us dollar to pound
   elif cur=="14":
     n=input(" what amount would you like to convert?")
     n1=int(n)*.81
     print(str(n) + " us dollaris " +str(n1) + " pound ") 
   
    #us dollar to australian dollar
   elif cur=="15":
     o=input(" what amount would you like to convert?")
     o1=int(o)*1.30
     print(str(o) + " us dollar is" +str(o1) + " australian dollar ")
   
   
    #us dollar to yen 
   elif cur=="16":
     p=input(" what amount would you like to convert?")
     p1=int(p)*103.50
     print(str(p) + " us dollar is " +str(p1) + " yen ")
   
     
    #us dollar to swiss franc
   elif cur=="17":
     q=input(" what amount would you like to convert?")
     q1=int(q)*.99
     print(str(q) + " us dollar is " +str(q1) + " swiss franc ")
   
     
    #us dollar to canadian dollar
   elif cur=="18":
     r=input(" what amount would you like to convert?")
     r1=int(r)*1.31
     print(str(r) + "us dollar is " +str(r1) + "canadian dollar ")
   
     
    #australian dollar to euro
   elif cur=="19":
     s=input(" what amount would you like to convert?")
     s1=int(s)*.70
     print(str(s) + " australian dollar is " +str(s1) + " euro ")
   
       
    #australian dollar to pound
   elif cur=="20":
     t=input(" what amount would you like to convert?")
     t1=int(t)*.63
     print(str(t) + " australian dollar is " +str(t1) + " pound ")
   
   
    #australian dollar to us dollar 
   elif cur=="21":
     u=input(" what amount would you like to convert?")
     u1=int(u)*.77
     print(str(u) + " australian dollar is" +str(u1) + " us dollar ")
   
     
    #australian dollar to yen
   elif cur=="22":
     v=input(" what amount would you like to convert?")
     v1=int(v)*79.84
     print(str(v) + " australian dollar is " +str(v1) + " us dollar ")
   
    
    #australian dollar to swiss franc
   elif cur=="23":
     w=input(" what amount would you like to convert?")
     w1=int(w)*1.3
     print(str(w) + " australian dollar is " +str(w1) + " swiss franc ")
   
    
    #australian dollar to canadian dollar
   elif cur=="24":
     x=input(" what amount would you like to convert?")
     x1=int(x)*1.01
     print(str(x) + " australian dollar is " +str(x1) + " canadian dollar")
   
   
    #yen to euro
   elif cur=="25":
     y=input(" what amount would you like to convert?")
     y1=int(y)*.0088
     print(str(y) + " yesn is " +str(y1) + " euro ")
   
     
    #yen to pound
   elif cur=="26":
     z=input(" what amount would you like to convert?")
     z1=int(z)*0.0079
     print(str(z) + " yen is " +str(z1) + " pound")
   
     
    #yen to us dollar
   elif cur=="27":
     aa=input(" what amount would you like to convert?")
     aa1=int(aa)*0.0096
     print(str(aa) + " yen is " +str(aa1) + " us dollar ")
   
    
    #yen to australian dollar
   elif cur=="28":
     bb=input(" what amount would you like to convert?")
     bb1=int(bb)*.012
     print(str(bb) + " yen is " +str(bb1) + " australian dollar ")
   
   
    #yen to swiss franc
   elif cur=="29":
     cc=input(" what amount would you like to convert?")
     cc1=int(cc)*.0095
     print(str(cc) + " yen is " +str(cc1) + " swiss franc ")
   
   
    #yen to canadian dollar
   elif cur=="30":
     dd=input(" what amount would you like to convert?")
     dd1=int(dd)*.0127
     print(str(dd) + " yen is " +str(dd1) + " canadian dollar ")
   
  
    #swiss franc to euro 
   elif cur=="31":
     ee=input(" what amount would you like to convert?")
     ee1=int(ee)*.92
     print(str(ee) + " swiss franc is " +str(ee1) + " euro ")
   

    #swiss franc to pound
   elif cur=="32":
     ff=input(" what amount would you like to convert?")
     ff1=int(ff)*.82
     print(str(ff) + " swiss franc is " +str(ff1) + " pound ")

    #swiss franc to us dollar 
   elif cur=="33":
     gg=input(" what amount would you like to convert?")
     gg1=int(gg)*1.01
     print(str(gg) + " swiss franc is " +str(ff1) + " us dollar ")

    #swiss franc to australian dollar
   elif cur=="34":
     hh=input(" what amount would you like to convert?")
     hh1=int(hh)*1.32
     print(str(hh) + " swiss franc is " +str(hh1) + " australian dollar ")

    #swiss franc to yen
   elif cur=="35":
     ii=input(" what amount would you like to convert?")
     ii1=int(ii)*104.860
     print(str(ii) + " swiss franc is " +str(ii1) + " yen ")

    #swiss franc to canadian dollar 
   elif cur=="36":
     jj=input(" what amount would you like to convert?")
     jj1=int(jj)*1.33
     print(str(jj) + " swiss franc is " +str(jj1) + " canadian dollar ")

    #canadian dollar to euro
   elif cur=="37":
     kk=input(" what amount would you like to convert?")
     kk1=int(kk)*.69
     print(str(kk) + " canadian dollar is " +str(kk1) + " euro ")

    #canadian dollar to pound
   elif cur=="38":
     ll=input(" what amount would you like to convert?")
     ll1=int(ll)*.62
     print(str(ll) + " canadian dollar is " +str(ll1) + " pound ")
     
    #canadian dollar to us dollar
   elif cur=="39":
     mm=input(" what amount would you like to convert?")
     mm1=int(mm)*.76
     print(str(mm) + " canadian dollar is " +str(mm1) + " us dollar ")

    #canadian dollar to australian dollar
   elif cur=="40":
     nn=input(" what amount would you like to convert?")
     nn1=int(nn)*99
     print(str(nn) + " canadian dollar is " +str(nn1) + " australian dollar")

    #canadian dollar to yen
   elif cur=="41":
     oo=input(" what amount would you like to convert?")
     oo1=int(oo)*78.70
     print(str(oo) + " canadian dollar is " +str(oo1) + " yen ")

    #canadian dollar to swiss franc
   elif cur=="42":
     pp=input(" what amount would you like to convert?")
     pp1=int(pp)*.75
     print(str(pp) + " canadian dollar is " +str(pp1) + " swiss franc")

choice=input("would you like to convert 1. exchange rates or 2. measurements?")
 
if choice=="1":
 money()
  
elif choice=="2":
 science()
  
 
    
