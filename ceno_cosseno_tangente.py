import math
an=float(input('ângulo da circunferência:'))
cen=math.asinh(math.radians(an))
#math.radians converte números integrais para radianos
cos=math.cos(math.radians(an))
tang=math.tan(math.radians(an))
print('O ceno do ângulo de {} é {:.2f}'.format(an,cen))
print('O coceno do ângulo de {} é {:.2f}'.format(an,cos))
print('A tangente do ângulo de {} é {:.2f}'.format(an,tang))


