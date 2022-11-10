##soal1
list = "tipe data yang terbentuk dari berbagai jenis data(integer,float,dll). List adalah tipe data yang ordered, dengan kata lain kita bisa indexing & slicing"
print (list)
tuple = "tipe data ordered yang objectnya tidak dapat dirubah, bersifat immuntable, tanda ()"
print (tuple)
set = "tipe data yang tidak ordered, cirinya bisa diubah untuk objeknya namun diuntuk objeknya harus berupa unique, tandanya {}"
print (set)
dict = "pasangan key-value, tanda {}"
print (dict)

##soal2
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print (a[1:5])

##soal3
a = [
    [5,9,8],
    [0,0,6]
    ]
print (a[1][1:3])

##soal4
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
a [0][2] = 10
a [1][0] = 11
print (a)

##soal5
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del areas [8:10]
print (areas)

##SOAL6
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
T = S[0::2]
print(T)

##soal8
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe ["italy"] = "roma"
print (europe)

##soal9
print((9 > 10) and (2 < 4))	
print((8 == 8) or (6 != 6))	
print(not(3 <= 1))			

##soal10
A = 10000
if A > 100000 :
   print ("High")
elif  A > 50000 :
   print ("Medium")
elif A < 50000 :
   print ("Low")




##latihan sendiri
a = "True"
b = "False"

a = 10 < 9
print (a)

b = 100 == 1000
print (b)

c = 1 == 1
print (c)

a = (2 > 1 or 3 == 3)
b = (1 == 1 and 4 == 10)
print (a)