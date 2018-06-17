def evenDigitsOnly(n):
   return sum([(0 if int(i) % 2 == 0 else 1)for i in list(str(n))]) < 1
