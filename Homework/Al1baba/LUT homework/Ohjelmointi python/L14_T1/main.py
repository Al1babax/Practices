import math


class Car:

    def __init__(self):
        self.km = float(input("Anna vuotuiset kilometrit: "))
        self.consumption = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
        self.gas_price = float(input("Anna polttoaineen hinta (€/l): "))
        self.age = float(input("Anna auton ikä vuosissa: "))
        self.insurance_cost = float(input("Anna vakuutusten määrä (euroissa): "))
        self.insurance_bonus = float(input("Anna bonusprosentti kokonaislukuna: "))
        self.taxes = float(input("Anna verojen määrä: "))

    def calculate_cost(self):
        """
        summa = kilometrit / 100 * polttoaineen kulutus * polttoaineen hinta +vakuutusten määrä – bonukset + verot
         + 200 * SQRT(auton ikä).
        """
        five_year_cost = 0
        for x in range(5):
            total_cost = self.km / 100 * self.consumption * self.gas_price + self.insurance_cost - (self.insurance_cost * (self.insurance_bonus / 100)) + self.taxes + 200 * math.sqrt(self.age + x)
            five_year_cost += total_cost
            print(f"{x + 1}. vuosi: {int(round(total_cost, 0))}")
        print(f"Viiden vuoden aikana autoon käytettiin rahaa {int(round(five_year_cost, 0))} euroa.")


def main():
    new_car = Car()
    new_car.calculate_cost()


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
