#Fáum num_int frá notanda
#upphafsstillum max_int sem 0
# Á meðan num_int er ekki neikvæð tala
#þá mun forritið halda áfram að biðja um input
#Ef num_int er stærra en max_int
#þá tekur max_int nýtt gildi sem num_int
#Fáum notanda til að slá inn input annað input

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int >= 0 :
    if num_int > max_int :
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
