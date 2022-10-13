
str1 = 'Your color choices are red, blue, green, white or yellow.'
print(str1)

str2 = 'Enter a color from the list above: '
print(str2)

userColor = input()

userColor = userColor.lower()

validcolor = True
if userColor == 'red':
    spanishcolor = 'rojo'
elif userColor == 'blue':
    spanishColor = 'azul'
elif userColor == 'green':
    spanishColor = 'verde'
elif userColor == 'white':
    spanishcolor = 'blanco'
elif userColor == 'yellow':
    spanishcolor = 'amarillo'
else:
    validcolor = False

if validcolor:
    print('The color', userColor, 'in Spanish is ' + spanishcolor)
else:
    print('That is not a valid color for this program. Ese no es un color Valido')
