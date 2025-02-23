total = 171.99

monais = [20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
nb = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0

while total > 0:
    if total - monais[i] >= 0:
        total -= monais[i]
        nb[i] += 1
    elif total - monais[i] < 0:
        i += 1


print(nb)


/*
l'algo vorace trouve la solution opt pour compter une 
somme a l'aide des monais 5, 2, 1

dem:
prenons x
les resto possibe de la division de x par 5
sont 0, 1, 2, 3, 4

cas 1, reste 0   x = 5*a     opt  a (a monais de val 5)
					vorace a monais de val 5


cas 2, reste 1	x= 5a+1 	opt a + 1 (a monais de 5 + 1 monais de 1)

cas 3, reste 2	x= 5a+2		opt a + 2 (a monais de 5 + 1 monais de 2)

cas 4, reste 3 	x= 5a+1+2	opt a+2+1 (a monais de 5, 1 monais de 2 et 1 monais de 1)

cas 5, reste 4  x= 5a+2+2	opt a+2*2 (a monais de 5, 2 monais de 2)












*/
