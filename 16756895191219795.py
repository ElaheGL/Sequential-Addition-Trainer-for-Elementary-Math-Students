user_enter = list(input())
newlis = []
x = '+'
for i in user_enter:
    if ((i =='1') or (i =='2') or (i =='3') or (i =='+') ):
        newlis.append(i)
        newlis.sort()
        while( x in newlis):
            newlis.remove('+')
    
print("+".join(newlis))
   

 
    
    




    
    



     