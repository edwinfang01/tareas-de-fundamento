peso = float( input('ingrese su peso') )
unidad = float( input('diga en que unidad ingreso su peso (1/kg) (2/lb)').strip() )
altura = float( input('ingrese su altura en metros') )
if unidad == 2:
    peso = peso * (1/2.20462262) ## lb a kg
masa = peso / (altura**2)
print(f'su masa es {masa}')
