semaforo = input("Como ves el semaforo\n")
semaforo = semaforo.lower()
if semaforo in ["verde",
                "VERDE", 
                "VERDE",
                "VERDE",
                "verde",
                "verrrrr  "]:
    print("avanzando")
elif semaforo == "amarillo":
    print("Reducir velocidad")
elif semforo == "VERDE":
    print("avanzando")
else:
    print("Alto")

