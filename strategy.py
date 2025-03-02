from abc import ABC, abstractmethod



class CurrencyConversionStrategy(ABC):
    @abstractmethod
    def convert(self, amount: float, rate: float) -> float:
        pass



class FixedRateConversion(CurrencyConversionStrategy):
    def convert(self, amount: float, rate: float = 1.0) -> float:
        return amount * rate


class MarketRateConversion(CurrencyConversionStrategy):
    def convert(self, amount: float, rate: float) -> float:
        return amount * rate


class CentralBankRateConversion(CurrencyConversionStrategy):
    def convert(self, amount: float, rate: float) -> float:
        return amount * rate



class CurrencyConverterContext:
    def __init__(self, strategy: CurrencyConversionStrategy):
        self.strategy = strategy

    def convert_currency(self, amount: float, rate: float) -> float:
        return self.strategy.convert(amount, rate)



def main():
    print("Выберите стратегию конвертации:")
    print("1. Фиксированный курс")
    print("2. Рыночный курс")
    print("3. Курс центрального банка")

    choice = input("Введите номер стратегии: ")
    amount = float(input("Введите сумму для конвертации: "))
    rate = float(input("Введите курс: "))

    if choice == '1':
        strategy = FixedRateConversion()
    elif choice == '2':
        strategy = MarketRateConversion()
    elif choice == '3':
        strategy = CentralBankRateConversion()
    else:
        print("Неверный выбор")
        return

    converter = CurrencyConverterContext(strategy)
    converted_amount = converter.convert_currency(amount, rate)
    print(f"Конвертированная сумма: {converted_amount}")


if __name__ == "__main__":
    main()
