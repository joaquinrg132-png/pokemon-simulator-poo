"""
=============================================================
  Simulador de Entrenamiento Pokémon
  Módulo: clases/pokemon.py
  Descripción: Define la clase Pokemon con todos los
               conceptos de POO requeridos.
=============================================================
"""

# ─── Variable global de clase (compartida entre todas las instancias) ──────────
# Se actualiza directamente en Pokemon._total para no depender del
# contador mutable desde fuera de la clase.

class Pokemon:
    """
    Representa a un Pokémon con sus estadísticas y comportamientos.

    Atributos de clase
    ------------------
    _total : int
        Número total de Pokémon que han sido creados (variable de clase).

    Atributos de instancia
    ----------------------
    nombre   : str   – Nombre del Pokémon.
    tipo     : str   – Tipo elemental (Fuego, Agua, Eléctrico, etc.).
    nivel    : int   – Nivel actual; inicia en 1.
    ataque   : int   – Puntos de ataque base.
    defensa  : int   – Puntos de defensa base.
    salud    : int   – Puntos de salud actuales.
    salud_max: int   – Puntos de salud máximos (igual a salud inicial).
    """

    # ── Variable de clase ──────────────────────────────────────────────────────
    _total: int = 0  # Cuenta cuántos Pokémon existen actualmente

    # ══════════════════════════════════════════════════════════════════════════
    # CONSTRUCTOR
    # ══════════════════════════════════════════════════════════════════════════
    def __init__(self, nombre: str, tipo: str,
                 ataque: int, defensa: int, salud: int) -> None:
        """
        Inicializa un nuevo Pokémon con los valores dados.

        Parámetros
        ----------
        nombre  : str – Nombre del Pokémon.
        tipo    : str – Tipo elemental.
        ataque  : int – Puntos de ataque base.
        defensa : int – Puntos de defensa base.
        salud   : int – Puntos de salud base.

        Nota: 'nivel' siempre inicia en 1.
        """
        # ── Atributos de instancia (self) ──────────────────────────────────
        self.nombre    = nombre       # Paso de parámetro por valor (str inmutable)
        self.tipo      = tipo
        self.nivel     = 1            # Nivel inicial siempre es 1
        self.ataque    = ataque
        self.defensa   = defensa
        self.salud     = salud
        self.salud_max = salud        # Guardamos la salud máxima para referencia

        # ── Actualizar contador de clase ───────────────────────────────────
        Pokemon._total += 1

        # ── Mensaje de creación ────────────────────────────────────────────
        print(f"\n  ✨ ¡{self.nombre} ({self.tipo}) ha sido capturado! "
              f"[Nivel {self.nivel}]")

    # ══════════════════════════════════════════════════════════════════════════
    # DESTRUCTOR
    # ══════════════════════════════════════════════════════════════════════════
    def __del__(self) -> None:
        """
        Se ejecuta cuando el objeto es eliminado de memoria.
        Muestra un mensaje de despedida y decrementa el contador.
        """
        # Protección ante errores durante el apagado del intérprete
        try:
            Pokemon._total -= 1
            print(f"\n  🕊️  {self.nombre} ha sido liberado ✨")
        except Exception:
            pass

    # ══════════════════════════════════════════════════════════════════════════
    # MÉTODOS DE INSTANCIA
    # ══════════════════════════════════════════════════════════════════════════

    def entrenar(self, *args) -> None:
        """
        Entrena al Pokémon aumentando su nivel y sus estadísticas.

        Sobrecarga mediante *args
        ─────────────────────────
        Sin argumentos  → aumenta ataque, defensa y salud con valores
                          predeterminados escalados por nivel.
        1 argumento     → sólo mejora el ataque en la cantidad indicada.
        2 argumentos    → mejora ataque y defensa en las cantidades indicadas.
        3+ argumentos   → mejora ataque, defensa y salud con los valores dados.

        Parámetros
        ----------
        *args : int (opcional) – Cantidades de mejora para cada estadística.

        Variables locales
        -----------------
        bonus_ataque, bonus_defensa, bonus_salud : int
            Incrementos que se aplicarán en esta sesión de entrenamiento.
        """
        # ── Variables locales (ámbito de función) ──────────────────────────
        bonus_ataque  = 0
        bonus_defensa = 0
        bonus_salud   = 0

        if len(args) == 0:
            # Sin argumentos: mejora automática escalada al nivel actual
            bonus_ataque  = 5 + self.nivel * 2
            bonus_defensa = 3 + self.nivel
            bonus_salud   = 10 + self.nivel * 3

        elif len(args) == 1:
            # 1 argumento: sólo ataque
            bonus_ataque = int(args[0])

        elif len(args) == 2:
            # 2 argumentos: ataque y defensa
            bonus_ataque  = int(args[0])
            bonus_defensa = int(args[1])

        else:
            # 3 o más argumentos: ataque, defensa y salud
            bonus_ataque  = int(args[0])
            bonus_defensa = int(args[1])
            bonus_salud   = int(args[2])

        # ── Subir nivel ────────────────────────────────────────────────────
        self.nivel    += 1

        # ── Aplicar bonificaciones (modificación por referencia del objeto) ──
        self.ataque   += bonus_ataque
        self.defensa  += bonus_defensa
        self.salud    += bonus_salud
        self.salud_max = self.salud    # La salud máxima crece con el entrenamiento

        # ── Mostrar resultado ──────────────────────────────────────────────
        print(f"\n  💪 ¡{self.nombre} ha entrenado duro!")
        print(f"     Nivel     : {self.nivel - 1} → {self.nivel}")
        if bonus_ataque  > 0:
            print(f"     Ataque    : +{bonus_ataque}")
        if bonus_defensa > 0:
            print(f"     Defensa   : +{bonus_defensa}")
        if bonus_salud   > 0:
            print(f"     Salud     : +{bonus_salud}")

    # ──────────────────────────────────────────────────────────────────────────
    def mostrar_info(self) -> None:
        """
        Muestra todos los datos del Pokémon en un formato legible.
        Accede a los atributos usando self.
        """
        barra = self._barra_salud()
        print(f"""
  ╔══════════════════════════════════════╗
  ║  🐾  {self.nombre:<33}║
  ╠══════════════════════════════════════╣
  ║  Tipo     : {self.tipo:<27}║
  ║  Nivel    : {self.nivel:<27}║
  ║  Ataque   : {self.ataque:<27}║
  ║  Defensa  : {self.defensa:<27}║
  ║  Salud    : {self.salud}/{self.salud_max:<21}║
  ║  HP       : {barra:<27}║
  ╚══════════════════════════════════════╝""")

    # ──────────────────────────────────────────────────────────────────────────
    def atacar(self, objetivo: "Pokemon") -> None:
        """
        Simula un ataque a otro Pokémon.
        El daño se calcula con:  daño = max(1, self.ataque - objetivo.defensa // 2)

        Parámetros
        ----------
        objetivo : Pokemon – El Pokémon que recibirá el daño.
                              Se pasa por referencia (objeto mutable),
                              por lo que sus atributos son modificados.

        Variables locales
        -----------------
        daño    : int  – Daño calculado para este ataque.
        critico : bool – Indica si el ataque fue crítico (1 en 5).
        """
        import random  # ámbito local de import

        # ── Variables locales ──────────────────────────────────────────────
        critico = random.randint(1, 5) == 1
        daño    = max(1, self.ataque - objetivo.defensa // 2)

        if critico:
            daño = int(daño * 1.5)

        # ── Modificar la salud del objetivo (paso por referencia) ──────────
        objetivo.salud = max(0, objetivo.salud - daño)

        # ── Mostrar resultado ──────────────────────────────────────────────
        tipo_ataque = "¡CRÍTICO! 💥" if critico else "⚔️"
        print(f"\n  {tipo_ataque}  {self.nombre} ataca a {objetivo.nombre}!")
        print(f"     Daño causado  : {daño}")
        print(f"     Salud restante: {objetivo.salud}/{objetivo.salud_max}")

        if objetivo.salud == 0:
            print(f"     💀 ¡{objetivo.nombre} ha sido derrotado!")

    # ══════════════════════════════════════════════════════════════════════════
    # MÉTODO DE CLASE
    # ══════════════════════════════════════════════════════════════════════════

    @classmethod
    def total_pokemons(cls) -> None:
        """
        Muestra cuántos Pokémon han sido creados y siguen activos.
        Accede a la variable de clase a través de 'cls'.
        """
        print(f"\n  🧮 Pokémon activos en el sistema: {cls._total}")

    # ══════════════════════════════════════════════════════════════════════════
    # MÉTODO DE PODER TOTAL
    # ══════════════════════════════════════════════════════════════════════════

    def poder_total(self) -> int:
        """
        Calcula y retorna el poder total del Pokémon.
        Fórmula: (ataque + defensa + salud) * nivel

        Retorno
        -------
        int – Puntuación de poder total.
        """
        # Variable local para el cálculo
        poder = (self.ataque + self.defensa + self.salud) * self.nivel
        return poder

    # ══════════════════════════════════════════════════════════════════════════
    # MÉTODO PRIVADO AUXILIAR
    # ══════════════════════════════════════════════════════════════════════════

    def _barra_salud(self) -> str:
        """
        Genera una barra de salud visual de 10 caracteres.

        Retorno
        -------
        str – Barra de salud con emojis.
        """
        if self.salud_max == 0:
            return "░░░░░░░░░░"
        # Variable local: porcentaje de salud
        porcentaje = self.salud / self.salud_max
        llenas     = int(porcentaje * 10)
        vacias     = 10 - llenas
        return "█" * llenas + "░" * vacias

    # ──────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        """Representación legible del Pokémon (usada en print())."""
        return (f"{self.nombre} [{self.tipo}] "
                f"Lv.{self.nivel} | "
                f"ATK:{self.ataque} DEF:{self.defensa} HP:{self.salud}")

    def __repr__(self) -> str:
        """Representación técnica del Pokémon."""
        return (f"Pokemon(nombre='{self.nombre}', tipo='{self.tipo}', "
                f"nivel={self.nivel}, ataque={self.ataque}, "
                f"defensa={self.defensa}, salud={self.salud})")
