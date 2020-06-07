
def cpf(dv):
  l_dv = list( dv )
  lc_dv1 = list( range( 10, 1, -1))
  lc_dv2 = list( range( 11, 1, -1))
  ls_dv1, ls_dv2 = [], []
  s_s, s_s2, menos = 0, 0, 0
  dvf1, dvf2 = 0, 0
  # PRIMEIRA FORMULA
  for s in range(0,8):
    ls_dv1.append( int( l_dv[s] ) * lc_dv1[s] )
    s_s +=ls_dv1[s]
  s_s = s_s % 11
  menos = 11 - s_s
  if menos > 9:
    dvf1 = 0
  else:
    dvf1 = menos
  # SEGUNDA FORMULA
  for s2 in range(0, 9):
    ls_dv2.append(  int( l_dv[s2] ) * lc_dv2[s2] )
    s_s2 += ls_dv2[s2]
 
  ls_dv2.append( dvf1 * lc_dv2[9])
  s_s2 += ls_dv2[9]
  s_s2 = s_s2 % 11
  dvf2 = 11 - s_s2
  # RETORNANDO VALOR
  if int(l_dv[9] ) == dvf1:
    if int( l_dv[10] ) == dvf2:
      return True
    else:
      return False
  else:
    return False



digitos = input( 'Informe CPF/CNPJ: ')


t = len(digitos)
if t == 11:
  if not cpf(digitos):
    print('CPF Inváido')
elif t == 14:
  if not cnpj(digitos):
    print('CNPJ Inválido')


