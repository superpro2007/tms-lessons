def ask_for_product():
    product_name = input('enter product name: \n')
    proteins = input('enter proteins amount: \n')
    fats = input('enter fats amount: \n')
    carbohydrates = input('enter carbohydrates amount: \n')
    print(f'{product_name}, {proteins}, {fats}, {carbohydrates}')

if __name__ == "__main__":
    ask_for_product()