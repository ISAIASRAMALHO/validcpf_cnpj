
def cpf(dv):
  l_dv = list( dv )
  lc_dv1 = list( range( 10, 1, -1))
  lc_dv2 = list( range( 11, 1, -1))
  ls_dv1, ls_dv2 = [], []
  s_s, s_s2  = 0, 0
  resto1, resto2 = 0, 0
  dvf1, dvf2 = 0, 0
  # PRIMEIRA FORMULA
  for s in range(0,9):
    ls_dv1.append( int( l_dv[s] ) * lc_dv1[s] )
    s_s +=ls_dv1[s]
  resto1 = s_s % 11
  dvf1 = 11 - resto1
  if dvf1 > 9:
    dvf1 = 0
 
  # SEGUNDA FORMULA
  for s2 in range(0, 9):
    ls_dv2.append(  int( l_dv[s2] ) * lc_dv2[s2] )
    s_s2 += ls_dv2[s2]
 
  ls_dv2.append( dvf1 * lc_dv2[9])
  s_s2 += ls_dv2[9]
  resto2 = s_s2 % 11
  dvf2 = 11 - resto2
 
  # RETORNANDO VALOR
  return ( int( l_dv[9] ) == dvf1 and int( l_dv[10] ) == dvf2 )
 
# EXEMPLO dv = 1 1 4 4 4 7 7 7 0 0 0 1 0 1

def cnpj( dv ):
  l_dv = list( dv )
  m = [5,4,3,2,9,8,7,6,5,4,3,2]
  m2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
  n1, n2, q1, q2 = 0, 0, 0, 0
  dvf1, dvf2 = 0, 0
  # PRIMEIRA FORMULA
  for s in range(0,12):
    n1 += int(l_dv[s]) * m[s]
    print(s)
  q1 = n1 % 11
  if q1 < 2:
    dvf1 = 0
  else:
    dvf1 = 11 - q1
  
  # SEGUNDA FORMULA
  for s2 in range(0,12):
    n2 += int( l_dv[s2]) * m2[s2] 
 
  n2 += dvf1 * m2[12]
  # RESTO
  q2 = n2 % 11
  if q2 < 2:
    dvf2 = 0
  else:
    dvf2 = 11 - q2

  # RETORNANDO VALOR
  return ( int( l_dv[12]) == dvf1 and int( l_dv[13]) == dvf2 )
  



dig = input( 'Informe CPF/CNPJ: ')


t = len(dig)
if t == 11:
  if not cpf(dig):
    print('CPF Inváido')
  else:
    print( 'CPF {}.{}.{}-{} é válido'.format( dig[0:3], dig[3:6],dig[6:9],dig[9:11] ) )
elif t == 14:
  if not cnpj(dig):
    print('CNPJ Inválido')
  else:
    print(' CNPJ informado :{}.{}.{}/{}-{} é válido'.format( dig[0:2], dig[2:5], dig[5:8], dig[8:12], dig[12:14]))
