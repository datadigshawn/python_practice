"""
C
L
A
S
S
"""
class MiaClasse:
   
   Count = 0

   def __init__(root, item, price, vendor):
      root.item = item
      root.price = price
      root.vendor = vendor
      MiaClasse.Count += 1
   
   def CountResult(root):
     print MiaClasse.Count

   def PrintData(root):
      print "Item: ", root.item,  ", Price: ", root.price, ",Vendor:", root.vendor



#Create Data

D1 = MiaClasse("Apple", 10, "SuperMarket")
D2 = MiaClasse("Lemon", 5, "My Farm")
D3 = MiaClasse("PineApple", 50, "Market")

#Print Data
D1.PrintData()
D2.PrintData()
D3.PrintData()
print "Total:", MiaClasse.Count

