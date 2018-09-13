#Byrjum á að biðja um lengd á rununni
#runan er: síðustu þrír tölustafir plúsaðir saman gefa næstu tölu
#Ef lengdin er 1 þá prentum við út fyrsta staf í runu
#Ef lengdin er 2 þá prentum við út fyrstu tvo stafi í runu
#Upphafsstillum fyrstu þrjá töllustafi
# Ef lengdin er meira en tveir förum við í while lykkju
# Byrjum á því að prenta fyrstu tvo í rununni
# sequence er þá nr1 + nr2 + nr3
# í næstu tölu verður nr1 = nr2
# nr2 = nr3
# og nr3 = sequence talan  

n = int(input("Enter the length of the sequence: ")) # Do not change this line
number = 0
first_number = 0
second_number = 1
third_number = 2


if n == 1 :
    print("1")
elif n == 2 :
    print("1")
    print("2")
elif n > 2 :
    print("1")
    print("2")
    while number < n-2 :
        sequence = first_number + second_number + third_number
        first_number = second_number
        second_number = third_number
        third_number = sequence
        print(sequence)
        number += 1


