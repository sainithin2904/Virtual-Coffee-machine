
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def checking_needs(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"sorry! insufficient {item}")
            return False
    return True
def process_coins(q,d,n,p):
    q_d = q*0.25
    d_d = d*0.10
    n_d= n*0.05
    p_d = p*0.01
    in_dollars = round((q_d + d_d+ n_d+ p_d),2)
    return in_dollars
def ingredient_change(ingredients):
    for item in ingredients:
        resources[item] = resources[item] - ingredients[item]
        
shutdown =True
purse = 0
while shutdown != False:
    choice = input("what do you like to take(1.espresso 2.latte 3.cappuccino) :- ")
    if choice == "off":
        print("shutting down...... \nbye")
        shutdown = False
    elif choice == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"current purse:{purse}")
    else:
        drink = MENU[choice]
        print (drink)
        print(resources)
        if checking_needs(drink['ingredients']) == True:
            quarters        = int(input("enter quarters:"))
            dimes           = int(input("enter dimes:"))
            nickles         = int(input("enter nickels:"))
            penny           = int(input("enter pennies:"))
            amount_recieved = process_coins(quarters,dimes,nickles,penny)
            coffee_cost= drink["cost"]
            if amount_recieved >= coffee_cost:
                status = "success"
                print(f"your change {amount_recieved-coffee_cost}")
                ingredient_change(drink["ingredients"])
                purse += coffee_cost
            else:
                status= "failed"
                print("sorry! insufficient balance, amount refunded")
