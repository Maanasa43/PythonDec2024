"""Purpose Ration store

item    price     quantity      Amount
wheat   25/kg       30kgs     25*30=750/- 
Rice    12/kg       50kgs     50*12=600/-
                            -------------
                                    1350/-
                    subsidy 20%     -270
                            -------------
                    Billable Amount 1080/-

Algorithm
--------

Step 1: Get the cost of each item into variable
step 2: get the quantity of each item into variable
step 3: do the calculation(multiply) and add the Amount
step 4: calculate the subsidy amount and subtract the subsidy.
step 5: display the billable amount

"""

#Cost of items
Cost_of_wheat=25
Cost_of_rice=12

#quantities of items
qty_of_wheat=30 #kgs
qty_of_rice=50 #kgs

#Selling price computation
sp_of_wheat= Cost_of_wheat * qty_of_wheat
sp_of_rice= Cost_of_rice * qty_of_rice

Total_sp= sp_of_rice + sp_of_wheat
#print(Total_sp)

print("Total selling price =", Total_sp)

# Subsidy calculation

Subsidy = (Total_sp * 20)/100 #PEMDAS
print("subsidy amount   :", Subsidy)

Billable_Amount = Total_sp - Subsidy
print("Billable Amount  :", Billable_Amount)

