import numpy as np
import matplotlib.pyplot as plt

def floatkeyboardinput_range(_min, _max, _message):
    while True:
        _obj = float(input(_message))
        if _min <= _obj <= _max:
            break
        print("Введенное значение недопустимо! Повторите попытку.\n")
    return _obj
def floatkeyboardinput_list(_list, _message):
    while True:
        _obj = float(input(_message))
        if _obj in _list:
            break
        print("Введенное значение недопустимо! Повторите попытку.\n")
    return _obj
t = np.arange(0, np.pi/32, 0.0001)
f_acceptable = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
C0 = floatkeyboardinput_range(-10, 10, "Введите постоянную составляющую сигнала (C0), В: ")
A1 = floatkeyboardinput_range(0, 220, "Введите амплитуду составляющей электрического сигнала (А1), В: ")
A2 = floatkeyboardinput_range(0, 220, "Введите амплитуду составляющей электрического сигнала (А2), В: ")
A3 = floatkeyboardinput_range(0, 220, "Введите амплитуду составляющей электрического сигнала (А3), В: ")
f1 = floatkeyboardinput_list(f_acceptable,"Введите частоту составляющей электрического сигнала (f1), Гц: ")
f2 = floatkeyboardinput_list(f_acceptable,"Введите частоту составляющей электрического сигнала (f2), Гц: ")
f3 = floatkeyboardinput_list(f_acceptable,"Введите частоту составляющей электрического сигнала (f3), Гц: ")
psi1 = floatkeyboardinput_range(0, 360, "Введите фазовый сдвиг составляющей электрического сигнала (psi1): ")
psi2 = floatkeyboardinput_range(0, 360, "Введите фазовый сдвиг составляющей электрического сигнала (psi2): ")
psi3 = floatkeyboardinput_range(0, 360, "Введите фазовый сдвиг составляющей электрического сигнала (psi3): ")
C1 = A1*np.sin(2*np.pi*f1*t+psi1)
C2 = A2*np.sin(2*np.pi*f2*t+psi2)
C3 = A3*np.sin(2*np.pi*f3*t+psi3)
S = C0 + C1 + C2 + C3
plt.plot(t, S, 'o-b',lw=1, ms=0, label='Сигнал, сформированный системой')
plt.ylabel("U, В")
plt.xlabel("t, С")
plt.legend()
plt.title("РГЗ")
print(f"Максимальное значение, В: {round(np.max(S), 2)}\nСреднее значение, В: {round(np.average(S), 2)}\nМинимальное значение, В: {round(np.min(S), 2)}\n")
plt.show()