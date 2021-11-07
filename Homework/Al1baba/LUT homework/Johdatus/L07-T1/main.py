class ShoppingList:

    list = []

    def add(self, product):
        self.list.append(product)

    def remove(self, product_index):
        self.list.pop(product_index - 1)

    def length(self):
        return len(self.list)

    def items(self):
        return self.list

    def __str__(self):
        return f"""Ostoslistasi sisältää seuraavat tuotteet:
{self.list}
Voit valita alla olevista toiminnoista:
1) Lisää
2) Poista
0) Lopeta"""


def main():
    ostoslista = ShoppingList()

    while True:
        print(ostoslista)
        decision = int(input("Valintasi: "))

        if decision == 1:
            new_product = input("Anna lisättävä tuote: ")
            print()
            ostoslista.add(new_product)
        elif decision == 2:
            print(f"Ostoslistassasi on {ostoslista.length()} tuotetta.")
            remove_number = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            print()
            ostoslista.remove(remove_number)
        elif decision == 0:
            print(f"Sinulta jäi ostamatta seuraavat tuotteet:\n{ostoslista.items()}")
            break
        else:
            print("Tunnistamaton valinta.\n")

    print("Kiitos ohjelman käytöstä.")


if __name__ == '__main__':
    main()
