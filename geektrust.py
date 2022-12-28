from sys import argv
from cal import add_item_to_cart, get_discounted_cost
def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    cart = {}
    cart['items'] = {}
    for line in lines:
        line = line.split(" ")
        command = line[0]

        if command == 'ADD_ITEM':
            item = line[1]
            quantity = line[2]
            cart,output = add_item_to_cart(cart, item, quantity)
            print(output)
        elif command == 'PRINT_BILL':
            total_cost,total_discount  = get_discounted_cost(cart)
            print('TOTAL_DISCOUNT',total_discount)
            print('TOTAL_AMOUNT_TO_PAY',total_cost)


    
if __name__ == "__main__":
    main()