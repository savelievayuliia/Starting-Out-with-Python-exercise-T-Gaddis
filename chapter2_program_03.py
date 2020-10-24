COEFF = 4047
m_sqr = float(input("Ведите площадь участка (в метрах квадратных): "))
q_acrs = m_sqr / COEFF
print("Количество акров в этом участке = ", format(q_acrs,".1f"))
