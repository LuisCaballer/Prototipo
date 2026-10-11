import random
import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra el banner del juego."""
    print("=" * 50)
    print("   🎯 JUEGO DE ADIVINANZA 🎯")
    print("=" * 50)

def elegir_dificultad():
    """Permite al jugador elegir la dificultad."""
    print("\nSelecciona la dificultad:")
    print("1. Fácil    (1-50,  10 intentos)")
    print("2. Medio    (1-100,  7 intentos)")
    print("3. Difícil  (1-500,  5 intentos)")
    
    while True:
        opcion = input("\nElige una opción (1-3): ").strip()
        if opcion == "1":
            return 50, 10
        elif opcion == "2":
            return 100, 7
        elif opcion == "3":
            return 500, 5
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

def jugar():
    """Lógica principal de una partida."""
    limpiar_pantalla()
    mostrar_banner()
    
    limite, intentos_max = elegir_dificultad()
    numero_secreto = random.randint(1, limite)
    intentos = 0
    
    print(f"\n✨ He pensado un número entre 1 y {limite}.")
    print(f"Tienes {intentos_max} intentos para adivinarlo. ¡Buena suerte!\n")
    
    while intentos < intentos_max:
        restantes = intentos_max - intentos
        try:
            entrada = input(f"Intento {intentos + 1}/{intentos_max} → Ingresa tu número: ").strip()
            intento = int(entrada)
        except ValueError:
            print("⚠️  Por favor, ingresa un número válido.\n")
            continue
        
        if intento < 1 or intento > limite:
            print(f"⚠️  El número debe estar entre 1 y {limite}.\n")
            continue
        
        intentos += 1
        
        if intento == numero_secreto:
            print(f"\n🎉 ¡FELICIDADES! Adivinaste el número {numero_secreto}.")
            print(f"   Lo lograste en {intentos} intento(s).")
            return True
        elif intento < numero_secreto:
            print(f"📈 Muy bajo. Te quedan {restantes - 1} intento(s).\n")
        else:
            print(f"📉 Muy alto. Te quedan {restantes - 1} intento(s).\n")
    
    print(f"\n💀 ¡Sin intentos! El número secreto era: {numero_secreto}")
    return False

def main():
    """Bucle principal del juego."""
    victorias = 0
    derrotas = 0
    
    while True:
        if jugar():
            victorias += 1
        else:
            derrotas += 1
        
        print(f"\n📊 Marcador → Victorias: {victorias} | Derrotas: {derrotas}")
        
        otra = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra != 's':
            print("\n👋 ¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()