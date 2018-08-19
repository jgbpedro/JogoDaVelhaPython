from datetime import datetime

now = datetime.now()

ano = now.year
mes = now.month
dia = now.day

print(now.year)
print(now.month)
print(now.day)
print("%s/%s/%s" % (dia,mes,ano))