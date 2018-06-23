import osa

# Задание 2 - поездка

def read_file(temp):
    a = list()
    with open(temp, 'r') as f:
        for line in f:
            a.append(line.strip().split(' '))
    return a

def convert_ru(amount, currency):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum('', currency, 'RUB', amount, True, '', '')
    
cur = read_file('currencies.txt')
rubles = list()
for cu  in cur:
    rubles.append(convert_ru(cu[1], cu[2]))
    print('{} -> {}'.format(cu, rubles[-1]))
print(int(sum(rubles)) + (sum(rubles) - int(sum(rubles)) > 0))