"""
Purpose: fruit store

Items  Price       qty              amount
Apples 12/piece  5 dozens=5*12=60    12*60
Mangos 34/piece  3 dozens=3*12=36    34*36
                                   ---------
                                    1994/-
                        discount -2% 38.8/-
                                    -------
                                    1950/-
                         GST 12.5% +238.14           
                                    --------
                                    2143.26

Algorithm
--------
step 0: declare the constants, like dozen ,discount
        and GST
step 1: declare cost of fruit as variable
step 2: declare the quantity of fruit
        compute the and quantity, by substituting the dozen value
step 3: selling price of each item and add them
Step 4: compute the discount and subtract from selling price
            and get payable amount
step 5: calculate GST and add to payable amount                                           
            and calculate the billable amount

"""
#constants
DOZEN=12
GST=12.5
DISCOUNT=2

# Cost
Cost_of_apples = 12 #per piece
Cost_of_mango = 34 #per piece

#Quantities of fruits
qty_of_apples = 5*DOZEN
qty_of_mangoes= 3*DOZEN

#Selling price computation
total_sp = Cost_of_apples*qty_of_apples+Cost_of_mango*qty_of_mangoes
print("Total selling price= ", total_sp)

#Discount calculation
discount_amount = (total_sp*2)/100
print("Discount amt=", discount_amount)

#PAyable amount 
payable_amount = total_sp - discount_amount
print("payable amount=", payable_amount)

#GST
gst_on_fruits = (payable_amount * GST)/100
print("GST =", gst_on_fruits)

#Billable amount
billable_amt = payable_amount + gst_on_fruits
print("Billable amount=", billable_amt)

billable_amt = payable_amount + gst_on_fruits
print("Billable amount=", round(billable_amt,2))
