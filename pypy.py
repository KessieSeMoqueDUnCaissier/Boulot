n = int(input("Nombre"))
binaire = ""

while n != 0:
  d, r = n // 2, n % 2
  binaire += str(r)
  n = d
binary = binaire[::-1]
print(binary)


somme = 0
for j in range(len(binary)):
  somme += int(binaire[j]) * 2**j
print(somme)
    
A = '10'
B = '11'
C = '12'
D = '13'
E = '14'
F = '15'

hexa = ""
while somme != 0:
  d1, r1 = somme // 16, n % 16
  if r1 == 10:
    r1 = 'A'
  if r1 == 11:
    r1 = 'B'
  if r1 == 12:
    r1 = 'C'
  if r1 == 13:
    r1 = 'D'
  if r1 == 14:
    r1 = 'E'
  if r1 == 15:
    r1 = 'F'
  if type(r1) == int:
    r1=str(r1)
  hexa += r1
  somme = d1


  
hex = hexa[::-1]
print(hex)


