# 🎮 Simulador de Entrenamiento Pokémon

> **Programación Orientada a Objetos** · Python 3.x · TecNM Campus Aguascalientes

## 📋 Descripción

Simulador interactivo de entrenamiento Pokémon desarrollado en Python que aplica los conceptos fundamentales de la Programación Orientada a Objetos (POO).

## 🧩 Conceptos de POO Implementados

| Concepto | Implementación |
|---|---|
| **Constructor `__init__`** | Inicializa atributos y muestra mensaje de captura |
| **Destructor `__del__`** | Mensaje `"Pokémon ha sido liberado ✨"` al eliminar |
| **Métodos de instancia** | `entrenar()`, `mostrar_info()`, `atacar()` |
| **Método de clase** | `@classmethod total_pokemons(cls)` |
| **Sobrecarga con `*args`** | `entrenar()` acepta 0, 1, 2 ó 3+ argumentos |
| **Variable de clase** | `Pokemon._total` — contador compartido |
| **Variables globales/locales** | `pokemons_capturados` global; `daño`, `bonus_*` locales |
| **Paso por valor** | Primitivos `str`/`int` en el constructor |
| **Paso por referencia** | Objeto `objetivo` en `atacar()` |

## 📁 Estructura del Proyecto

```
pokemon_simulator/
│
├── main.py                  ← Menú interactivo principal
├── reporte_pokemon.html     ← Reporte PDF del proyecto
└── clases/
    ├── __init__.py
    └── pokemon.py           ← Clase Pokemon completa
```

## 🚀 Cómo Ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/[TU-USUARIO]/pokemon-simulator-poo.git
cd pokemon-simulator-poo

# Ejecutar el simulador
python3 main.py
```

## 🕹️ Opciones del Menú

```
1. Capturar nuevo Pokémon  🐉  → Constructor __init__ en acción
2. Entrenar un Pokémon     💪  → Sobrecarga con *args (0-3 args)
3. Ver información         📋  → mostrar_info() + poder_total()
4. Total de Pokémon        🧮  → Método de clase total_pokemons()
5. Simular batalla         ⚔️  → atacar() con paso por referencia
6. Liberar un Pokémon      🕊️  → Destructor __del__ activado
7. Salir                   🚪
```

## 📊 Pokémon Predefinidos

| # | Nombre | Tipo | ATK | DEF | HP |
|---|---|---|---|---|---|
| 1 | Pikachu | Eléctrico | 55 | 40 | 35 |
| 2 | Charizard | Fuego | 84 | 78 | 78 |
| 3 | Blastoise | Agua | 83 | 100 | 79 |
| 4 | Bulbasaur | Planta | 49 | 49 | 45 |
| 5 | Mewtwo | Psíquico | 110 | 90 | 106 |
| 6 | Gengar | Veneno | 65 | 60 | 60 |
| 7 | Snorlax | Normal | 110 | 65 | 160 |
| 8 | Dragonite | Dragón | 134 | 95 | 91 |

---

*Desarrollado para la materia de Programación Orientada a Objetos · TecNM · Octubre 2026*
