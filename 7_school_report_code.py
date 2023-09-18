"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:
"""


import json

with open("school_data.json", "r") as json_file:
    json_data = json.load(json_file)


    

# "NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"

print("American Athletic Conference Schools:")
for institution in json_data:
    if institution["NCAA"]["NAIA conference number football (IC2020)"] == 372:
        print(institution["instnm"])


print("Big Twelve Conference:")
for institution in json_data:
    if institution["NCAA"]["NAIA conference number football (IC2020)"] == 108:
        print(institution["instnm"])


print("Big Ten Conference:")
for institution in json_data:
    if institution["NCAA"]["NAIA conference number football (IC2020)"] == 107:
        print(institution["instnm"])


print("Southeastern Conference:")
for institution in json_data:
    if institution["NCAA"]["NAIA conference number football (IC2020)"] == 130:
        print(institution["instnm"])



# Display report for all universities that have a graduation rate for Women over 50%
for institution in json_data:
    if institution["Graduation rate  women (DRVGR2020)"] is not None:
        if institution["Graduation rate  women (DRVGR2020)"] > 50:
            print(institution["instnm"])
            print("Graduation rate for women: " + str(institution["Graduation rate  women (DRVGR2020)"])+"\n")



# Display report for all universities that have a total price for in-state students living off campus over $50,000
for institution in json_data:

    total_in_state_price = institution["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
    
    if  total_in_state_price is not None:
        if total_in_state_price > 50000:
            print(institution["instnm"])
            print("Total price for in-state students living off campus: $" + f"{total_in_state_price:,.2f}"+"\n")