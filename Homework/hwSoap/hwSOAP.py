import osa

# Задание 1 - температура

def read_file(temp):
    a = list()
    with open(temp, 'r') as f:
        for line in f:
            a.append(line.strip().split(' '))
    return a
    
def convert(temperature):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(temperature, 'degreeFahrenheit', 'degreeCelsius')
    
tem = read_file('temps.txt')
tem_list = list()
for te in tem:
    tem_list.append(convert(te[0]))
    print('{} -> {}'.format(te, tem_list[-1]))
print(sum(tem_list) / len(tem_list))   
    
# Задание 2 - поездка

def convert_ru(amount, currency):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum('', currency, 'RUB', amount, True, '', '')
    
cur = read_file('currencies.txt')
rubles = list()
for cu  in cur:
    rubles.append(convert_ru(cu[1], cu[2]))
    print('{} -> {}'.format(cu, rubles[-1]))
print(int(sum(rubles)) + (sum(rubles) - int(sum(rubles)) > 0))

# Задание 3 - путь

def convert_miles(distance):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(distance, 'Miles', 'Kilometers')

dist_list = list()
trip = read_file('travel.txt')
for tri in trip:
    dist_list.append(convert_miles(float(str(tri[1]).replace(',', ''))))
    print('{} -> {}'.format(tri, dist_list[-1]))
print(round(sum(dist_list) / len(dist_list), 2))    