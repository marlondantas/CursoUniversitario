from random import randint

for x in range(10):
    f = open("Entrada\entrada"+str(x)+".txt","w+")

    # print(x)

    for y in range(100):
        # print(y)
        f.write(str(randint(1,5))+" "+str(y)+"\n")
    
    f.close()