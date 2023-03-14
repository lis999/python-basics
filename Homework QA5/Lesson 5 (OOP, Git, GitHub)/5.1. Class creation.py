"""
Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set
"""

class Investments:
    def __init__(self, ticker, market, price):
        self.ticker = ticker
        self.market = market
        self.price = price

    def show_info(self):
        return f"{self.ticker}/${self.price}"


class Stocks(Investments):
    def __init__(self, ticker, market, price, dividends):
        super().__init__(ticker, market, price)
        self.dividends = dividends

    def dividend_premium(self):
        return f'Forward Dividend Yeld: {self.dividends}%'


class ETF(Stocks):
    def __init__(self, ticker, market, price, dividends, ind):
        super().__init__(ticker, market, price, dividends)
        self.ind = ind

    def show_index(self):
        return f'Included into {self.ind} index'

    def snap_shot(self):
        return f'Index: {self.ind}\nTicker: {self.ticker}\nPrice: ${self.price}\nDiv.yeld: {self.dividends}%'


intel = Investments('INTC', 'US', 25.77)

facebook = Stocks('META', 'US', 143, 0)

vanguard = ETF('VOO', 'US', 328.3, 1.55, 'S&P500')


print(intel.__dict__)
print(intel.show_info())
print(vanguard.show_info())
print('-'*40)
print(facebook.__dict__)
print(facebook.dividend_premium())
print('-'*40)
print(f'{vanguard.ticker}', vanguard.show_index())
print('-'*40)
print(vanguard.snap_shot())







