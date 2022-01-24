tekst = input("Ievadit Virkne Tekstu: ")
def replace(tekst):
  if len(tekst)>1:
   sar = []
   for burts in tekst:
     sar.append(burts)
     sar.reverse()
     tekst = ""
   for elem in sar: 
     tekst += elem
     tekst = tekst.upper()
     print(tekst)
   else:
     tekst = "Parak Iss tekst"
   print(tekst)
replace(tekst)