from director import Director
from drinkbuilder import DrinkBuilder

director = Director()
builder = DrinkBuilder()
director.builder = builder

choice = input('1.Kubek\n2.Kawa - czarna\n3.Herbata\n4.Gorąca czekolada\n5.Latte\n')


def switch(choice):
    if choice == '1':
        print("Podaję kubek:")
        director.prepare_cup()
        builder.product.list_parts()
        return "Miłego dnia!"
    elif choice == '2':
        print("Przygotowuję kawę:")
        director.prepare_coffee()
        builder.product.list_parts()
        return "Miłego dnia!"
    elif choice == '3':
        print("Przygotowuję herbatę:")
        director.prepare_tea()
        builder.product.list_parts()
        return "Miłego dnia!"
    elif choice == '4':
        print("Przygotowuję gorącą czekoladę:")
        director.prepare_hot_chocolate()
        builder.product.list_parts()
        return "Miłego dnia!"
    elif choice == '5':
        print("Przygotowuję Latte:")
        director.prepare_latte()
        builder.product.list_parts()
        return "Miłego dnia!"
    else:
        return'Wybrano złą opcję!'


print(switch(choice))
