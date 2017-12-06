product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}

def user_select(test_dict):
    selection = int(input("Select 1, 2, or 3"))
    print("you selected", selection)

    print(selection)
    if selection == 1:
        #do something
        return product_to_price['apple']
    # elif
    #     #other thing
    # else:
    #     #whatever

select = user_select(product_to_price)
print(select)
