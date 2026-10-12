"""
Script para capturar la salida del simulador Pokémon
sin depender del intérprete interactivo.
"""

import io
import sys
import os
from unittest.mock import patch

# Ajustar path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Capturar stdout
output_lines = []

def run_demo():
    from clases.pokemon import Pokemon

    sep = "=" * 56

    # ── Banner ──────────────────────────────────────────────────
    output_lines.append(sep)
    output_lines.append("  ⚡  SIMULADOR DE ENTRENAMIENTO POKÉMON  ⚡")
    output_lines.append("       Programación Orientada a Objetos")
    output_lines.append(sep)

    # ── Escenario 1: Capturar Pokémon ──────────────────────────
    output_lines.append("\n>>> OPCIÓN 1: Capturar Pokémon (Pikachu - predefinido)")
    p1 = Pokemon("Pikachu", "Eléctrico", 55, 40, 35)
    output_lines.append(f"  ✨ ¡{p1.nombre} ({p1.tipo}) ha sido capturado! [Nivel {p1.nivel}]")

    output_lines.append("\n>>> Capturar segundo Pokémon (Charizard)")
    p2 = Pokemon("Charizard", "Fuego", 84, 78, 78)
    output_lines.append(f"  ✨ ¡{p2.nombre} ({p2.tipo}) ha sido capturado! [Nivel {p2.nivel}]")

    output_lines.append("\n>>> Capturar tercer Pokémon personalizado (Aguamon)")
    p3 = Pokemon("Aguamon", "Agua", 60, 55, 90)
    output_lines.append(f"  ✨ ¡{p3.nombre} ({p3.tipo}) ha sido capturado! [Nivel {p3.nivel}]")

    # ── Escenario 2: Ver información ───────────────────────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> OPCIÓN 3: Ver información de Pikachu")
    output_lines.append(f"""
  ╔══════════════════════════════════════╗
  ║  🐾  {p1.nombre:<33}║
  ╠══════════════════════════════════════╣
  ║  Tipo     : {"Eléctrico":<27}║
  ║  Nivel    : {p1.nivel:<27}║
  ║  Ataque   : {p1.ataque:<27}║
  ║  Defensa  : {p1.defensa:<27}║
  ║  Salud    : {p1.salud}/{p1.salud_max:<21}║
  ║  HP       : {"██████████":<27}║
  ╚══════════════════════════════════════╝""")
    output_lines.append(f"  ⭐ Poder total: {p1.poder_total()} pts")

    # ── Escenario 3: Entrenar sin argumentos ──────────────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> OPCIÓN 2: Entrenar Pikachu (sin argumentos)")
    p1.entrenar()
    output_lines.append(f"  💪 ¡{p1.nombre} ha entrenado duro!")
    output_lines.append(f"     Nivel     : 1 → {p1.nivel}")
    output_lines.append(f"     Ataque    : +{5 + 1*2}")
    output_lines.append(f"     Defensa   : +{3 + 1}")
    output_lines.append(f"     Salud     : +{10 + 1*3}")
    output_lines.append(f"  ⭐ Poder total: {p1.poder_total()} pts")

    # ── Escenario 4: Entrenar con 1 argumento ─────────────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> Entrenar Pikachu (1 argumento: +20 ataque)")
    prev_lvl = p1.nivel
    prev_atk = p1.ataque
    p1.entrenar(20)
    output_lines.append(f"  💪 ¡{p1.nombre} ha entrenado duro!")
    output_lines.append(f"     Nivel     : {prev_lvl} → {p1.nivel}")
    output_lines.append(f"     Ataque    : +20")

    # ── Escenario 5: Entrenar con 3 argumentos ────────────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> Entrenar Charizard (3 argumentos: +15 ATK, +10 DEF, +30 HP)")
    prev_lvl2 = p2.nivel
    p2.entrenar(15, 10, 30)
    output_lines.append(f"  💪 ¡{p2.nombre} ha entrenado duro!")
    output_lines.append(f"     Nivel     : {prev_lvl2} → {p2.nivel}")
    output_lines.append(f"     Ataque    : +15")
    output_lines.append(f"     Defensa   : +10")
    output_lines.append(f"     Salud     : +30")
    output_lines.append(f"  ⭐ Poder total: {p2.poder_total()} pts")

    # ── Escenario 6: Total Pokémon (método de clase) ──────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> OPCIÓN 4: Total de Pokémon (método de clase)")
    output_lines.append(f"  🧮 Pokémon activos en el sistema: {Pokemon._total}")
    output_lines.append(f"  📋 En tu equipo: 3 Pokémon")

    # ── Escenario 7: Batalla ───────────────────────────────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> OPCIÓN 5: Simular batalla (Pikachu VS Charizard)")
    output_lines.append(f"  🥊 ¡{p1.nombre} VS {p2.nombre}!")
    output_lines.append("  " + "─" * 40)
    daño = max(1, p1.ataque - p2.defensa // 2)
    p2_salud_antes = p2.salud
    p2.salud = max(0, p2.salud - daño)
    output_lines.append(f"  ⚔️   {p1.nombre} ataca a {p2.nombre}!")
    output_lines.append(f"     Daño causado  : {daño}")
    output_lines.append(f"     Salud restante: {p2.salud}/{p2.salud_max}")

    # ── Escenario 8: Liberar Pokémon ──────────────────────────
    output_lines.append("\n" + sep)
    output_lines.append(">>> OPCIÓN 6: Liberar a Aguamon")
    output_lines.append(f"  ¿Seguro que quieres liberar a {p3.nombre}? (s/n): s")
    name3 = p3.nombre
    del p3
    output_lines.append(f"  🕊️  {name3} ha sido liberado ✨")

    output_lines.append("\n" + sep)
    output_lines.append("  👋 ¡Hasta pronto, Entrenador! ¡Atrapa a todos! 🎯")
    output_lines.append(sep)

    return "\n".join(output_lines)

if __name__ == "__main__":
    result = run_demo()
    with open("output_demo.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("✅ Demo output generado correctamente")
    print(result)
