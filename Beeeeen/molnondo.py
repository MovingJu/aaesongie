import time

def playerinput():
    weigh = float(input('CO2의 질량을 입력하세요 (g) : '))
    Rtkdtn = 0.082
    tempC = float(input('CO2의 온도를 입력하세요 (℃) : '))
    tempT = tempC + 273
    Powerwmdrl = float(input('수증기의 압력을 입력하세요 (mmHg) : '))
    Powertemp = 760 - Powerwmdrl
    Powerreal = Powertemp / 760
    Volumetemp = float(input('CO2의 부피를 입력하세요 (ml) : '))
    Volumereal = Volumetemp / 1000
    molcalcul(weigh, Rtkdtn, tempT, Powerreal, Volumereal)

def molcalcul(w, R, T, P, V):
    print('\n계산중입니다..')
    Molnongdo = w * R * T / P / V
    time.sleep(1)
    print('\nCO2의 몰농도는 %fg/mol 입니다.' %Molnongdo)

if __name__ == '__main__':
    playerinput()