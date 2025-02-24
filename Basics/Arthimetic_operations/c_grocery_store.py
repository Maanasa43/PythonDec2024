"""
Purpose: grocery store

Item        Cost
-----------------
Wheat       10/kg
Rice        34/kg

Algorithm
---------
step1: Get the cost of items to variables
step 2: get the quantity of items from user (in run time)
step 3: 

NoTE: input()
--> get the value in run time
by default, input will take string only

"""
#Cost of Variables
Cost_of_Wheat=10
Cost_of_Rice=34

#Quantity of Variables
qty_of_wheat=float(input("qty_of_wheat="))
#qty_of_wheat=int(qty_of_wheat) both same
print("qty_of_wheat=", qty_of_wheat)

qty_of_rice=float(input("qty_of_rice="))
print("qty_of_rice=", qty_of_rice)

# Selling price computation
sp_of_wheat = Cost_of_Wheat * qty_of_wheat
print("sp_of_wheat=", sp_of_wheat)
sp_of_rice= Cost_of_Rice * qty_of_rice
print("sp_of_rice=", sp_of_rice)

Billable_price = sp_of_rice + sp_of_wheat
print("Billable_price=", Billable_price)
      
