def ask_for_product():
    product_name = input('enter product name: \n')
    proteins = input('enter proteins amount: \n')
    fats = input('enter fats amount: \n')
    carbohydrates = input('enter carbohydrates amount: \n')
    product = {
        'name': product_name,
        'proteins': proteins,
        'fats': fats,
        'carbohydrates': carbohydrates
    }
    return product

if __name__ == "__main__":
    product = ask_for_product()
    print(product)