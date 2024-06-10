# Juceklis
# Lietotājs ievada vārdu.
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu 
# un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# name = input ("Kå Tevi sauc? ")
name = "Lielgabals"
output = f"{name[::-1].capitalize()}, pamatīgs juceklis vai ne {name[0].upper()}"
print (output.split()[2])