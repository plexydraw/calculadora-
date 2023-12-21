
print("""                
                .__                  .__               .___                      
  ____  _____   |  |    ____   __ __ |  |  _____     __| _/ ____  _______  _____   
_/ ___\ \__  \  |  |  _/ ___\ |  |  \|  |  \__  \   / __ | /  _ \ \_  __ \ \__  \  
\  \___  / __ \_|  |__\  \___ |  |  /|  |__ / __ \_/ /_/ |(  <_> ) |  | \/  / __ \_
 \___  >(____  /|____/ \___  >|____/ |____/(____  /\____ | \____/  |__|    (____  /
     \/      \/            \/                   \/      \/                      \/ 
""")
digito1 = input("Ingrese el dígito para hacer la suma (+), resta (-), división (/) o porciento (%): ")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
calculo = digito1
    

if digito1 == '-':
    calculo = numero1 - numero2

if digito1 == '+':
    calculo = numero1 + numero2

if digito1 == '%':
    calculo = numero1 % numero2

if digito1 == '/':
    if numero2 == 0:
        print(".")
    else:
        calculo = numero1 / numero2

resultado = calculo

if digito1 == '/':
    if numero2 == 0:
        print("No se puede dividir por 0")
    else:
        print(f"La {digito1} entre {numero1} y {numero2} da como resultado {resultado}")
else:
    print(f"La {digito1} entre {numero1} y {numero2} da como resultado {resultado}")

if digito1 == '%':
        print(f"El {digito1}{numero2} de {numero1} es {resultado}")

