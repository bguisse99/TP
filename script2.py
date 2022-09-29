#Lire la saisie de l'utilisateur
min = int(1)
max = int(1000000)
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
