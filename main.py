"""
=============================================================
  Simulador de Entrenamiento Pokémon
  Archivo: main.py
  Descripción: Menú principal e interacción con el usuario.
               Aplica variables globales/locales, paso de
               parámetros y uso de la clase Pokemon.
=============================================================
"""

import sys
import os

# ── Ajustamos el path para importar el paquete 'clases' ───────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from clases.pokemon import Pokemon

# ══════════════════════════════════════════════════════════════════════════════
# VARIABLE GLOBAL
# La lista de Pokémon capturados es global para que todas las
# funciones del menú puedan acceder y modificarla.
# ══════════════════════════════════════════════════════════════════════════════
pokemons_capturados: list[Pokemon] = []

# ── Tipos disponibles (constante global) ──────────────────────────────────────
TIPOS_DISPONIBLES = [
    "Fuego", "Agua", "Planta", "Eléctrico", "Psíquico",
    "Hielo", "Lucha", "Tierra", "Volador", "Veneno",
    "Normal", "Dragón", "Siniestro", "Acero", "Hada"
]

# ── Pokémon predefinidos para captura rápida ───────────────────────────────────
POKEMONS_PREDEFINIDOS = {
    "1": ("Pikachu",    "Eléctrico", 55, 40, 35),
    "2": ("Charizard",  "Fuego",     84, 78, 78),
    "3": ("Blastoise",  "Agua",      83, 100, 79),
    "4": ("Bulbasaur",  "Planta",    49, 49, 45),
    "5": ("Mewtwo",     "Psíquico", 110, 90, 106),
    "6": ("Gengar",     "Veneno",    65, 60, 60),
    "7": ("Snorlax",    "Normal",    110, 65, 160),
    "8": ("Dragonite",  "Dragón",   134, 95, 91),
}


# ══════════════════════════════════════════════════════════════════════════════
# FUNCIONES DEL MENÚ
# ══════════════════════════════════════════════════════════════════════════════

def limpiar_pantalla() -> None:
    """Limpia la terminal (variable local: sistema operativo)."""
    sistema = os.name  # variable local
    os.system("cls" if sistema == "nt" else "clear")


def mostrar_banner() -> None:
    """Imprime el banner principal del simulador."""
    print("""
  ╔══════════════════════════════════════════════════════╗
  ║   ⚡  SIMULADOR DE ENTRENAMIENTO POKÉMON  ⚡         ║
  ║          Programación Orientada a Objetos            ║
  ╚══════════════════════════════════════════════════════╝""")


def mostrar_menu_principal() -> None:
    """Muestra las opciones del menú principal."""
    print("""
  ┌──────────────────────────────────────┐
  │           MENÚ PRINCIPAL             │
  ├──────────────────────────────────────┤
  │  1. Capturar nuevo Pokémon  🐉        │
  │  2. Entrenar un Pokémon    💪         │
  │  3. Ver información        📋         │
  │  4. Total de Pokémon       🧮         │
  │  5. Simular batalla        ⚔️          │
  │  6. Liberar un Pokémon     🕊️          │
  │  7. Salir                  🚪         │
  └──────────────────────────────────────┘""")


def pedir_entero(mensaje: str, minimo: int = 1, maximo: int = 999) -> int:
    """
    Solicita un número entero al usuario dentro de un rango.

    Parámetros (paso por valor)
    ---------------------------
    mensaje : str – Texto de solicitud.
    minimo  : int – Valor mínimo aceptado.
    maximo  : int – Valor máximo aceptado.

    Variable local
    --------------
    valor : int – Valor ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(f"  {mensaje}: ").strip())  # variable local
            if minimo <= valor <= maximo:
                return valor
            print(f"  ⚠️  Ingresa un número entre {minimo} y {maximo}.")
        except ValueError:
            print("  ⚠️  Por favor ingresa un número válido.")


def seleccionar_pokemon(mensaje: str = "Selecciona un Pokémon") -> Pokemon | None:
    """
    Muestra la lista de Pokémon capturados y permite seleccionar uno.

    Parámetros
    ----------
    mensaje : str – Texto de encabezado.

    Retorno
    -------
    Pokemon | None – El Pokémon seleccionado, o None si no hay ninguno.
    """
    # Acceso a variable global
    global pokemons_capturados

    if not pokemons_capturados:
        print("\n  ⚠️  No tienes Pokémon capturados todavía.")
        return None

    print(f"\n  {mensaje}:")
    for indice, poke in enumerate(pokemons_capturados, start=1):
        print(f"    {indice}. {poke}")

    opcion = pedir_entero("Número del Pokémon", 1, len(pokemons_capturados))
    return pokemons_capturados[opcion - 1]  # Acceso por referencia al objeto


# ══════════════════════════════════════════════════════════════════════════════
# OPCIÓN 1: CAPTURAR POKÉMON
# ══════════════════════════════════════════════════════════════════════════════

def capturar_pokemon() -> None:
    """
    Permite crear un nuevo Pokémon (predefinido o personalizado)
    y lo agrega a la lista global.

    Variables locales: nombre, tipo, ataque, defensa, salud, nuevo_pokemon.
    Variable global modificada: pokemons_capturados.
    """
    global pokemons_capturados  # Declaramos uso de variable global

    print("\n  ══ CAPTURAR POKÉMON ══")
    print("\n  ¿Cómo quieres capturar tu Pokémon?")
    print("    A. Elegir un Pokémon predefinido")
    print("    B. Crear un Pokémon personalizado")

    modo = input("\n  Opción (A/B): ").strip().upper()

    if modo == "A":
        # ── Pokémon predefinido ────────────────────────────────────────────
        print("\n  Pokémon disponibles:")
        for clave, datos in POKEMONS_PREDEFINIDOS.items():
            print(f"    {clave}. {datos[0]:10} | Tipo: {datos[1]:10} | "
                  f"ATK:{datos[2]} DEF:{datos[3]} HP:{datos[4]}")

        eleccion = input("\n  Elige un número (1-8): ").strip()
        if eleccion not in POKEMONS_PREDEFINIDOS:
            print("  ⚠️  Opción inválida.")
            return

        datos = POKEMONS_PREDEFINIDOS[eleccion]
        # Variables locales con los datos del Pokémon predefinido
        nombre, tipo, ataque, defensa, salud = datos

    elif modo == "B":
        # ── Pokémon personalizado ──────────────────────────────────────────
        nombre  = input("\n  Nombre del Pokémon : ").strip()
        if not nombre:
            print("  ⚠️  El nombre no puede estar vacío.")
            return

        print(f"\n  Tipos disponibles: {', '.join(TIPOS_DISPONIBLES)}")
        tipo    = input("  Tipo              : ").strip().capitalize()

        print("\n  Estadísticas (valores entre 10 y 200):")
        ataque  = pedir_entero("Ataque ", 10, 200)
        defensa = pedir_entero("Defensa", 10, 200)
        salud   = pedir_entero("Salud  ", 10, 200)
    else:
        print("  ⚠️  Opción inválida.")
        return

    # ── Crear la instancia (se pasan parámetros por valor) ────────────────
    nuevo_pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)

    # ── Agregar a la lista global (paso por referencia del objeto) ────────
    pokemons_capturados.append(nuevo_pokemon)


# ══════════════════════════════════════════════════════════════════════════════
# OPCIÓN 2: ENTRENAR UN POKÉMON
# ══════════════════════════════════════════════════════════════════════════════

def entrenar_pokemon() -> None:
    """
    Permite elegir cómo entrenar un Pokémon seleccionado,
    demostrando la sobrecarga de métodos con *args.
    """
    print("\n  ══ ENTRENAR POKÉMON ══")
    pokemon = seleccionar_pokemon("¿Qué Pokémon quieres entrenar?")
    if pokemon is None:
        return

    print(f"\n  Entrenando a {pokemon.nombre}...")
    print("  ¿Cómo quieres entrenar?")
    print("    1. Entrenamiento automático (sin argumentos)")
    print("    2. Mejorar sólo Ataque (1 argumento)")
    print("    3. Mejorar Ataque y Defensa (2 argumentos)")
    print("    4. Mejorar Ataque, Defensa y Salud (3 argumentos)")

    modo = pedir_entero("Modo de entrenamiento", 1, 4)

    # ── Demostramos sobrecarga de métodos según la elección ────────────────
    if modo == 1:
        pokemon.entrenar()                  # Sin argumentos
    elif modo == 2:
        val_atk = pedir_entero("Puntos de Ataque a ganar", 1, 100)
        pokemon.entrenar(val_atk)           # 1 argumento
    elif modo == 3:
        val_atk = pedir_entero("Puntos de Ataque a ganar ", 1, 100)
        val_def = pedir_entero("Puntos de Defensa a ganar", 1, 100)
        pokemon.entrenar(val_atk, val_def)  # 2 argumentos
    else:
        val_atk = pedir_entero("Puntos de Ataque a ganar ", 1, 100)
        val_def = pedir_entero("Puntos de Defensa a ganar", 1, 100)
        val_sal = pedir_entero("Puntos de Salud a ganar  ", 1, 200)
        pokemon.entrenar(val_atk, val_def, val_sal)  # 3 argumentos

    # Mostrar poder total después del entrenamiento
    poder = pokemon.poder_total()  # variable local
    print(f"\n  ⭐ Poder total de {pokemon.nombre}: {poder} pts")


# ══════════════════════════════════════════════════════════════════════════════
# OPCIÓN 3: VER INFORMACIÓN
# ══════════════════════════════════════════════════════════════════════════════

def ver_informacion() -> None:
    """
    Muestra la información de todos los Pokémon o de uno seleccionado.
    Accede a la variable global pokemons_capturados.
    """
    global pokemons_capturados

    if not pokemons_capturados:
        print("\n  ⚠️  No tienes Pokémon capturados todavía.")
        return

    print("\n  ══ INFORMACIÓN DE POKÉMON ══")
    print("    1. Ver todos")
    print("    2. Ver uno específico")
    opcion = pedir_entero("Opción", 1, 2)

    if opcion == 1:
        for poke in pokemons_capturados:  # Paso por referencia (iteración)
            poke.mostrar_info()
            print(f"  ⭐ Poder total: {poke.poder_total()} pts")
    else:
        pokemon = seleccionar_pokemon("¿De qué Pokémon quieres ver información?")
        if pokemon:
            pokemon.mostrar_info()
            print(f"  ⭐ Poder total: {pokemon.poder_total()} pts")


# ══════════════════════════════════════════════════════════════════════════════
# OPCIÓN 4: TOTAL DE POKÉMON (método de clase)
# ══════════════════════════════════════════════════════════════════════════════

def mostrar_total() -> None:
    """Llama al método de clase total_pokemons()."""
    Pokemon.total_pokemons()  # Llamada a método de clase (sin instancia)
    print(f"  📋 En tu equipo: {len(pokemons_capturados)} Pokémon")


# ══════════════════════════════════════════════════════════════════════════════
# OPCIÓN 5: SIMULAR BATALLA
# ══════════════════════════════════════════════════════════════════════════════

def simular_batalla() -> None:
    """
    Simula una batalla entre dos Pokémon del equipo.
    Demuestra el paso de objetos por referencia en atacar().
    """
    global pokemons_capturados

    if len(pokemons_capturados) < 2:
        print("\n  ⚠️  Necesitas al menos 2 Pokémon para batallar.")
        return

    print("\n  ══ SIMULAR BATALLA ══")
    print("\n  Selecciona el Pokémon atacante:")
    atacante = seleccionar_pokemon("Atacante")
    if atacante is None:
        return

    print("\n  Selecciona el Pokémon defensor:")
    defensor = seleccionar_pokemon("Defensor")
    if defensor is None:
        return

    if atacante is defensor:
        print("  ⚠️  Un Pokémon no puede atacarse a sí mismo.")
        return

    print(f"\n  🥊 ¡{atacante.nombre} VS {defensor.nombre}!")
    print("  " + "─" * 40)

    # ── El objeto defensor se pasa por referencia; su salud es modificada ──
    atacante.atacar(defensor)


# ══════════════════════════════════════════════════════════════════════════════
# OPCIÓN 6: LIBERAR UN POKÉMON (destructor)
# ══════════════════════════════════════════════════════════════════════════════

def liberar_pokemon() -> None:
    """
    Elimina un Pokémon de la lista global.
    Al eliminar la última referencia, Python llama automáticamente a __del__.

    Variable global modificada: pokemons_capturados.
    Variable local: indice, confirmacion.
    """
    global pokemons_capturados

    print("\n  ══ LIBERAR POKÉMON ══")

    if not pokemons_capturados:
        print("\n  ⚠️  No tienes Pokémon para liberar.")
        return

    print("\n  Pokémon disponibles:")
    for indice, poke in enumerate(pokemons_capturados, start=1):  # indice: var local
        print(f"    {indice}. {poke}")

    num = pedir_entero("Número del Pokémon a liberar", 1, len(pokemons_capturados))
    pokemon = pokemons_capturados[num - 1]

    confirmacion = input(  # variable local
        f"\n  ¿Seguro que quieres liberar a {pokemon.nombre}? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        # Remover de la lista y eliminar la referencia → activa __del__
        pokemons_capturados.pop(num - 1)
        del pokemon  # Elimina la referencia → llama a __del__
    else:
        print(f"\n  {pokemon.nombre} se queda contigo. 🤝")


# ══════════════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    """
    Función principal que controla el ciclo del menú.
    Usa la variable global pokemons_capturados a través de las funciones.
    """
    # ── Tabla de despacho: mapea opciones a funciones ─────────────────────
    acciones = {
        "1": capturar_pokemon,
        "2": entrenar_pokemon,
        "3": ver_informacion,
        "4": mostrar_total,
        "5": simular_batalla,
        "6": liberar_pokemon,
    }

    mostrar_banner()

    # ── Ciclo principal del menú ───────────────────────────────────────────
    while True:
        mostrar_menu_principal()
        opcion = input("\n  Elige una opción (1-7): ").strip()  # variable local

        if opcion == "7":
            print("\n  👋 ¡Hasta pronto, Entrenador! ¡Atrapa a todos! 🎯\n")
            break
        elif opcion in acciones:
            acciones[opcion]()  # Llamada a la función correspondiente
        else:
            print("  ⚠️  Opción no válida. Elige entre 1 y 7.")

        input("\n  Presiona ENTER para continuar...")
        limpiar_pantalla()
        mostrar_banner()


# ══════════════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
